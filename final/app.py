import streamlit as st
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
        
# whatsapp chat analysis

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.title("Whatsapp Chat analyzer")
    
col1,col2,col3,col4=st.columns([1,1,1,1])
with col1:
    st.image("x_whatsapp_pic.png",width=600)
with col3:
    st.image("x_whatsapp-icon-6953522.jpg",width=600)

st.markdown("""
### Unleash the Hidden Insights

Dive into the depths of your daily chats or seek meaningful patterns with our cutting-edge ***WhatsApp Chat Analyzer***. This tool provides comprehensive analysis with ease, offering:

- Detailed statistics on the number of messages sent and received.
- Insights into active days and your busiest chat hours.
- Analysis of the most commonly used words in your chats.
- Identification of who you chat with the most and analysis of conversation dynamics with different contacts.

### Interactive and User-Friendly

Enjoy interactive charts and graphs that make it easy to visualize your chat data.Simply export your WhatsApp chat as a text file and upload it to our analyzer. Our powerful algorithms will process the chat data to extract valuable insights.

View and interact with the results through an intuitive and user-friendly interface. Unlock the potential of your conversations today with the WhatsApp Chat Analyzer – your personal window into the world of chat data!

#### Click the button below to analyze your chats 
""")
col1, col2, col3 = st.columns([1, 1, 1])
with col1 :
    if st.button("Analyze WhatsApp Chats"):
        st.switch_page("pages/whatsapp.py")
        
#  car price prediction

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.title("Car Price Predictor")
    
col1,col2,col3,col4=st.columns([1,1,1,1])
with col1:
     st.image("x_car.jpg",width=600)
with col3:
    st.image("x_car_price_new.jpg",width=600)
st.markdown("""
## Highlights

Unlock the power of accurate car valuations with our state-of-the-art ***Car Price Prediction*** tool, designed to provide precise and insightful assessments of any vehicle's worth. This tool is an invaluable resource for anyone looking to buy, sell, or simply understand the market value of a car. By leveraging advanced algorithms and extensive data analysis, our ***Car Price Prediction tool*** takes into account a multitude of factors including the ***car’s company, model, year, fuel type, and how many kilometers are driven by the car***.

**Key Features:**

- **User-Friendly Interface:** Enter the car's details into our easy-to-use interface and receive an instant, comprehensive price prediction that reflects the car's true market value.
- **In-Depth Analysis:** Our tool goes beyond simple estimates, offering in-depth analysis and visualizations that show how various attributes.
- **Versatile Use:** Perfect for car enthusiasts, dealerships, and anyone in the market for a vehicle. 
- **Informed Decisions:** Equip yourself with the knowledge needed to make informed, confident decisions. Whether you're negotiating a sale, making a purchase, or just curious about a car's value, our tool provides the detailed insights you need to navigate the automotive market effectively.
- **Best Deals:** Make data-driven decisions with confidence and ensure you get the best possible deal with our comprehensive Car Price Prediction tool.
#### Click the button to predict the price of the car you want 
""")
col1, col2, col3 = st.columns([1, 1, 1])
with col1 :
    if st.button("Predict price"):
        st.switch_page("pages/car.py")
        
# Stock price prediction
col1, col2 = st.columns([2,4])
with col2:
    st.title("Stock Price Predictor")
col1,col2,col3,col4=st.columns([1,1,1,1])
with col1:
    st.image("x_stock_price.jpg",width=600)
with col3:
    st.image("x_stock_price2.jpg",width=600)

    
# col1, col2, col3 = st.columns([1, 1, 1])
# with col2:
#     st.image("x_car.jpg",width=600)
    # st.image("x_Stock_Price_Prediction.webp",width=600)
