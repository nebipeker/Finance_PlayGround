from asyncio import selector_events
import yfinance as yf
import streamlit as st
import datetime
from ta import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.write("# Finance Playground by [Peker Çelik](https://github.com/nebipeker)")
    st.write("## This application enables you to backtest or develop strategy.")
    with open("file.txt", 'r') as f:
        stocks = [line.rstrip('\n') for line in f]

    selected_stock = st.selectbox(
     'Select the stocks that you would like to inspect. Some of them may not be aviable from yahoo finance API',stocks
     )

    st.write('You selected:', selected_stock)
    
    msft = yf.Ticker(selected_stock)
    st.write(" Please select starting and ending dates:")
    start = st.date_input("Starting day", datetime.date(2019, 7, 6))
    end = st.date_input("Ending day", datetime.date.today())
    tickerDf = msft.history(period ='1d', start=start,end=end)
    df = add_all_ta_features(tickerDf, open="Open", high="High", low="Low", close="Close", volume="Volume", fillna=True) 
    df.drop("Dividends",axis=1,inplace=True)
    df.drop("Stock Splits",axis=1,inplace=True)
    st.write("### Stock price informations with all the indicators")
    st.dataframe(df)
    st.write("### Close prices ploted below.")
    st.line_chart(df.Close)
    st.write(" Our basic strategy to buy or sell is choosing a indicator, then below and above the thresholds capture the signal as buy and sell.")
    selected_indicator = st.selectbox("Indicator selected", df.columns[5:])
    upper = st.number_input('The upper threshold')
    lower = st.number_input('The lower threshold')
    
    buy=[]
    sell=[]
    
    for i in range(df.shape[0]):
        if df[selected_indicator][i] > upper:
            sell.append(df["Close"][i])
            buy.append(np.nan)
        elif df[selected_indicator][i] < lower:
            buy.append(df["Close"][i])
            sell.append(np.nan)
        else:
            buy.append(np.nan)
            sell.append(np.nan)
    
    plt.figure(figsize=(15,6))
    plt.plot(df.Close.values)
    plt.plot(buy[0:],color='g', linestyle='None', marker='^')
    plt.plot(sell[0:],color='r', linestyle='None', marker='^')
    plt.legend(['Price', 'Buy Signal', 'Sell Signal'])
    st.pyplot(plt)

    money = 100
    stocks = 0
    stoploss=0
    for i in range(len(buy)):
        if money== 0 and df["Close"].iloc[i]< stoploss:
            money = (stocks * df["Close"].iloc[i]).round(2)
            st.write(stocks," amount of stock is sold with",money,"dollars","with the price of", df["Close"].iloc[i].round(2), "in order to stop loss.")
            stocks = 0
        if stocks== 0 and df["Close"].iloc[i]> stoploss:
            stocks = (money / df["Close"].iloc[i]).round(2)
            st.write(stocks," amount of stock is bought with",money,"dollars","with the price of", df["Close"].iloc[i].round(2), "in order to catch rising trend.")
            money = 0
        if not np.isnan(buy[i]) and money!=0:
            stocks = money/df["Close"].iloc[i]
            st.write(stocks," amount of stock is bought with",money,"dollars at the price of", df["Close"].iloc[i].round(2))
            stoploss = df["Close"].iloc[i] * 0.95
            money = 0
        elif not np.isnan(sell[i]) and stocks!=0 :
            money = (stocks * df["Close"].iloc[i]).round(2)
            st.write(stocks," amount of stock is sold with",money,"dollars", df["Close"].iloc[i].round(2))
            stocks = 0



if __name__=='__main__':
    main()
