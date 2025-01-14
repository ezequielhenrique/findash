import pandas as pd


def id_to_ticker(ticker_id, sa=True):
    if sa:
        return ticker_id.split()[0] + '.SA'
    else:
        return ticker_id.split()[0]


class TickerProcessor:
    def __init__(self, csv_path):
        self.df_tickers = pd.read_csv(csv_path)

    def get_ticker_list(self):
        return list(self.df_tickers['Ticker'])

    def get_names_list(self):
        return list(self.df_tickers['Nome'])

    def get_tickers_id(self):
        tickers_id = list()
        ticker_list = self.get_ticker_list()
        names_list = self.get_names_list()

        for i in range(len(ticker_list)):
            tickers_id.append(f'{ticker_list[i]} - {names_list[i]}')

        return tickers_id

    def get_nome(self, ticker):
        df_row = self.df_tickers[self.df_tickers['Ticker'] == ticker]
        return df_row['Nome'].to_string(index=False)

    def get_razao_social(self, ticker):
        df_row = self.df_tickers[self.df_tickers['Ticker'] == ticker]
        return df_row['Razão Social'].to_string(index=False)

    def get_setor_atuacao(self, ticker):
        df_row = self.df_tickers[self.df_tickers['Ticker'] == ticker]
        return df_row['Setor de Atuação'].to_string(index=False)

    def get_segmento(self, ticker):
        df_row = self.df_tickers[self.df_tickers['Ticker'] == ticker]
        return df_row['Segmento'].to_string(index=False)
