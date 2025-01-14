from datetime import datetime, timedelta
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

st.set_page_config(layout='wide')

st.title('FinDash')

st.subheader('Análise de ações')

df_stocks = pd.read_csv('acoes_listadas_b3_completo.csv')

ticker_list = list(df_stocks['Ticker'])
names_list = list(df_stocks['Nome'])

tickers_id = list()

for i in range(len(ticker_list)):
    tickers_id.append(f'{ticker_list[i]} - {names_list[i]}')

stock_select = st.selectbox('Selecione a empresa', tickers_id)
end_date = datetime.today()
start_date = end_date - timedelta(days=5*365)

stock_data = None

if stock_select:
    ticker = stock_select.split()[0] + '.SA'
    stock_df = yf.Ticker(ticker)
    stock_data = stock_df.history(period='1d', start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))

stock_info = df_stocks[df_stocks['Ticker'] == stock_select.split()[0]]

st.image(f'https://raw.githubusercontent.com/thefintz/icones-b3/main/icones/{stock_select.split()[0]}.png')
st.subheader(stock_info['Razão Social'].to_string(index=False))
st.text(f'Setor de Atuação: {stock_info['Setor de Atuação'].to_string(index=False)}')
st.text(f'Segmento: {stock_info['Segmento'].to_string(index=False)}')

st.dataframe(stock_data)

st.line_chart(stock_data.Close, x_label='Preço (R$)', y_label='Data')
st.bar_chart(stock_data.Volume, color='#FF6400')
