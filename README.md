# Finance_PlayGround

This is an application developed by [Peker Çelik](https://www.linkedin.com/in/pekercelik/) that enables you to backtest or develop financial strategies. 
The application is built with streamlit and yfinance libraries, and it allows you to select the stocks you would like to inspect from a pre-defined list of stocks.

## Features
* Selecting a stock from the list of pre-defined stocks.
* Inputting starting and ending dates for the stock data.
* Displaying stock price information with all the technical indicators.
* Plotting close prices.
* Implementing a basic strategy for buying and selling stocks based on a selected technical indicator and upper/lower thresholds.
* Showing the transactions made and the final amount of money.

## Technical Requirements
* Python 3.6 or higher
* streamlit
* yfinance
* ta
* matplotlib
* pandas
* numpy

## Installation
To install the required libraries, use the following pip command in your terminal:

```bash
pip install streamlit yfinance ta matplotlib pandas numpy
```

## Usage
1. Clone the repository to your local machine using the following command in your terminal:
```bash
git clone https://github.com/nebipeker/finance_playground.git
```

2. Navigate to the project directory using the following command in your terminal:

```bash
cd finance_playground
```
3. Run the application using the following command in your terminal:

```bash
streamlit run main.py
```

4. Use the application in your web browser.

## Future Improvements
* Adding more pre-defined stocks to the list.
* Implementing different financial strategies.
* Improving the interface and the design of the application.
* Providing more customization options for the technical indicators and thresholds.



