class Car:
    # Конструктор - вызывается при создании нового экземпляра
    def __init__(self, color, mark, model):
        self.color = color
        self.mark = mark
        self.model = model

    def drive_to(self, city):
        print(f'{self.color} {self.mark} {self.model} driving to {city}')

    def honk(self):
        print('HONK-HONK')


c1 = Car('blue', 'Lamborgini', 'Aventador')
c1.drive_to('Washington')

c2 = Car('red', 'Tesla', 'Model X')
c2.drive_to('Berlin')
