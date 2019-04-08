from bs4 import BeautifulSoup


def extract(soup):
    for link in soup.body.find_all('ul')[1].find_all('a'):
        print(link.get('href'))
    pass


def main():
    with open('list.html', 'r') as f:
        html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        extract(soup)


if __name__ == '__main__':
    main()
