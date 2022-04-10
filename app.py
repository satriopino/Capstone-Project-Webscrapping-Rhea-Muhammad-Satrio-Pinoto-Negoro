from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup
import requests

# don't change this
matplotlib.use('Agg')
app = Flask(__name__)  # do not change this

# insert the scrapping here
url_get = requests.get(
    'https://www.coingecko.com/en/coins/ethereum/historical_data/usd?start_date=2020-01-01&end_date=2021-06-30#panel')
soup = BeautifulSoup(url_get.content, "html.parser")

# find your right key here
table = soup.find(
    'table', attrs={'class': 'table table-striped text-sm text-lg-normal'})
row = table.find_all('td', attrs={'class': 'text-center'})
row1 = table.find_all('td', attrs={'class': 'text-center'})

row_length = len(row)
row_length1 = len(row1)

temp = []  # initiating a list

n = 0
for i in range(0, row_length):
    # insert the scrapping process here
    while n < row_length1:
        # get period
        period = table.find_all(
            'th', attrs={'class': 'font-semibold text-center'})[i].text
        i += 1

        # get market cap
        market_cap = table.find_all(
            'td', attrs={'class': 'text-center'})[n].text
        market_cap = market_cap.strip()  # to remove excess white space
        n += 1

        # get volume
        volume = table.find_all('td', attrs={'class': 'text-center'})[n].text
        volume = volume.strip()  # to remove excess white space
        n += 1

        # get Open
        open_price = table.find_all(
            'td', attrs={'class': 'text-center'})[n].text
        open_price = open_price.strip()  # to remove excess white space
        n += 1

        # get close
        close_price = table.find_all(
            'td', attrs={'class': 'text-center'})[n].text
        close_price = close_price.strip()  # to remove excess white space
        n += 1

        temp.append((period, market_cap, volume, open_price, close_price))

temp = temp[::-1]

# change into dataframe
data = pd.DataFrame(temp, columns=(
    'Date', 'Market_Cap', 'Volume', 'Open', 'Close'))

# insert data wrangling here
data['Close'] = data['Close'].str.replace("$", "")
data['Open'] = data['Open'].str.replace("$", "")
data['Volume'] = data['Volume'].str.replace("$", "")
data['Market_Cap'] = data['Market_Cap'].str.replace("$", "")

data['Close'] = data['Close'].str.replace(",", "")
data['Open'] = data['Open'].str.replace(",", "")
data['Volume'] = data['Volume'].str.replace(",", "")
data['Market_Cap'] = data['Market_Cap'].str.replace(",", "")
data['Close'] = data['Close'].str.replace("N/A", "2279.35")

data['Close'] = data['Close'].astype('float64')
data['Open'] = data['Open'].astype('float64')
data['Volume'] = data['Volume'].astype('float64')
data['Market_Cap'] = data['Market_Cap'].astype('float64')
data['Date'] = data['Date'].astype('datetime64')


eth_volume = data.drop(columns=['Market_Cap', 'Open', 'Close'])
eth_volume1 = eth_volume.set_index('Date')

market_cap = data.drop(columns=['Volume', 'Open', 'Close'])
market_cap1 = market_cap.set_index('Date')
# end of data wranggling


@app.route("/")
def index():

    # be careful with the " and '
    card_data = f'{eth_volume1["Volume"].mean().round(2)}'

    # generate plot
    ax = eth_volume1.plot(figsize=(20, 9))

    # Rendering plot
    # Do not change this
    figfile = BytesIO()
    plt.savefig(figfile, format='png', transparent=True)
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    plot_result = str(figdata_png)[2:-1]

    # render to html
    return render_template('index.html',
                           card_data=card_data,
                           plot_result=plot_result
                           )

if __name__ == "__main__":
    app.run(debug=True)
