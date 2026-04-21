import streamlit as st
import pandas as pd
import joblib

@st.cache_data
def load_model():
    model = joblib.load("data/car_price_model.pkl")
    columns = joblib.load("data/model_columns.pkl")
    return model, columns

model, columns = load_model()

data = pd.read_csv("data/cleaned_data.csv", sep=';')

st.title("Used Car Price Predictor")
make = st.selectbox("Make", options=sorted(data['make'].unique()))
model_name = st.selectbox("Model", options=sorted(data['model'].unique()))
year = st.number_input("Year", min_value=1990, max_value=2024, value=2010)
mileage = st.number_input("Mileage", min_value=0, max_value=500000, value=50000)
engine_power = st.number_input("Engine Power (HP)", min_value=0, max_value=1000, value=150)
fuel_type = st.selectbox("Fuel Type", options=sorted(data['fuel_type'].unique()))
gearbox = st.selectbox("Gearbox", options=sorted(data['gearbox'].unique()))

if st.button("Predict Price"):
    input_data = pd.DataFrame({
        "make": [make],
        "model": [model_name],
        "year": [year],
        "mileage": [mileage],
        "engine_power": [engine_power],
        "fuel_type": [fuel_type],
        "gearbox": [gearbox]
    })

    input_data_encoded = pd.get_dummies(input_data, columns=['make', 'model', 'fuel_type', 'gearbox'], drop_first=True)
    input_data_encoded = input_data_encoded.reindex(columns=columns, fill_value=0)

    predicted_price = model.predict(input_data_encoded)[0]
    st.success(f"Predicted Price: {predicted_price:.2f} PLN")

