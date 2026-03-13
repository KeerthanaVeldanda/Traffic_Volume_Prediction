# 🚦 Traffic Volume Prediction Dashboard

## 📌 Overview

Traffic Volume Prediction Dashboard is a **Machine Learning based web application** built using **Streamlit** that predicts traffic congestion levels based on date, time, and junction information.

The system analyzes historical traffic data and uses a **Random Forest Regression model** to forecast the number of vehicles expected at a particular time.

The dashboard also provides **interactive visualizations** to understand traffic patterns and congestion trends.

---

## ✨ Features

* Predict traffic volume using Machine Learning
* Interactive **Streamlit dashboard**
* Traffic congestion classification (Low, Medium, Heavy)
* Month-wise traffic analysis
* Year-wise traffic growth visualization
* Real-time prediction based on user input
* Modern UI dashboard with Plotly charts

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* Plotly
* Pickle (model serialization)

---

## 📂 Project Structure

```
Traffic_Volume_Prediction
│
├── traffic.csv                # Dataset
├── traffic_model.pkl          # Trained ML model
├── app.py                     # Streamlit dashboard
├── requirements.txt           # Python dependencies
└── README.md
```

---

## ⚙️ Machine Learning Model

The system uses **Random Forest Regressor** to predict vehicle traffic volume.

### Features Used

* Junction
* Hour
* Day
* Month
* Weekday

### Target

* Vehicles (traffic volume)

---

## 🚀 Installation

Clone the repository

```
git clone https://github.com/yourusername/Traffic_Volume_Prediction.git
```

Navigate to the project folder

```
cd Traffic_Volume_Prediction
```

Install required libraries

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit app:

```
streamlit run app.py
```

Then open the browser:

```
http://localhost:8501
```

---

## 📊 Dashboard Components

### Traffic Trend

Shows vehicle movement trends over time using interactive line charts.

### Traffic Prediction

Predicts the number of vehicles based on:

* Selected junction
* Date
* Time

### Traffic Analytics

Provides insights like:

* Month-wise traffic flow
* Year-wise traffic growth

---

## 🔮 Future Improvements

* Real-time traffic data integration
* Deployment on cloud (AWS / Streamlit Cloud)
* Deep learning models for higher accuracy
* Smart traffic alert system

---
