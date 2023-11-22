# Web-Scrapping using Beautifulsoup

Projek ini dikembangkan sebagai salah satu capstone project dari Algoritma Academy Data Analytics Specialization. Deliverables yang diharapkan dari projek ini adalah melakukan simple webscrapping untuk mendapatkan informasi. Untuk step by step guide, Bapak Ibu dipersilahkan untuk membuka git saya [Click here](https://github.com/t3981-h/Webscrapping-with-BeautifulSoup "Webscrapping with Beautiful Soup"). Kita juga akan memanfaatkan flask dashboard sederhana untuk menampilkan hasil scrap dan visualisasi kita.

## Dependencies

- beautifulSoup4
- pandas
- flask
- matplotlib

Atau Bapak Ibu cukup menginstall requirements.txt dengan cara berikut

```python
pip install -r requirements.txt
```

### The Final Mission

1. (Easy) Data Volume Penjualan Ethereum dari `https://www.coingecko.com/en/coins/ethereum/historical_data/usd?start_date=2020-01-01&end_date=2021-06-30#panel`

   * Dari halaman tersebut carilah `Date`, dan `Volume`.
   * Buat lah plot pergerakan volume perdagangan dari Ethereum. 

2. (Medium) Data kurs US Dollar ke rupiah dari `https://www.exchange-rates.org/history/IDR/USD/T`

    * Dari halaman tersebut carilah `harga harian`, dan `tanggal`
    * Bualah plot pergerakan kurs USD 
    
3. (Hard) Data film yang rilis di tahun 2021 dari `https://www.imdb.com/search/title/?release_date=2021-01-01,2021-12-31`

    * Dari Halaman tersebut carilah `judul` , `imdb rating` , `metascore`, dan `votes`
    * Buatlah plot dari 7 film paling populer di tahun 2021.


Happy learning! 
