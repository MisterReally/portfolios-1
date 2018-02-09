# Write a class that holds a single security
# Content:
#  + Raw data (date, closing price, volume)
#  - Dividends
#  - Splits
#  + Ticker symbol
#  + Name 
#  - Description
#
# Methods:
#  + Current price
#  - Price at date
#  - Difference in prices
#  + Min / Max price
#  - Runrate
#  - Rolling weighted average
#  - Volatility
#  - Predictions (like runrate, RWA, autoregressive model)

from etfs.io.helpers import read_yahoo_csv, retrieve_yahoo_quote


class security(object):

    def __init__(self, name, start='1900-01-01', end='2100-01-01'):
        self.ticker = name
        self.load(start=start, end=end)
        self.get_last_price()
        self.get_max_price()
        self.get_min_price()
        self.get_median_price()
        self.get_mean_price()
        self.get_std_price()

    def set_name(self, name):
        self.name = name

    def load(self, start='1900-01-01', end='2100-01-01'):
        '''
        Tries to load from csv first, then pulls from Yahoo!
        '''
        try:
            filepath = '../data/{0}.csv'.format(self.ticker)
            self.data = read_yahoo_csv(path=filepath, startdate=start, enddate=end)
        except:
            self.data = retrieve_yahoo_quote(ticker=self.ticker, startdate=start.replace('-', ''), enddate=end.replace('-', ''))
        else:
        	pass

    def get_last_price(self, column='Close'):
        self.last_price = self.data[column][-1]
        return self.last_price

    def get_max_price(self, column='Close'):
        self.max_price = self.data.Close.max()
        return self.max_price

    def get_min_price(self, column='Close'):
        self.min_price = self.data.Close.min()
        return self.min_price

    def get_median_price(self, column='Close'):
        self.median_price = self.data.Close.median()
        return self.median_price

    def get_mean_price(self, column='Close'):
        self.mean_price = self.data.Close.mean()
        return self.mean_price

    def get_std_price(self, column='Close'):
        self.std_price = self.data.Close.std()
        return self.std_price