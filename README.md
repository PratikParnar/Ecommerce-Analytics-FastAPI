# 🛒 E-Commerce Analytics API & Dashboard

## 📌 Project Overview
This project is an end-to-end E-Commerce Analytics solution built using Python, Pandas, FastAPI, and Streamlit. The objective is to transform raw e-commerce transaction data into meaningful business insights through data analysis, RESTful APIs, and an interactive dashboard.

Using the Brazilian E-Commerce (Olist) dataset, the project analyzes customer behavior, revenue trends, payment methods, product performance, and regional sales patterns.

---

## 🚀 Key Objectives
- Analyze e-commerce sales performance
- Track revenue and order trends
- Understand customer distribution across regions
- Identify top-performing products
- Monitor payment preferences
- Provide analytics through FastAPI endpoints
- Visualize insights through an interactive Streamlit dashboard

---

## 🛠️ Technology Stack
| Category | Tools |
|-----------|--------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| API Development | FastAPI |
| Dashboard | Streamlit |
| Data Visualization | Plotly, Matplotlib |
| Development Environment | Jupyter Notebook |
| Deployment | Render |
| Version Control | Git & GitHub |

---

## 📊 Business Insights Generated

### Revenue Analytics
- Total Revenue
- Monthly Revenue Trends
- Average Order Value
- State-wise Revenue Distribution

### Customer Analytics
- Total Customers
- Top Customer States
- Customer Distribution Analysis

### Product Analytics
- Best Selling Products
- Product Performance Insights

### Order Analytics
- Total Orders
- Order Status Breakdown
- Monthly Order Trends

### Payment Analytics
- Most Preferred Payment Methods
- Payment Distribution Analysis

---

## 🔗 Available API Endpoints
| Endpoint | Description |
|-----------|------------|
| `/total-orders` | Returns total orders |
| `/order-status` | Order status distribution |
| `/monthly-orders` | Monthly order trends |
| `/total-revenue` | Total revenue generated |
| `/average-order-value` | Average order value |
| `/payment-methods` | Payment method analysis |
| `/top-states` | Top customer states |
| `/total-customers` | Total customers |
| `/monthly-revenue` | Revenue trend by month |
| `/top-products` | Best-selling products |
| `/state-revenue` | Revenue by state |
| `/customer-insights` | Customer analytics |
| `/dashboard-summary` | Overall business summary |

---

## 📊 Streamlit Dashboard

An interactive analytics dashboard built with Streamlit, connected to the FastAPI backend.

### Dashboard Features
| Feature | Description |
|---------|-------------|
| 📈 Key Metrics | Total Revenue, Orders, Avg Order Value, Customers |
| 📅 Monthly Revenue | Month-wise revenue trend (Line Chart) |
| 💳 Payment Methods | Payment distribution (Pie Chart) |
| 🗺️ Top States | Revenue by state (Bar Chart) |
| 📦 Order Status | Order status breakdown (Bar Chart) |
| 🏷️ Top Categories | Best performing product categories |
| 🏙️ Top Cities | Most active cities by orders |
| 🔍 Raw Data | Interactive data table preview |

### Dashboard Filters
- 📅 Filter by Year
- 🗺️ Filter by State

### 📸 Dashboard Preview

### 🔢 Key Metrics
![Key Metrics](assets/Key%20Metrics.png.png)

### 📅 Monthly Revenue & 💳 Payment Methods
![Monthly Revenue](assets/Monthly%20Revenue.png.png)

### 🗺️ Top States & 📦 Order Status
![Top States](assets/Top%20States.png.png)

### 🏷️ Top Product Categories
![Top Categories](assets/Top%20Categories.png.png)

### 🏙️ Top Cities
![Top Cities](assets/Top%20Cities.png.png)

### 🎛️ Dashboard Sidebar
![Dashboard Sidebar](assets/Dashboard%20Sidebar.png.png)

---

## 📂 Dataset
**Brazilian E-Commerce Public Dataset by Olist**

Dataset includes:
- Orders
- Customers
- Products
- Payments
- Sellers
- Reviews
- Geolocation Information

---

## 📁 Project Structure
```
Ecommerce_Project/
│
├── E-Commerce Analytics.ipynb   # EDA & Data Analysis
├── main.py                      # FastAPI Backend
├── requirements.txt             # Dependencies
├── README.md                    # Project Documentation
│
├── streamlit_dashboard/
│   ├── dashboard.py             # Streamlit Dashboard
│   └── requirements_dashboard.txt
│
└── assets/
    └── dashboard_screenshot.png # Dashboard Preview
```

---

## 🎯 Project Highlights
✔ Data Cleaning & Preprocessing  
✔ Exploratory Data Analysis (EDA)  
✔ Business Intelligence Insights  
✔ FastAPI REST APIs  
✔ Interactive Streamlit Dashboard  
✔ Customer & Revenue Analytics  
✔ Product Performance Analysis  
✔ Deployed on Render  
✔ GitHub Version Control  

---

## ⚙️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd Ecommerce_Project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run FastAPI
```bash
uvicorn main:app --reload
```

### 4. Run Streamlit Dashboard
```bash
cd streamlit_dashboard
streamlit run dashboard.py
```

---

## 🚀 Live Demo
🔗 **FastAPI Swagger UI:** https://ecommerce-analytics-fastapi.onrender.com/docs

---

## 👨‍💻 Author
**Pratikkumar Parmar**  
Aspiring Data Analyst | Python | Power BI | FastAPI | Streamlit | Data Analytics

---

⭐ If you found this project interesting, feel free to star the repository!
