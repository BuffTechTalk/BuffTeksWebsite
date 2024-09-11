from datetime import date, datetime
import streamlit as st
import yfinance as yf
import plotly.express as px
from webpages import code_editor as ce

def pythonx_lesson3():
        
    st.title("Lesson 3: Collecting Stock Data Through API")
    st.header(":one: What is API")
    st.markdown(
        """
        API stands for **Application Programming Interface**. It is a set of protocols, routines, and tools for building software and applications. An API defines the way by which an external client can request services and access data from an operating system, library, or application. It provides a communication interface for two or more systems to exchange data and interact with each other. APIs are commonly used to enable developers to create new applications and services that integrate with existing systems or to extract data from websites and services for use in other applications.
        """)
    st.image("./images/lesson3-api.png")

    st.header(":two: Using yfinance Library(Package) to Extract Stock Data")
    st.markdown("""
        [yfinance](https://github.com/ranaroussi/yfinance) is a Python library that allows you to easily download and analyze financial data from Yahoo Finance. 

        It provides a convenient way to access stock market data and perform various operations with it such as 
        - retrieving historical data
        - getting real-time data
        - obtaining financial ratios and metrics, and more. 

        It provides a simple and efficient way to work with stock data in Python, without the need to manually scrape data from websites or manually download data from financial sources.
        """)
    
    st.header(":three: Application Demo")
    # print text formatted by HTML
    st.markdown(
        "<h1 style='text-align:center; color:red;'> Sample Stock Price App. </h1>",
        unsafe_allow_html=True)

    st.write(
        'We will use the code learned from previous lecture to build an online application for tracing stock price'
    )

    # print text in markdown
    st.markdown("## **Check Stock Information**")

    # a list of stock names
    stock_names = ['MSFT', 'AAPL', 'AMZN', 'GOOGL']
    # select a stock to check
    target_stock = st.selectbox('Select a stock to check', options=stock_names)

    st.markdown("## **Check Stock Price History**")

    # start date of the stock infomation, default is the first day of year 2024
    start_date = st.date_input('Start Date', datetime(2024, 1, 1))
    # end date of the stock infomation, default is date of today
    end_date = st.date_input("End Date")

    # get today date
    today = date.today()
    if st.button('Submit'):
        # check valid date
        if start_date > today or end_date > today:
            st.write("## **Please select a valid date period.**")
        else:
            # download the stock data based on stock name, start/end date
            data = yf.download(target_stock, start_date, end_date)
            # show a progress bar
            with st.spinner(text='In progress'):

                fig = px.line(data,
                            x=data.index,
                            y=['Open', 'High', 'Low', 'Close'],
                            title=target_stock + " Stock Price",
                            labels={
                                "value": "Stock Price ($)",
                                "variable": "Price Type"
                            })
                st.write(fig)
                st.success('Done')


