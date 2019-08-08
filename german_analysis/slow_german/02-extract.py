import sys
import json
from bs4 import BeautifulSoup


def extract(soup):
    return soup.find_all('div', class_='entry-content')[0].get_text()


def main():
    html_doc = sys.stdin.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(extract(soup), end='')


if __name__ == '__main__':
    main()
