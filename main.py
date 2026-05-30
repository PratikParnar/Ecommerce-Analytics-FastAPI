from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load dataset
orders = pd.read_csv("olist_orders_dataset.csv")

@app.get("/")
def home():

    return {
        "message": "E-Commerce Analytics API Running"
    }


# total order api
@app.get("/total-orders")
def total_orders():

    return{
        "total_orders": int(orders.shape[0])
    }

# order status
@app.get("/order-status")
def order_status():

    status = orders["order_status"].value_counts().to_dict()

    return status

# monthly order -- datetime conversion
orders["order_purchase_timestamp"]  = pd.to_datetime(orders["order_purchase_timestamp"])

orders["purchase_month"] = (orders["order_purchase_timestamp"].dt.month)

@app.get("/monthly-orders")
def monthly_orders():

    monthly = (orders["purchase_month"].value_counts().sort_index().to_dict())

    return monthly

# total revenue api
payments = pd.read_csv("olist_order_payments_dataset.csv")

@app.get("/total-revenue")
def total_revenue():

    revenue = payments["payment_value"].sum()

    return {
        "total_revenue": round(float(revenue), 2)
    }
# avg order value api
@app.get("/average-order-value")
def average_order_value():

    avg = payments["payment_value"].mean()

    return{
        "average_order_value": round(float(avg), 2)
    }

# payment method api
@app.get("/payment-method")
def payment_method():

    methods = (payments["payment_type"].value_counts().to_dict())

    return methods

# top states api
customers = pd.read_csv("olist_customers_dataset.csv")

merged_df = pd.merge(orders,customers,on="customer_id",how="left")

@app.get("/top-states")
def top_states():

    states = (merged_df["customer_state"].value_counts().head(10).to_dict())

    return states

# total customers
@app.get("/total-customers")
def total_customers():

    total = customers["customer_unique_id"].nunique()

    return {
        "total_customers": int(total)
    }

@app.get("/top-states")
def top_states(limit: int = 10):

    states = (merged_df["customer_state"].value_counts().head(limit).to_dict())

    return states

@app.get("/orders-by-status")
def orders_by_status(status: str):

    filtered = orders[
               orders["order_status"] == status
        ]

    return {
        "status": status,
        "total_orders": int(filtered.shape[0])
    }

@app.get("/revenue-by-payment")
def revenue_by_payment(payment_type: str):

    filtered = payments[
        payments["payment_type"] == payment_type
    ]

    revenue = filtered["payment_value"].sum()

    return {
        "payment_type": payment_type,
        "revenue": round(float(revenue), 2)
          }

@app.get("/orders/{order_id}")
def get_order(order_id: str):

    order = orders[
        orders["order_id"] == order_id
    ]

    return order.to_dict(orient="records")


@app.get("/state/{state}")
def state_orders(state: str):

    filtered = merged_df[
        merged_df["customer_state"] == state.upper()
    ]

    return {
        "state": state,
        "orders": int(filtered.shape[0])
    }


# POST API

from pydantic import BaseModel

class Feedback(BaseModel):
    name : str
    rating : int
    comment: str
    
@app.post("/feedback")
def add_feedback(feedback: Feedback):

    return{
        "message": "Feedback received",
        "data": feedback
    }


class OrderUpdate(BaseModel):
    order_status: str 

@app.put("/orders/{order_id}")
def update_order(
    order_id: str,
    order: OrderUpdate
):

    return{
        "message":"Order Update Successfully",
        "order_id": order_id,
        "new_status": order.update_status
    }

products = pd.read_csv("olist_products_dataset.csv")

order_items = pd.read_csv("olist_order_items_dataset.csv")

product_df =pd.merge(order_items, products, on="product_id", how="left")

@app.get("/top-products")
def top_products():

    products = (
        product_df["product_category_name"]
        .value_counts()
        .head(10)
        .to_dict()
    )

    return products

revenue_df = pd.merge(orders,payments,on="order_id",how="left")

state_revenue_df = pd.merge(revenue_df, customers, on="customer_id", how="left")

@app.get("/state-revenue")
def state_revenue(limit: int = 10):

    revenue = (
        state_revenue_df
        .groupby("customer_state")["payment_value"]
        .sum()
        .sort_values(ascending=False)
        .head(limit)
        .to_dict()
    )

    return revenue


# Customer insights API 

@app.get("/customer-insights")
def customer_insights():

    total_customers = customers["customer_unique_id"].nunique()

    top_states = (
        customers["customer_state"]
        .value_counts()
        .head(5)
        .to_dict()
    )

    top_cities = (
        customers["customer_city"]
        .value_counts()
        .head(5)
        .to_dict()
    )

    return {
        "total_customers": int(total_customers),
        "top_states": top_states,
        "top_cities": top_cities
    }


@app.get("/dashboard-summary")
def dashboard_summary():

    return{
        "total_orders": int(orders.shape[0]),
        "total_customers":int(
            customers["customer_unique_id"].nunique()
            ),
        "total_revenue": round(
            float(payments["payment_value"].sum()), 2
        )
    }














    


    