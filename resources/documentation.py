doc = """
# **Fully Automated AI Trading System**

## **Overview**

The Fully Automated AI Trading System is a comprehensive system for
automated stock trading. The system includes a number of programs and
components, including machine learning models, data processing
pipelines, trading algorithms, and more.

The system is designed to be fully automated, allowing traders to
execute trades without the need for human intervention. This helps to
reduce the risk of human error and enables traders to make trades more
quickly and efficiently.

### **Programs and Components**

The Fully Automated AI Trading System includes a number of programs and
components, including:

-   app.py: The main program that handles user interactions and executes
    > Web App

-   conn.py: A program that handles connections to various financial
    > data sources.

-   RSI.py: A program that calculates Relative Strength Index (RSI)
    > Strategy we have implied.

-   strategy_ema_macd.py: A program that implements a trading strategy
    > based on Exponential Moving Average (EMA) and Moving Average
    > Convergence Divergence (MACD) indicators. (Strategy)

-   token_lookup.py: A program that looks up stock tokens for various
    > exchanges.

-   strategy_robo_order.py: A program that handles the actual execution
    > of trades.

-   buy_CENTEXT.py, buy_IDEA.py, buy_PATELENG.py: Programs that handle
    > the buying of specific stocks.

-   GTT_orders: A folder that contains programs for placing
    > Good-Til-Trigger (GTT) orders.

-   resources: A folder that contains various resources, including
    > documentation and copyright information.

### **Package Installation:**
The program requires several packages to be installed, including streamlit, newsapi, yfinance, and plotly. You can install these packages using pip or conda command line tools. For example, to install streamlit using pip, run  
> To install Streamlit use the command

`pip install streamlit ` 

> To fetch news from this website 

`pip install newsapi `   

> Yfinance Data resources

`pip install yfinance`

>> To install all the requirements **run requirments.txt** as

`python -m pip install -r requirements.txt`
### **Package Imports:**
The program imports several Python packages/modules that are required for different functionalities, such as streamlit, newsapi, yfinance, plotly.graph_objs, datetime, subprocess, urllib, pandas, json, numpy, conn, RSI, hist_data, instrument_list, token_lookup, and documentation. Each of these packages has a specific purpose and functionality in the program.

### **Variables and Objects:**
Next, the program declares several variables and objects that are used to store data or perform calculations. For example, doc is a variable that stores a string containing the documentation text for the program. newsapi is an object that is used to interact with the News API and retrieve news articles. tickers is a list of stock tickers that the program uses to retrieve financial data.

### **Implementation**

The Fully Automated AI Trading System was implemented using a
combination of Python, various libraries and frameworks, and custom
code. Some of the key libraries and frameworks used in the system
include:

-   streamlit: A Python framework for building interactive web
    > applications.

-   newsapi: A Python library for accessing news articles and headlines.
    > To fetch latest news. (Feature)

-   yfinance: A Python library for accessing stock market data from
    > Yahoo Finance.

-   plotly: A Python library for creating interactive data
    > visualizations.

### **Challenges Faced**

During the implementation of the Fully Automated AI Trading System, a
number of challenges were faced. Some of the key challenges included:

-   Processing large amounts of data in real-time.

-   Training and optimizing machine learning models.

-   Ensuring the system is secure and robust against potential attacks.

### **Visual Aids**

To help explain the various programs and components within the Fully
Automated AI Trading System, visual aids such as screenshots and
diagrams can be included. These can help to make complex concepts easier
to understand.

### **Conclusion**

The Fully Automated AI Trading System is a powerful tool for automated
stock trading. By combining machine learning models, trading algorithms,
and real-time data processing, the system enables traders to execute
trades quickly and efficiently, with reduced risk of human error.


## **Additional details:**

The app.py program relies on several other programs and components to function, including conn.py, copyrights.py, RSI.py, strategy_ema_macd.py, token_lookup.py, strategy_robo_order.py, and buy/sell scripts in the stocks and GTT_orders folders.
The program is designed to be fully automated, but also allows for manual intervention if desired.
The program may incorporate multiple machine learning models and trading algorithms to generate trading signals and optimize returns.
The program may also include risk management strategies to minimize losses and maximize profits.
The program is designed to be scalable and adaptable, allowing for integration with new data sources, trading algorithms, and APIs as necessary.
"""

print(doc)