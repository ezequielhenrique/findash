import yfinance as yf


class StockProcessor:
    def __init__(self, ticker):
        self.ticker = ticker
        self.stock_data = yf.Ticker(ticker)
        self.stock_prices = None

    def set_stock_data(self, period, start, end):
        self.stock_prices = self.stock_data.history(period=period, start=start, end=end)

    def get_stock_prices(self):
        return self.stock_prices

    def get_closes_prices(self):
        return self.stock_prices.Close

    def get_volume(self):
        return self.stock_prices.Volume
