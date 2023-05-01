import yfinance as yf
import streamlit as st
from datetime import datetime

st.write("""
#  Stock Price App

shown are the stocks ***closing price*** and volume of Google:

""")

tickerSymbols = 'GOOGL'
tickerData = yf.Ticker(tickerSymbols)
tickerDf = tickerData.history(period='1d' , start='2010-1-1', end=datetime.today().strftime('%Y-%m-%d'))
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.table(tickerDf.drop(['Dividends' , 'Stock Splits'], axis=1).copy().head(10))




#%%
