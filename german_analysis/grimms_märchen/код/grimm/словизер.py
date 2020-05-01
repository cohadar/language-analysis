class Словизер():
    def __init__(бре, текст):
        assert len(текст) > 0
        бре._текст = текст
        бре._индекс = -1

    @property
    def претходно(бре):
        return -1 if бре._индекс <= 0 else бре._текст[бре._индекс - 1]

    @property
    def тренутно(бре):
        return -1 if бре._индекс < 0 else бре._текст[бре._индекс]

    @property
    def следеће(бре):
        return -1 if бре._индекс >= len(бре._текст) - 1 else бре._текст[бре._индекс + 1]

    @property
    def индекс(бре):
        return бре._индекс

    def __next__(бре):
        if бре._индекс >= len(бре._текст) - 1:
            raise StopIteration()
        бре._индекс += 1
        return бре.тренутно

