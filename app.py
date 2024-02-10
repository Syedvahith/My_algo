import streamlit as st
from newsapi import NewsApiClient
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta
import subprocess
import urllib
import json
import token_lookup
import conn
from RSI import hist_data, RSI, instrument_list
from resources import documentation, copyrights


# Set up API credentials
newsapi = NewsApiClient(api_key='')

# Create Streamlit app
st.set_page_config(page_title="Automated Stock Analysis", page_icon=":chart_with_upwards_trend:")

# Define the functions to display the text for each button
def display_dashboard():

    # banner Image on dashboard page
    dash_grande = '/home/wasim/Music/pjt/python-trading-system-main/resources/dash_grande.jpg'
    st.image(dash_grande, caption='A fully Automated AI based Trading System', use_column_width=True)

    #credentials  preview
    st.write("My Angel Broking Credentials")
    st.write(conn.userProfile)

    # button property
    st.write("<style>div.row-widget.stRadio > div{flex-direction:row;}</style>", unsafe_allow_html=True)

# Create center-placed button
    st.write("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
    button_clicked = st.button("Click here to Preview the Chart", key="preview_button")
    st.write("</div>", unsafe_allow_html=True)

# Add green glow effect on button click
    if button_clicked:
        st.write("<style>div.stButton > button:first-child {box-shadow: 0 0 15px #7fff00; marigin:auto; width:50%;}</style>", unsafe_allow_html=True)
        st.write('<meta http-equiv="refresh" content="0; URL=https://trade.cashmakers.in/" target="_blank">', unsafe_allow_html=True)
    
    # angel broking logo banner
    angelone_logo = '/home/wasim/Music/pjt/python-trading-system-main/resources/angelone_logo.png'
    st.image(angelone_logo, caption='', use_column_width=True)

        
# Get historical data for tickers
    ticker_list = ["IDEA", "PATELENG", "CENTEXT"]
    ticker = st.selectbox("Select Ticker", ticker_list)
    candle_data = hist_data([ticker], 5, "FIVE_MINUTE", instrument_list)

    # Calculate RSI values for the historical data
    RSI(candle_data)

    # Display the RSI values
    st.write(f"RSI values for {ticker}:")
    st.write(candle_data[ticker])
    st.line_chart(candle_data[ticker]) 


def display_documentation():
    st.markdown(documentation.doc)



def display_stocks():
    # Create dropdown for stock selection
    st.subheader("Select a stock")
    stock_choice = st.selectbox("", ["IDEA", "Century Extrusions Ltd", "Patel Engineering Ltd"])

    # candlesticks table 
    st.subheader("Candlesticks Table")
    if stock_choice == "IDEA":
            tickers = ["IDEA"]
            duration = 50
            interval = "ONE_HOUR"
            exchange = "NSE"
            instrument_url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
            response = urllib.request.urlopen(instrument_url)
            instrument_list = json.loads(response.read())

            # Call the hist_data function in token_lookup.py to get the historical data
            candle_data = token_lookup.hist_data(tickers, duration, interval, instrument_list, exchange)

            # Use the resulting dataframe to create visualizations in Streamlit
            for ticker, data in candle_data.items():
                st.write(ticker)
                st.dataframe(data)
                st.line_chart(data)

    elif stock_choice == "Century Extrusions Ltd":
            tickers = ["CENTEXT"]
            duration = 50
            interval = "ONE_HOUR"
            exchange = "NSE"
            instrument_url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
            response = urllib.request.urlopen(instrument_url)
            instrument_list = json.loads(response.read())

            # Call the hist_data function in token_lookup.py to get the historical data
            candle_data = token_lookup.hist_data(tickers, duration, interval, instrument_list, exchange)

            # Use the resulting dataframe to create visualizations in Streamlit
            for ticker, data in candle_data.items():
                st.write(ticker)
                st.dataframe(data)
                st.line_chart(data)

    elif stock_choice == "Patel Engineering Ltd":
            tickers = ["PATELENG"]
            duration = 50
            interval = "ONE_HOUR"
            exchange = "NSE"
            instrument_url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
            response = urllib.request.urlopen(instrument_url)
            instrument_list = json.loads(response.read())

            # Call the hist_data function in token_lookup.py to get the historical data
            candle_data = token_lookup.hist_data(tickers, duration, interval, instrument_list, exchange)

            # Use the resulting dataframe to create visualizations in Streamlit
            for ticker, data in candle_data.items():
                st.write(ticker)
                st.dataframe(data)
                st.line_chart(data)


    # Get data for the selected stock
    if stock_choice == "IDEA":
        stock_ticker = "VOD.BO"
    elif stock_choice == "Century Extrusions Ltd":
        stock_ticker = "CENTEXT.BO"
    elif stock_choice == "Patel Engineering Ltd":
        stock_ticker = "PATELENG.BO"

    stock_data = yf.Ticker(stock_ticker).history(period='1d')
    stock_chart = go.Figure(data=go.Candlestick(x=stock_data.index, open=stock_data['Open'], high=stock_data['High'], low=stock_data['Low'], close=stock_data['Close']))
    st.plotly_chart(stock_chart)

    # Get news for the selected stock
    news = newsapi.get_everything(q=stock_choice, language='en', sort_by='relevancy')
    if news['totalResults'] > 0:
        st.subheader("Latest news about " + stock_choice)
        for article in news['articles'][:3]:
            st.write("- " + article['title'])
            st.write(article['description'])
            st.write(article['url'])
    else:
        st.write("No news found")

    # Create buttons to buy and sell the selected stock
    st.subheader("Trade " + stock_choice)
    if stock_choice == "IDEA":
        buy_button = st.button("Buy")
        sell_button = st.button("Sell")
        buy_path = "/home/wasim/Music/pjt/python-trading-system-main/stocks/buy_IDEA.py"
        sell_path = "/home/wasim/Music/pjt/python-trading-system-main/stocks/sell_IDEA.py"

         # Handle buy button click
        if buy_button:
                st.write("Buying IDEA stock...")
                result = subprocess.run(["/usr/bin/python3", buy_path], capture_output=True, text=True)
                if result.returncode == 0:
                    order_id = result.stdout.strip()
                    st.success("Order placed successfully. Order ID: {}".format(order_id))
                else:
                    st.error("Failed to place the order.")

        # Handle sell button click
        if sell_button:
            st.write("Selling IDEA stock...")
            result = subprocess.run(["/usr/bin/python3", sell_path], capture_output=True, text=True)
            if result.returncode == 0:
                order_id = result.stdout.strip()
                st.success("Order placed successfully. Order ID: {}".format(order_id))
            else:
                st.error("Failed to place the order.")


    elif stock_choice == "Century Extrusions Ltd":
        buy_button = st.button("Buy Century Extrusions Ltd")
        sell_button = st.button("Sell Century Extrusions Ltd")
        buy_path = "/home/wasim/Music/pjt/python-trading-system-main/stocks/buy_CENTEXT.py"
        sell_path = "/home/wasim/Music/pjt/python-trading-system-main/stocks/sell_CENTEXT.py"

         # Handle buy button click
        if buy_button:
                st.write("Buying Century Extrusions Ltd stock...")
                result = subprocess.run(["/usr/bin/python3", buy_path], capture_output=True, text=True)
                if result.returncode == 0:
                    order_id = result.stdout.strip()
                    st.success("Order placed successfully. Order ID: {}".format(order_id))
                else:
                    st.error("Failed to place the order.")

        # Handle sell button click
        if sell_button:
            st.write("Selling Century Extrusions Ltd stock...")
            result = subprocess.run(["/usr/bin/python3", sell_path], capture_output=True, text=True)
            if result.returncode == 0:
                order_id = result.stdout.strip()
                st.success("Order placed successfully. Order ID: {}".format(order_id))
            else:
                st.error("Failed to place the order.")


    elif stock_choice == "Patel Engineering Ltd":
        buy_button = st.button("Buy Patel Engineering Ltd")
        sell_button = st.button("Sell Patel Engineering Ltd")
        buy_path = "/home/wasim/Music/pjt/python-trading-system-main/stocks/buy_PATELENG.py"
        sell_path = "/home/wasim/Music/pjt/python-trading-system-main/stocks/sell_PATELENG.py"

         # Handle buy button click
        if buy_button:
                st.write("Buying Patel Engineering Ltd stock...")
                result = subprocess.run(["/usr/bin/python3", buy_path], capture_output=True, text=True)
                if result.returncode == 0:
                    order_id = result.stdout.strip()
                    st.success("Order placed successfully. Order ID: {}".format(order_id))
                else:
                    st.error("Failed to place the order.")

        # Handle sell button click
        if sell_button:
            st.write("Selling Patel Engineering Ltd stock...")
            result = subprocess.run(["/usr/bin/python3", sell_path], capture_output=True, text=True)
            if result.returncode == 0:
                order_id = result.stdout.strip()
                st.success("Order placed successfully. Order ID: {}".format(order_id))
            else:
                st.error("Failed to place the order.")


       # Execute the corresponding buy or sell program
    if buy_button:
        subprocess.run(['/usr/bin/python3', buy_path])
    elif sell_button:
        subprocess.run(['/usr/bin/python3', sell_path])

    # Create buttons to GTT ORDER PLCE and MOD&CANCELL the selected stock
    st.subheader("GTT ORDER " + stock_choice)
    if stock_choice == "IDEA":
        place_button = st.button("Place")
        cancel_button = st.button("Cancel")
        place_path = "/home/wasim/Music/pjt/python-trading-system-main/GTT_orders/IDEA_place.py"
        cancel_path= "/home/wasim/Music/pjt/python-trading-system-main/GTT_orders/IDEA_mod_cancel.py"

        # Handle GTT ORDER PLACE button click
        if place_button:
            st.write("Placing GTT ORDER for IDEA stock...")
            result = subprocess.run(["/usr/bin/python3", place_path], capture_output=True, text=True)
            if result.returncode == 0:
                order_id = result.stdout.strip()
                st.success("GTT ORDER placed successfully. Order ID: {}".format(order_id))
            else:
                st.error("Failed to place the GTT ORDER.")

        # Handle GTT ORDER CANCEL button click
        if cancel_button:
            st.write("Canceling GTT ORDER for IDEA stock...")
            result = subprocess.run(["/usr/bin/python3", cancel_path], capture_output=True, text=True)
            if result.returncode == 0:
                st.success("GTT ORDER canceled successfully.")
            else:
                st.error("Failed to cancel the GTT ORDER.")


    elif stock_choice == "Century Extrusions Ltd":
        place_button = st.button("Place")
        cancel_button = st.button("Cancel")
        place_path = "/home/wasim/Music/pjt/python-trading-system-main/GTT_orders/CENTEXT_place.PY"
        cancel_path = "/home/wasim/Music/pjt/python-trading-system-main/GTT_orders/CENTEXT_mod_cancel.PY"


        # Handle GTT ORDER PLACE button click
        if place_button:
            st.write("Placing GTT ORDER for Century Extrusions Ltd stock...")
            result = subprocess.run(["/usr/bin/python3", place_path], capture_output=True, text=True)
            if result.returncode == 0:
                order_id = result.stdout.strip()
                st.success("GTT ORDER placed successfully. Order ID: {}".format(order_id))
            else:
                st.error("Failed to place the GTT ORDER.")

        # Handle GTT ORDER CANCEL button click
        if cancel_button:
            st.write("Canceling GTT ORDER for Century Extrusions Ltd stock...")
            result = subprocess.run(["/usr/bin/python3", cancel_path], capture_output=True, text=True)
            if result.returncode == 0:
                st.success("GTT ORDER canceled successfully.")
            else:
                st.error("Failed to cancel the GTT ORDER.")


    elif stock_choice == "Patel Engineering Ltd":
        place_button = st.button("Place")
        cancel_button = st.button("cancel")
        place_path = "/home/wasim/Music/pjt/python-trading-system-main/GTT_orders/PATELENG_place.PY"
        cancel_path = "/home/wasim/Music/pjt/python-trading-system-main/GTT_orders/PATENENG_mod_cancel.PY"

        # Handle GTT ORDER PLACE button click
        if place_button:
            st.write("Placing GTT ORDER for Patel Engineering Ltd stock...")
            result = subprocess.run(["/usr/bin/python3", place_path], capture_output=True, text=True)
            if result.returncode == 0:
                order_id = result.stdout.strip()
                st.success("GTT ORDER placed successfully. Order ID: {}".format(order_id))
            else:
                st.error("Failed to place the GTT ORDER.")

        # Handle GTT ORDER CANCEL button click
        if cancel_button:
            st.write("Canceling GTT ORDER for Patel Engineering Ltd stock...")
            result = subprocess.run(["/usr/bin/python3", cancel_path], capture_output=True, text=True)
            if result.returncode == 0:
                st.success("GTT ORDER canceled successfully.")
            else:
                st.error("Failed to cancel the GTT ORDER.")


       # Execute the corresponding buy or sell program
    if place_button:
        subprocess.run(['/usr/bin/python3', place_path])
    elif cancel_button:
        subprocess.run(['/usr/bin/python3', cancel_path])

   
def display_copyrights():
    st.write(copyrights.cp)


def main():
    st.sidebar.title("Automated Trading System")

    if st.sidebar.button("Dashboard"):
        display_dashboard()
    if st.sidebar.button("Documentation"):
        display_documentation()
    if st.sidebar.button("Stocks"):
        display_stocks()
    if st.sidebar.button("Copyrights"):
        display_copyrights()

if __name__ == "__main__":
    main()