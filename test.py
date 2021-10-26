import plotly.graph_objs as go


import pandas as pd
from datetime import datetime

df = pd.read_csv ('EURUSDhours.csv')
fig = go.Figure(data=[go.Candlestick(x=df['date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

fig.show()