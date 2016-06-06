from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)
  # app.run(host='0.0.0.0')
  
  import cgi
  form = cgi.FieldStorage()
  ticker_input = form.getvalue('ticker')
  
import pandas as pd
import numpy as np
import simplejson as json
import requests
from bokeh.plotting import figure, output_file, show
from datetime import datetime, timedelta
# ticker_input = raw_input('Please enter a stock ticker code (e.g., AAPL): ')
quandl_url = 'https://www.quandl.com/api/v3/datasets/WIKI/'
api_key = '_Dvc2yU_qTfyYtTzsqFd'
csv_ext = '.csv'
json_ext = '.json'
input_url = quandl_url + ticker_input + json_ext
input_csv = quandl_url + ticker_input + csv_ext

r = requests.get(input_url)

data = json.loads(r.text)
pd_data = pd.read_csv(input_csv,parse_dates=['Date'])
x = data["dataset"]["data"]
data_rows = len(x)
data_rows_good = np.zeros(data_rows)
start_date = datetime.now().date() + timedelta(-30)

booleans = []
for date_row in range(0,len(pd_data.Date)):
    # ticker_date = datetime.strptime(pd_data.Date[date_row],'%Y-%m-%d').date()
    ticker_date = pd_data.Date[date_row].date()
    if start_date < ticker_date:
        booleans.append(True)
    else:
        booleans.append(False)

closing_price = pd_data.Close[booleans]

output_file("datetime.html")

# create a new plot with a datetime axis type
p = figure(width=500, height=500, x_axis_type="datetime")

p.line(pd_data.Date[booleans], pd_data.Close[booleans], color='red', alpha=0.5)
