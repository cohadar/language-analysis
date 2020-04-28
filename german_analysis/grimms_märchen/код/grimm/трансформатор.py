class Трансформатор():
    def __init__(бре, дир1, дир2, трансформација):
        бре.дир1 = дир1
        бре.дир2 = дир2
        бре.трансформација = трансформација

    def __call__(бре, кеширај=True):
        if not бре.дир1.exists():
            бре.дир1.mkdir()
        if not бре.дир2.exists():
            бре.дир2.mkdir()
        for фајл1 in бре.дир1.iterdir():
            фајл2 = бре.дир2.joinpath(фајл1.name)
            if кеширај and фајл2.exists():
                print('КЕШ', фајл2)
                continue
            with фајл1.open('r') as ф1:
                try:
                    with фајл2.open('w') as ф2:
                        ф2.write(бре.трансформација(ф1.read()))
                        print('ТРАНС', фајл2)
                except Exception as е:
                    фајл2.unlink()
                    raise Exception(фајл1) from е

