# Scope - область видимости

def create_cat_profile(name: str, age: int, **kwargs: str) -> None:
    print('Профиль кота:')
    print(f'Имя: {name}')
    print(f'Возраст: {age} года')
    for key in kwargs:
        print(f'{key}: {kwargs[key]}')



create_cat_profile("Мурзик", 3, порода="Сиамский", цвет="Черный")
create_cat_profile("Барсик", 5, страна="Китай", хобби="Ловить мышей")