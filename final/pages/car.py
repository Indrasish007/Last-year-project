import streamlit as st
import pandas as pd
import pickle

# Load data and model
car = pd.read_csv("refine_car.csv")
model = pickle.load(open("LinearRegressionModel.pkl", "rb"))

# Streamlit app
st.title("Car Price Prediction")

# Get unique values for the dropdowns
companies = sorted(car["company"].unique())
car_models = sorted(car["name"].unique())
year = sorted(car["year"].unique(), reverse=True)
fuel_type = car["fuel_type"].unique()
kms_driven = car["kms_driven"].unique()

# Create dropdowns and input fields
selected_company = st.selectbox("Select Company", companies)
selected_car_model = st.selectbox("Select Car Model", car_models)
selected_year = st.selectbox("Select Year", year)
selected_fuel_type = st.selectbox("Select Fuel Type", fuel_type)
selected_kms_driven = st.number_input("Enter Kilometers Driven", min_value=0, step=1000)

# Predict button
if st.button("Predict Price"):
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

# from flask import Flask, render_template, request
# import pandas as pd
# import pickle

# app = Flask(__name__)
# car = pd.read_csv("refine_car.csv")
# model = pickle.load(open("LinearRegressionModel.pkl", "rb"))


# @app.route("/")
# def index():
#     companies = sorted(car["company"].unique())
#     car_models = sorted(car["name"].unique())
#     year = sorted(car["year"].unique(), reverse=True)
#     fuel_type = car["fuel_type"].unique()
#     kms_driven = car["kms_driven"].unique()

#     return render_template(
#         "index.html",
#         companies=companies,
#         car_models=car_models,
#         year=year,
#         fuel_types=fuel_type,
#         kms_driven=kms_driven,
#     )


# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         companies = request.form.get("companies")
#         car_models = request.form.get("car_models")
#         year = int(request.form.get("year") or 0)
#         fuel_type = request.form.get("fuel_type")
#         kms_driven = int(request.form.get("kms_driven") or 0)
#         print(companies, car_models, year, fuel_type, kms_driven)
#         prediction = model.predict(
#             pd.DataFrame(
#                 [[car_models, companies, year, kms_driven, fuel_type]],
#                 columns=["name", "company", "year", "kms_driven", "fuel_type"],
#                 dtype="object",
#             )
#         )

#         return "{:,.2f}".format(prediction[0])
#     except Exception as e:
#         print(e)
#         return {"error": "Something went wrong", "message": str(e)}


# if __name__ == "__main__":
#     app.run(debug=True)

# # from flask import Flask
# # import pandas as pd
# # app = Flask(__name__)
# # car=pd.read_csv('refine_car.csv')

# # @app.route('/')
# # def hello_world():
# #     companies=sorted(car['company'].unique())
# #     car_models=sorted(car['name'].unique())
# #     year= sorted(car['year'].unique(),reverse=True)
# #     fuel_type=car['fuel_type'].unique()
# #     return str(len(car_models))

# # if __name__=="__main__":
# #      app.run(debug=True)
