import streamlit as st
import pandas as pd
import pickle

col1,col2,col3,col4=st.columns([1,1,1,1])
with col1:
    if st.button("Home Page"):
        st.switch_page("app.py")
with col2:
     if st.button("Whatsapp Chat Analyzer"):
        st.switch_page("pages/whatsapp.py")
with col3:
    if st.button("Car Price Prediction"):
        st.switch_page("pages/car.py")
with col4:
    if st.button("Stock Price Prediction"):
        st.switch_page("pages/stock.py")

# Load data and model
car = pd.read_csv("refine_car.csv")
model = pickle.load(open("LinearRegressionModel.pkl", "rb"))

# Streamlit app
import streamlit as st

# Using markdown with HTML and CSS
st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    </style>
    <h1 class="title">Car Price Predictor</h1>
    """,
    unsafe_allow_html=True
)

# Get unique values for the dropdowns
companies = sorted(car["company"].unique())
car_models = sorted(car["name"].unique())
year = sorted(car["year"].unique(), reverse=True)
fuel_type = car["fuel_type"].unique()
kms_driven = car["kms_driven"].unique()

# dropdowns and input fields
selected_company = st.selectbox("Select company", companies)
selected_car_model = st.selectbox("Select Car Model", car_models)
selected_year = st.selectbox("Select Year", year)
selected_fuel_type = st.selectbox("Select Fuel Type", fuel_type)
selected_kms_driven = st.number_input("Enter Kilometers Driven", min_value=0, step=1000)

# Predict button
col1, col2,col3=st.columns([2,1,2])
with col2:
     predict_button=st.button("Predict Price")
if predict_button:
        try:
            # Prepare input data for prediction
            input_data = pd.DataFrame(
                [[selected_car_model, selected_company, selected_year, selected_kms_driven, selected_fuel_type]],
                columns=["name", "company", "year", "kms_driven", "fuel_type"],
                dtype="object",
            )

            # Make prediction
            prediction = model.predict(input_data)
            predicted_price = "{:,.2f}".format(prediction[0])

            # Display prediction
            st.success(f"The predicted price of the car is ${predicted_price}")
        except Exception as e:
            st.error(f"Error: {e}")    

    
