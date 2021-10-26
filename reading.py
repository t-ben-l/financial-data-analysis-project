import csv 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR




from f_functions import *
import sys

sys.path.insert(0, '/home/ben/Documents/proj.0.1/f_functions')
from f_functions import holder
import pandas as pd 
import plotly as py 
from plotly import tools
import plotly.graph_objs as go



r = open ('GBPCAD.csv','r')

reader = csv.reader(r)

openn = []
currency = ['open','high']

for row in reader:
    openn.append(row)

pred_open = []
pred_high = []
pred_low = []
pred_close =[]

new_vals = []

print ('list ')

for item in openn:
   pred_open.append(item[1])


for item in openn:
   pred_high.append(item[2])


for item in openn:
   pred_low.append(item[3])


for item in openn:
   pred_close.append(item[4])

   
for item in new_vals and pred_open and pred_high:
   new_vals[0].append(pred_open(item[1]))
   


for n in pred_high:
    print(n)
m = 0

with open ('mydoc.csv', mode = 'w' ) as f:
    fieldnames = ['index','open', 'high','low','close']
    thewriter = csv.DictWriter(f, fieldnames = fieldnames)

    thewriter.writeheader()

    for i in range (1,100):
        thewriter.writerow({'index': str(m), 'open' : str(pred_open), 'high' : str(pred_high), 'low' : str(pred_low), 'close' : str(pred_close)})
        m = m+1

print ('last value of open')
      

print(pred_open[-2:])

#plt.plot(pred_open[-50:])
#plt.show()


df = pd.read_csv ('GBPCAD.csv')
df.columns = ['date','open','high','low','close','volume']
df.date = pd.to_datetime(df.date,format='%d.%m.%Y %H:%M:%S.%f')
df = df.set_index(df.index)
df= df[['open','high','low','close','volume']]
df = df.drop_duplicates (keep=False)
df = df.iloc[:200]
print (df.head())

ma = df.close.rolling (center = False, window = 30).mean()


ben = holder()
HAresults = ben.heikenashi (df,[1])
HA= HAresults.candles[1]
trace0 = go.Ohlc (x = df.index, open = pred_open , high = pred_high, low = pred_low, close = pred_close, name = 'currency quote')
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



#--------------------------------------------------
