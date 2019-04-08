import sys
import json
from bs4 import BeautifulSoup


def extract(soup):
    ret = {}
    pt = soup.find(id='plainText')
    ret["title"] = pt.h1.get_text()
    ret["text"] = pt.find_all('div', class_='text')[0].get_text()
    json.dump(ret, sys.stdout)


def main():
    html_doc = sys.stdin.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    extract(soup)


if __name__ == '__main__':
    main()
