import json
import textwrap
from pathlib import Path
from bs4 import BeautifulSoup
from grimm.контејнер import Контејнер
from grimm.трансформатор import Трансформатор
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
    return json.dumps(рез)


def wrap(text):
    lines = text.splitlines()
    wrapped = []
    for line in lines:
        wrapped.extend(textwrap.wrap(line, 70))
    return wrapped


def сави_текст(текст):
    линије = []
    for line in текст.splitlines(keepends=False):
        a = json.loads(line)
        b = []
        b.append(wrap(a["title"]))
        b.append(wrap(a["text"]))
        линије.append(json.dumps(b))
    return '\n'.join(линије)


def главна():
    к = Контејнер()
    сесија = к.сесија(тмпдир=ТМПДИР0)
    списак = скини_списак(сесија, СПИСАК)
    for линк in списак:
        одговор = сесија.дај(линк)
        if одговор.кеширан:
            print('КЕШ', сесија.кеш_путања(линк))
        else:
            print('СКИНУТ', сесија.кеш_путања(линк))
    Трансформатор(ТМПДИР0, ТМПДИР1, извуци_текст)()
    Трансформатор(ТМПДИР1, ТМПДИР2, сави_текст)()


if __name__ == '__main__':
    главна()

