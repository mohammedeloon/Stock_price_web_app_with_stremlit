import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
#  Stock Price App

shown are the stocks ***closing price*** and volume of Google:

""")

tickerSymbols = 'GOOGL'
tickerData = yf.Ticker(tickerSymbols)
tickerDf = tickerData.history(period='1d' , start='2010-5-31' , end='2023-3-21')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.table(tickerDf.head(10))




#%%
