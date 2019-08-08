import sys
from bs4 import BeautifulSoup


def extract(soup):
    for link in soup.find("ul", {"id": "lcp_instance_0"}).find_all('a'):
        print(link.get('href'))
    pass


def main():
    html_doc = sys.stdin.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    extract(soup)


if __name__ == '__main__':
    main()
