from bs4 import BeautifulSoup
from grimm.сесија import Сесија


СПИСАК = "https://www.grimmstories.com/de/grimm_maerchen/list"


def главна():
    сесија = Сесија()
    одг = сесија.дај(СПИСАК)
    одг.добар()
    супа = BeautifulSoup(одг.текст, 'html.parser')
    for линк in супа.body.find_all('ul')[1].find_all('a'):
        print(линк.get('href'))


if __name__ == '__main__':
    главна()
