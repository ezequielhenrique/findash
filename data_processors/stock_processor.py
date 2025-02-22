import yfinance as yf
import fundamentus


class StockProcessor:
    def __init__(self, ticker):
        self.ticker = ticker
        self.stock_data = yf.Ticker(ticker + '.SA')
        self.stock_prices = None
        self.fundamental_data = fundamentus.get_papel(ticker)

    def set_stock_data(self, period, start, end):
        self.stock_prices = self.stock_data.history(period=period, start=start, end=end)

    def get_stock_prices(self):
        return self.stock_prices

    def get_closes_prices(self):
        return self.stock_prices.Close

    def get_volume(self):
        return self.stock_prices.Volume

    def get_last_price(self):
        return self.get_closes_prices().iloc[-1]

    def get_daily_variation(self):
        today_price = self.get_last_price()
        yesterday_price = self.get_closes_prices().iloc[-2]
        variation = ((today_price / yesterday_price) - 1) * 100
        return variation

    def get_info(self):
        return self.stock_data.info

    def get_market_cap(self):
        return self.stock_data.info['marketCap']

    def get_average_volume(self):
        return self.stock_data.info['averageVolume']

    def get_pl(self):
        return float(self.fundamental_data['PL'][0]) / 100

    def get_pvp(self):
        return float(self.fundamental_data['PVP'][0]) / 100

    def get_dy(self):
        return self.fundamental_data['Div_Yield'][0]

    def get_roe(self):
        return self.fundamental_data['ROE'][0]

    def get_max_52_sem(self):
        return float(self.fundamental_data['Max_52_sem'][0])

    def get_min_52_sem(self):
        return float(self.fundamental_data['Min_52_sem'][0])
