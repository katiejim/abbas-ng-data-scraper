import os
import urllib.request
import requests, zipfile
from bs4 import BeautifulSoup
from io import BytesIO

year = input("Enter year in yyyy format: ")
month = input("Enter month in mm format: ")
strip_month = month.strip('0')

urls = []
url = 'https://data.nationalgrideso.com/system/system-frequency-data?from=0#resources'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

for link in soup.find_all('a'):
    urls.append(link.get('href'))


os.chdir("C:/Users/hale03k/Documents/Abbas")
dir = os.path.abspath('.')
work_path_zip = os.path.join(dir, 'NG Historic Frequency Data {}-{}.csv'.format(year, month))
work_path_csv = os.path.join(dir, 'NG Historic Frequency Data {}-{}.csv'.format(year, month))


zip_keyword = '{}-{}.zip'.format(year, strip_month)
csv_keyword = '{}-{}.csv'.format(year, strip_month)
for link in urls:
    if csv_keyword in link:
        urllib.request.urlretrieve(link, work_path_csv)
    elif zip_keyword in link:
        req = requests.get(link)
        zipfile = zipfile.ZipFile(BytesIO(req.content))
        zipfile.extractall("C:/Users/hale03k/Documents/Abbas")
        os.rename('fNew {} {}.csv'.format(year, strip_month), 'NG Historic Frequency Data {}-{}.csv'.format(year, month))








