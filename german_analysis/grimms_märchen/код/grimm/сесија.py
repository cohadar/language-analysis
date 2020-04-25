import requests


class Одговор():
    def __init__(бре, resp):
        бре.resp = resp
        бре.текст = resp.text

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


class Сесија():
    def __init__(бре, кеширано=True):
        бре.кеширано = кеширано
        бре.сесија = requests.Session()

    def дај(бре, урл):
        return Одговор(бре.сесија.get(урл))

