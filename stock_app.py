import streamlit as st
import yfinance as yf
import streamlit as st

st.set_page_config(
    page_title="Stock Price Visualisation App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/gopal-kadam-4b29bb22a/',
        'Report a bug': "https://www.linkedin.com/in/gopal-kadam-4b29bb22a/",
        'About': "Developed by Gopal Kadam"
    }
)
st.header("Stock Price Visualisation App")
stock_sym = st.text_input("Select Stock")
col1,col2 = st.columns(2)

with col1:
    start_date = st.date_input("Enter start date")
with col2:
    end_date = col2.date_input("Enter end date")

if st.button("Get Data"):
    data = yf.download(stock_sym, start=start_date, end=end_date)
    st.dataframe(data.head(5))
    col1,col2 = st.columns(2)
    with col1:
        st.line_chart(data['Close'],x_label="Dates",y_label="Closing stock price")
    with col2:
        st.bar_chart(data['Volume'],x_label="Dates",y_label="Volume of stock")
