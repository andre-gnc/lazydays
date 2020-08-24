import requests
from bs4 import BeautifulSoup


def make_soup(ms_url):
    # Make soups of each url.
    response = requests.get(ms_url)
    data = response.text
    ms_soup = BeautifulSoup(data, 'html.parser')
    return ms_soup


url = 'https://www.lazydays.com/rvs/?query=inventoryLocation.id%3A759940&page=1&limit=12'

test = 'yes'
page_test = 1
item_no = 0
item_dict = {}

while True:
    soup = make_soup(url)
    # ==============================================================================================
    # print(soup)
    if test == 'yes':
        break
# Belum selesai.
# ========================================================================================================
