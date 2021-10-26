import pandas as pd
import numpy as np 
import scipy
from scipy import stats 
from scipy.optimize import OptimizeWarning
import warnings
import math 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression 
#from matplotlib.finance import candlestick
from mpl_finance import candlestick_ohlc
from matplotlib.dates import date2num
from datetime import datetime 

class holder:

    #heik ashi candles
    def heikenashi (self, prices,periods):

        results = holder()

        dict = {}

        HAclose = prices [['open','high','close', 'low']].sum(axis=1)/4

        HAopen = HAclose.copy()

        HAopen.iloc[0] = HAclose.iloc[0]

        HAhigh = HAclose.copy()

        HAlow = HAclose.copy() 

        for i in range (1,len(prices)):

            HAopen.iloc[i] =  (HAopen.iloc[i-1] + HAclose.iloc[i-1]) / 2 
            HAhigh.iloc[i] = np.array([prices.high.iloc[i],HAopen.iloc[i],HAclose.iloc[i]]).max()


            HAhigh.iloc[i] = np.array([prices.low.iloc[i],HAopen.iloc[i],HAclose.iloc[i]]).min()


        df = pd.concat((HAopen,HAhigh,HAlow,HAclose),axis=1)
        df.columns = [['open','high','close','low']]

        #df.index = df.index.droplevel(0)

        dict [periods[0]]= df

        results.candles = dict

        return results


#detrending

def detrend (prices, method = "difference"):

    if method == "difference":
        detrended = prices.close [1:] - prices.close[:-1].values
    
    elif method == "linear":

        x = np.arange (0,len(prices))
        y = prices.close.values 
        model = LinearRegression()
        mode.fit(x.reshape(-1,1),y.reshape(-1,1))

        trend = model.predict (x.reshape(-1,1))

        trend = trend.reshape ((len(prices),))

        detrended = prices.close - trend 

    else:

        print ("invalid option for detrending")

    return detrended 