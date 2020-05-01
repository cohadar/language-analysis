class Словизер():
    def __init__(бре, текст, почетак, крај):
        assert len(текст) > 0
        бре._текст = текст
        бре._индекс = -1
        бре._линија = 1
        бре.почетак = почетак
        бре.крај = крај

    @property
    def линија(бре):
        return бре._линија

    @property
    def претходно(бре):
        return бре.почетак if бре._индекс <= 0 else бре._текст[бре._индекс - 1]

    @property
    def тренутно(бре):
        return бре.почетак if бре._индекс < 0 else бре._текст[бре._индекс]

    @property
    def следеће(бре):
        return бре.крај if бре._индекс >= len(бре._текст) - 1 else бре._текст[бре._индекс + 1]

    @property
    def индекс(бре):
        return бре._индекс

    def __next__(бре):
        if бре._индекс >= len(бре._текст) - 1:
            raise StopIteration()
        бре._индекс += 1
        if бре.тренутно == '\n':
            бре._линија += 1
        return бре.тренутно

    def __str__(бре):
        return f"[{бре.претходно}], [{бре.тренутно}], [{бре.следеће}]"

