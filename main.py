# INF601 - Advanced Programming in Python
# David Bohorquez
# Mini Project 1

#Import the required modules:


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.dates as mdates

# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
# (10/10 points) Store this information in a list that you will convert to an array in NumPy.
# (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum, it just needs to show 10 data points.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this file with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

#Make list of tickers and empty dictionaries.
travel_stocks = ["MAR","HLT","RCL","LUV","UBER"]
travel_close = {}
stock_date = {}

# Make the folder called "charts".
os.makedirs(name="charts/", exist_ok=True)

# For each ticker, pull information from the last 10 trading days. Also pull dates from the index.
for ticker in travel_stocks:
    stock_info = yf.Ticker(ticker)
    stock_history = stock_info.history(period="10d")
    stock_date[ticker] = stock_history.index
    travel_close[ticker] = []

    '''
    Since stock_history is a dataframe, we specifically need the close price so we pull data 
    from that column and append it. Finally, we make an array for the closing price.
    '''

    for price in stock_history["Close"]:
        travel_close[ticker].append(price)
    numpy_close_price = np.array(travel_close[ticker])

    ''' 
    This command  makes the array with date but nullifies the time in the numpy array
    leaving only the date. Good for tick alignment.
    '''
    numpy_stock_date = np.array(stock_date[ticker], dtype='datetime64[D]')

    # Using ax makes it easier to format ticks and axes compared to traditional plt commands.
    fig, ax = plt.subplots()

    # This line adds dots(o) and a dotted line(linestyle). Does not clip first or last data point.
    ax.plot(numpy_stock_date,numpy_close_price, 'o', color='black', markersize=4, linestyle='dotted',clip_on=False)
    ax.set_ylabel('Closing Price')
    ax.set_xlabel('Date')
    ax.title.set_text('Closing Price Over the Last 10 Trading Days (' + ticker + ')')


    # Put dollar signs before the y-axis. Put 2 decimal places as well.
    ax.yaxis.set_major_formatter('${x:1.2f}')

    # Set x-axis ticks to show as abbreviated month (%b) and two-digit day(%d).
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

    # Hide the right and top bars in the graph. Makes the graph look better.
    ax.spines[['top', 'right']].set_visible(False)

    # Create 1 tick per day.
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))

    # Set boundaries for x and y for aesthetics. +1 added as a buffer for the title.
    ax.set_xlim(min(numpy_stock_date), max(numpy_stock_date))
    ax.set_ylim(min(numpy_close_price), max(numpy_close_price)+1)

    # Make the tick labels vertical.
    ax.tick_params(axis='x', rotation=90, labelrotation=90, size=3)

    # Leaves more space at the bottom of the figure.
    fig.tight_layout()

    #Finally, save the figure in the 'charts' folder.
    ax.get_figure().savefig("charts/" + ticker + ".png")
