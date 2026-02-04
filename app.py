import streamlit as st
import pandas as pd
import pickle
import os
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(
    page_title="Traffic Prediction Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

MODEL_FILE = "traffic_model.pkl"


st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background-color: #0f172a;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* cards */
.card {
    background-color: #1e293b;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.4);
}

/* big numbers */
.big {
    font-size: 60px;
    font-weight: bold;
    color: #38bdf8;
}

.block-container {
    padding-top: 1.2rem;
}

</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_model():
    df = pd.read_csv("traffic.csv")

    df['DateTime'] = pd.to_datetime(df['DateTime'])
    df['Hour'] = df['DateTime'].dt.hour
    df['Day'] = df['DateTime'].dt.day
    df['Month'] = df['DateTime'].dt.month
    df['Weekday'] = df['DateTime'].dt.weekday

    df.drop(columns=['DateTime', 'ID'], inplace=True)

    X = df.drop("Vehicles", axis=1)
    y = df["Vehicles"]

    model = RandomForestRegressor()
    model.fit(X, y)

    pickle.dump(model, open(MODEL_FILE, "wb"))

    return model, df


if os.path.exists(MODEL_FILE):
    model = pickle.load(open(MODEL_FILE, "rb"))
    df = pd.read_csv("traffic.csv")
else:
    model, df = load_model()

st.markdown("""
<div class="card">
<h1>🚦 Traffic Volume Prediction System</h1>
<p>ML based congestion forecasting dashboard</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.title("⚙️ Controls")

junction = st.sidebar.selectbox("Junction", sorted(df["Junction"].unique()))
date = st.sidebar.date_input("Date")
time = st.sidebar.time_input("Time")

predict = st.sidebar.button("🚦 Predict Traffic")

tab1, tab2 = st.tabs(["📊 Dashboard", "📈 Analytics"])


with tab1:

    left, right = st.columns([2, 1])

    # -------- Traffic Trend --------
    with left:
        st.subheader("Traffic Trend")
        fig = px.line(df.head(300), y="Vehicles")
        st.plotly_chart(fig, use_container_width=True)

    # -------- Prediction Card --------
    with right:
        st.subheader("Prediction")

        if predict:

            input_df = pd.DataFrame({
                "Junction": [junction],
                "Hour": [time.hour],
                "Day": [date.day],
                "Month": [date.month],
                "Weekday": [date.weekday()]
            })

            pred = int(model.predict(input_df)[0])

            st.markdown(f"""
            <div class="card">
                <p>Predicted Vehicles</p>
                <div class="big">{pred}</div>
            </div>
            """, unsafe_allow_html=True)

            if pred <= 30:
                st.success("🟢 Low Traffic")
            elif pred <= 60:
                st.warning("🟡 Medium Traffic")
            else:
                st.error("🔴 Heavy Traffic")

        else:
            st.info("Waiting to predict → Click Predict")

with tab2:

    df['DateTime'] = pd.to_datetime(df['DateTime'])

    # -------- Month Chart --------
    st.subheader("Month-wise Traffic Flow")

    df['Month'] = df['DateTime'].dt.month
    monthly = df.groupby("Month")["Vehicles"].sum().reset_index()

    fig_month = px.bar(monthly, x="Month", y="Vehicles")
    st.plotly_chart(fig_month, use_container_width=True)


    # -------- Year Chart --------
    st.subheader("Traffic Growth Over Years")

    df['Year'] = df['DateTime'].dt.year
    yearly = df.groupby("Year")["Vehicles"].sum().reset_index()

    fig_year = px.line(yearly, x="Year", y="Vehicles", markers=True)
    st.plotly_chart(fig_year, use_container_width=True)
