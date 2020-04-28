import sys
from pathlib import Path
from bs4 import BeautifulSoup
from grimm.контејнер import Контејнер
from grimm.трансформатор import Трансформатор
from grimm.токенизер import Токенизер
from grimm.линајзер import Линајзер
ТМПДИР = Path("/tmp/www.grimmstories.com/")
ТМПДИР0 = Path("/tmp/www.grimmstories.com/0/")
ТМПДИР1 = Path("/tmp/www.grimmstories.com/1/")
ТМПДИР2 = Path("/tmp/www.grimmstories.com/2/")
СПИСАК = "https://www.grimmstories.com/de/grimm_maerchen/list"


def скини_списак(сесија, урл):
    одг = сесија.дај(урл)
    одг.добар()
    супа = BeautifulSoup(одг.текст, 'html.parser')
    return [линк.get('href') for линк in супа.body.find_all('ul')[1].find_all('a')]


def извуци_текст(html_doc):
    супа = BeautifulSoup(html_doc, 'html.parser')
    рез = {}
    pt = супа.find(id='plainText')
    рез["title"] = pt.h1.get_text()
    рез["text"] = pt.find_all('div', class_='text')[0].get_text()
    return рез["text"]


def разби_на_линије(текст):
    ток = Токенизер(текст)
    токени = ток()
    лин = Линајзер(токени)
    линије = лин()
    return '\n'.join(линије)


def главна():
    к = Контејнер()
    сесија = к.сесија(тмпдир=ТМПДИР)
    списак = скини_списак(сесија, СПИСАК)
    сесија = к.сесија(тмпдир=ТМПДИР0)
    for линк in списак:
        одговор = сесија.дај(линк)
        if одговор.кеширан:
            print('КЕШ', сесија.кеш_путања(линк))
        else:
            print('СКИНУТ', сесија.кеш_путања(линк))
    Трансформатор(ТМПДИР0, ТМПДИР1, извуци_текст)()
    Трансформатор(ТМПДИР1, ТМПДИР2, разби_на_линије)(кеширај=False)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    главна()

