import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR



df = pd.read_csv ('mydoc.csv')

print(df.head(7))
days = 30
df ['pred_open'] = df[['open']].shift(-days)
#df ['pred_high'] = df[['High']].shift(-days)
#df ['pred_high'] = df[['High']].shift(-days)
#df ['pred_low'] = df[['Low']].shift(-days)
#df ['pred_close'] = df[['Close']].shift(-days)
#df ['pred_volume'] = df[['Volume']].shift(-days)

#print(df.tail(7))

x = np.array(df.drop(['pred_open'],1))

x = x[:len(df)-days]

print(x)

y = np.array(df['pred_open'])

#get all values leavin the last n rows

x = y [:-days]

print(y)

#train 80% data and test 20%
x_tr,x_test,y_tr,y_test = train_test_split(x,y, test_size = 0.2)

#set the prediction days array equal to the last  30 rows from original data 

pred_days_arr = np.array(df.drop(['pred_open'],1))[-days:]

print (pred_days_arr)

#train the support vector machine (regression) using radial bases function

svr_rbf = SVR(kernel='rbf', C=1e3,gamma=0.00001)


