import requests
from bs4 import BeautifulSoup


def get_html(url):
    respons = requests.get(url)
    return respons.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages_ul = soup.find('div', class_)
    


def main():
    nootebooks_url = "https://lalafo.kg/kyrgyzstan/kvartiry/arenda-kvartir/posutochnaya-arenda-kvartir"
    pages = "?page="
    get_total_pages(get_html(nootebooks_url))

main()

