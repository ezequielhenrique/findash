from datetime import datetime, timedelta
from data_processors.stock_processor import StockProcessor
from data_processors.ticker_processor import TickerProcessor, id_to_ticker
from data_processors.number_processor import format_num
import streamlit as st


st.set_page_config(page_title='FinDash', page_icon=':chart_with_upwards_trend:', layout='wide')

st.title('FinDash')
st.header('Análise de ações')

tickers = TickerProcessor('assets/csv/acoes_listadas_b3_completo.csv')

stock_select = st.selectbox('Selecione a empresa', tickers.get_tickers_id())

end_date = datetime.today()
start_date = end_date - timedelta(days=5*365)

ticker = None
stock_data = None

if stock_select:
    ticker = id_to_ticker(stock_select, sa=False)
    stock_data = StockProcessor(ticker)
    stock_data.set_stock_data(period='1d', start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))

header = st.container(border=True)
header.subheader(tickers.get_razao_social(id_to_ticker(stock_select, sa=False)), divider='blue')
col1, col2, col3, col4 = header.columns(4)
col1.image(f'https://raw.githubusercontent.com/thefintz/icones-b3/main/icones/{id_to_ticker(stock_select, sa=False)}.png', width=80)
col2.metric(label='Valor atual', value=f'R$ {stock_data.get_last_price():.2f}', delta=f'{stock_data.get_daily_variation():.1f}%')
col3.metric(label='Setor de Atuação', value=tickers.get_setor_atuacao(id_to_ticker(stock_select, sa=False)))
col4.metric(label='Segmento', value=tickers.get_segmento(id_to_ticker(stock_select, sa=False)))

section1 = st.container()
col1, col2 = section1.columns([3, 1])

# subcontainer = col1.container(border=True)
# subcontainer.subheader(f'Cotação do {id_to_ticker(stock_select, sa=False)} - Últimos 5 anos')
# subcontainer.line_chart(stock_data.get_closes_prices(), x_label='Data', y_label='Preço (R$)')
# subcontainer.subheader(f'Volume do {id_to_ticker(stock_select, sa=False)} - Últimos 5 anos')
# subcontainer.bar_chart(stock_data.get_volume(), color='#FF6400')

subcontainer = col1.container(border=True)
tab1, tab2, tab3 = subcontainer.tabs(['5 anos', '3 meses', '1 mês'])

with tab1:
    st.subheader(f'Cotação do {id_to_ticker(stock_select, sa=False)} - Últimos 5 anos')
    st.line_chart(stock_data.get_closes_prices(), x_label='Data', y_label='Preço (R$)')
    st.subheader(f'Volume do {id_to_ticker(stock_select, sa=False)} - Últimos 5 anos')
    st.bar_chart(stock_data.get_volume(), color='#FF6400')

with tab2:
    stock_data = StockProcessor(ticker)
    start_date = end_date - timedelta(days=90)
    stock_data.set_stock_data(period='1d', start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    st.subheader(f'Cotação do {id_to_ticker(stock_select, sa=False)} - Últimos 3 meses')
    st.line_chart(stock_data.get_closes_prices(), x_label='Data', y_label='Preço (R$)')
    st.subheader(f'Volume do {id_to_ticker(stock_select, sa=False)} - Últimos 3 meses')
    st.bar_chart(stock_data.get_volume(), color='#FF6400')

with tab3:
    stock_data = StockProcessor(ticker)
    start_date = end_date - timedelta(days=30)
    stock_data.set_stock_data(period='1d', start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    st.subheader(f'Cotação do {id_to_ticker(stock_select, sa=False)} - Últimos mês')
    st.line_chart(stock_data.get_closes_prices(), x_label='Data', y_label='Preço (R$)')
    st.subheader(f'Volume do {id_to_ticker(stock_select, sa=False)} -Últimos mês')
    st.bar_chart(stock_data.get_volume(), color='#FF6400')

subcontainer = col2.container(border=True)
subcontainer.subheader('Dados Financeiros')
a, b = subcontainer.columns(2)
a.metric(label='Captalização de Mercado', value=f'R$ {format_num(stock_data.get_market_cap())}')
b.metric(label='Volume Médio', value=f'R$ {format_num(stock_data.get_average_volume())}')
a, b = subcontainer.columns(2)
a.metric(label='P/L', value=stock_data.get_pl())
b.metric(label='P/VP', value=stock_data.get_pvp())
a, b = subcontainer.columns(2)
a.metric(label='DY', value=stock_data.get_dy())
b.metric(label='ROI', value=stock_data.get_roe())
a, b = subcontainer.columns(2)
a.metric(label='Min. 52 Semanas', value=f'R$ {stock_data.get_min_52_sem():.2f}')
b.metric(label='Máx. 52 Semanas', value=f'R$ {stock_data.get_max_52_sem():.2f}')

subcontainer = col2.container(border=True)
subcontainer.subheader('Indicadores Técnicos')
a, b = subcontainer.columns(2)
a.metric(label='RSI 14', value='50')
b.metric(label='MACD 21', value='10')
a, b = subcontainer.columns(2)
a.metric(label='MA 9 dias', value='R$ 150,00')
b.metric(label='MA 21 dias', value='R$ 90,00')
a, b = subcontainer.columns(2)
a.metric(label='MA 50 dias', value='R$ 150,00')
b.metric(label='MA 100 dias', value='R$ 90,00')

# st.dataframe(stock_data.get_stock_prices())
# st.dataframe(stock_data.get_info())

st.markdown('Fonte dos dados: **Yahoo Finance API**, **Fundamentus api**')
