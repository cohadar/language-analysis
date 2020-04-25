from requests import Session
from grimm.сесија import Сесија
import dependency_injector.containers as containers
import dependency_injector.providers as providers


class Контејнер(containers.DynamicContainer):
    def __init__(к):
        super().__init__()
        к.сирова_сесија = providers.Factory(Session)
        к.сесија = providers.Factory(Сесија, сирова_сесија=к.сирова_сесија)

