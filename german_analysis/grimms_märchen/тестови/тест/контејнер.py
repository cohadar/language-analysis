from grimm.__main__ import Контејнер as К
from grimm.сесија import Response
import dependency_injector.providers as providers


class ТестСироваСесија():
    def get(бре, урл):
        return Response(урл, 200, 'тест текст')


class Контејнер(К):
    def __init__(к):
        super().__init__()
        к.сирова_сесија.override(providers.Factory(ТестСироваСесија))

