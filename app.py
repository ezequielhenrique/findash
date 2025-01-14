from datetime import datetime, timedelta
from data_processors.stock_processor import StockProcessor
from data_processors.ticker_processor import TickerProcessor, id_to_ticker
import streamlit as st


st.set_page_config(page_title='FinDash', page_icon=':chart_with_upwards_trend:', layout='wide')

st.title('FinDash')
st.subheader('Análise de ações')

tickers = TickerProcessor('assets/csv/acoes_listadas_b3_completo.csv')

stock_select = st.selectbox('Selecione a empresa', tickers.get_tickers_id())

end_date = datetime.today()
start_date = end_date - timedelta(days=5*365)

stock_data = None

if stock_select:
    ticker = id_to_ticker(stock_select)
    stock_data = StockProcessor(ticker)
    stock_data.set_stock_data(period='1d', start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))

st.image(f'https://raw.githubusercontent.com/thefintz/icones-b3/main/icones/{id_to_ticker(stock_select, sa=False)}.png')
st.subheader(tickers.get_razao_social(id_to_ticker(stock_select, sa=False)))
st.text(f'Setor de Atuação: {tickers.get_setor_atuacao(id_to_ticker(stock_select, sa=False))}')
st.text(f'Segmento: {tickers.get_segmento(id_to_ticker(stock_select, sa=False))}')
st.dataframe(stock_data.get_stock_prices())
st.line_chart(stock_data.get_closes_prices(), x_label='Data', y_label='Preço (R$)')
st.bar_chart(stock_data.get_volume(), color='#FF6400')
