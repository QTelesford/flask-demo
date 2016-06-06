from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index2.html')

if __name__ == '__main__':
  app.run(port=33507)
  # app.run(host='0.0.0.0')
  
  # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import simplejson as json
import requests
from bokeh.plotting import figure, output_file, show
# import urllib2
# import re
from datetime import datetime, timedelta
ticker_input = raw_input('Please enter a stock ticker code (e.g., AAPL): ')
quandl_url = 'https://www.quandl.com/api/v3/datasets/WIKI/'
api_key = '_Dvc2yU_qTfyYtTzsqFd'
csv_ext = '.csv'
json_ext = '.json'
input_url = quandl_url + ticker_input + json_ext
input_csv = quandl_url + ticker_input + csv_ext

# print input_url
r = requests.get(input_url)

data = json.loads(r.text)
pd_data = pd.read_csv(input_csv,parse_dates=['Date'])
x = data["dataset"]["data"]
data_rows = len(x)
data_rows_good = np.zeros(data_rows)
start_date = datetime.now().date() + timedelta(-30)

booleans = []
for date_row in range(0,len(pd_data.Date)):
    ticker_date = datetime.strptime(pd_data.Date[date_row],'%Y-%m-%d').date()
    if start_date < ticker_date:
        booleans.append(True)
    else:
        booleans.append(False)

# data_current = pd.Series(booleans)
closing_price = pd_data.Close[booleans]

"""
for ii in range(0,data_rows):
    ticker_date = datetime.strptime(x[ii][0],'%Y-%m-%d').date()
    
    if start_date < ticker_date:
        data_rows_good[ii] = 1
        
closing_price = np.zeros(sum(data_rows_good))
closing_len = len(closing_price)
for jj in range(0,closing_len):
    ticker_closing = x[jj][4]
    closing_price[jj] = ticker_closing
"""
'''
output_file("line.html")

p = figure(plot_width=400, plot_height=400)

# add a line renderer
p.line(closing_price, line_width=2)

show(p)
'''
'''
figTitle = "Closing Price: " + ticker_input
plt.plot(closing_price)
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title(figTitle)
plt.grid(True)
'''

output_file("datetime.html")

# create a new plot with a datetime axis type
p = figure(width=500, height=500, x_axis_type="datetime")

p.line(pd_data.Date[booleans], pd_data.Close[booleans], color='red', alpha=0.5)

show(p)

# p = figure(width=400, height=400, x_axis_label='Date')
# p.xaxis.axis_label = 'New xlabel'
""" Column Names

data["dataset"]["column_names"][0]
Out[134]: u'Date'

data["dataset"]["column_names"][1]
Out[135]: u'Open'

data["dataset"]["column_names"][2]
Out[136]: u'High'

data["dataset"]["column_names"][3]
Out[137]: u'Low'

data["dataset"]["column_names"][4]
Out[138]: u'Close'

data["dataset"]["column_names"][5]
Out[139]: u'Volume'

data["dataset"]["column_names"][6]
Out[140]: u'Ex-Dividend'

data["dataset"]["column_names"][7]
Out[141]: u'Split Ratio'

data["dataset"]["column_names"][8]
Out[142]: u'Adj. Open'

data["dataset"]["column_names"][9]
Out[143]: u'Adj. High'

data["dataset"]["column_names"][10]
Out[144]: u'Adj. Low'

data["dataset"]["column_names"][11]
Out[145]: u'Adj. Close'

data["dataset"]["column_names"][12]
Out[146]: u'Adj. Volume'



# date_year = datetime.strptime(x[ii][0],'%Y-%m-%d').year
# date_month = datetime.strptime(x[ii][0],'%Y-%m-%d').month
# opener = urllib2.build_opener()
# f = opener.open(req)
# jason = json.load(f)

# for item in json:
    # print item.get('end_date')
# htmltext = urllib.urlopen(input_url)
# data = json.load(htmltext)
# r = requests.get(input_url)

# payload = {'some':'data'}
# r = requests.post(input_url,data=json.dumps(payload))

# with open(r) as f:
#    data = f.read()
#     jsondata = json.loads(data)

# nprint jsondata
# A = ([[1.,2.,'3.],[4.,5.,6.],[7.,8.,9.]])

# B = ([[2.,4.,6.],[3.,6.,9.],[4.,8.,12.]])

# print np.ndarray.ndim(A)
"""
