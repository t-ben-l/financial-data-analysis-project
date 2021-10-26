from f_functions import *
import sys

sys.path.insert(0, '/home/ben/Documents/proj.0.1/f_functions')
from f_functions import holder
import pandas as pd 
import plotly as py 
from plotly import tools
import plotly.graph_objs as go

df = pd.read_csv ('GBPCAD.csv')
df.columns = ['date','open','high','low','close','volume']
df.date = pd.to_datetime(df.date,format='%d.%m.%Y %H:%M:%S.%f')
df = df.set_index(df.date)
df= df[['open','high','low','close','volume']]
df = df.drop_duplicates (keep=False)
df = df.iloc[:200]
print (df.head())

ma = df.close.rolling (center = False, window = 30).mean()

#function calls

detrended = detrend (df,method = "difference")


#------------------


ben = holder()
HAresults = ben.heikenashi (df,[1])
HA= HAresults.candles[1]
trace0 = go.Ohlc (x = df.index, open = df.open, high = df.high, low = df.low, close = df.close, name = 'currency quote')
#trace1 = go.Scatter (x= df.index, y = ma)
#trace2 = go.Bar (x=df.index, y= df.volume)
#trace2 = go.Scatter (x= df.index, y = detrended )

data = [trace0]

fig = tools.make_subplots(rows=2,cols=1,shared_xaxes = True)
fig.append_trace(trace0,1,1)
#fig.append_trace(trace1,1,1)
#fig.append_trace(trace2,2,1)
fig.update_layout(
    autosize=False,
    width=1000,
    height=1100,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    paper_bgcolor="black",
)


py.offline.plot(fig, filename = 'candles.html')
print 'hie there  '
