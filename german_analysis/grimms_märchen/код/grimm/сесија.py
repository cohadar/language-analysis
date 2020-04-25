import hashlib
from pathlib import Path
from collections import namedtuple


Response = namedtuple('Response', ['url', 'status_code', 'text'])


class Одговор():
    def __init__(бре, resp, кеширан=False):
        бре.resp = resp
        бре.текст = resp.text
        бре.кеширан = кеширан

    def ок(бре):
        return бре.resp.status_code == 200

    def све(бре):
        return f"\n{бре.resp.url}\n{бре.resp.status_code}\n{бре.resp.text}"

    def добар(бре):
        if not бре.ок():
            raise Exception(бре.све())

    def пп(бре):
        if бре.ок():
            print(бре.resp.text)
        else:
            raise Exception(бре.све())


def sha256(урл):
    с = hashlib.new('sha256')
    с.update(bytes(урл, 'utf-8'))
    return с.hexdigest()


class Сесија():
    def __init__(бре, сирова_сесија, кеширај=True):
        бре.кеширај = кеширај
        бре.сирова = сирова_сесија

    def дај(бре, урл):
        if бре.кеширај:
            кеш = sha256(урл)
            путања = Path('/tmp').joinpath(кеш)
            if путања.exists():
                with путања.open('r') as ф:
                    текст = ф.read()
                    return Одговор(Response(урл, 200, текст), кеширан=True)
            else:
                resp = бре.сирова.get(урл)
                if resp.status_code == 200:
                    with путања.open('w') as ф:
                        ф.write(resp.text)
                return Одговор(resp)
        return Одговор(бре.сирова.get(урл))

