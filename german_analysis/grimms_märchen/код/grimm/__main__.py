from контејнер import Контејнер
from bs4 import BeautifulSoup
СПИСАК = "https://www.grimmstories.com/de/grimm_maerchen/list"


def скини_списак(сесија, урл):
    одг = сесија.дај(урл)
    одг.добар()
    супа = BeautifulSoup(одг.текст, 'html.parser')
    return [линк.get('href') for линк in супа.body.find_all('ul')[1].find_all('a')]


def главна():
    к = Контејнер()
    сесија = к.сесија()
    списак = скини_списак(сесија, СПИСАК)
    for линк in списак:
        print(линк)
        сесија.дај(линк)


if __name__ == '__main__':
    главна()

