# Инкапсуляция - encapsulation

class Car:
    # Конструктор - вызывается при создании нового экземпляра
    def __init__(self, color, mark, model):
        self.color = color
        self.mark = mark
        self.model = model
        self.engine_started = False

    def start_engine(self):
        self.engine_started = True

    def stop_engine(self):
        self.engine_started = False

    def drive_to(self, city):
        if self.engine_started:
            print(f'{self.color} {self.mark} {self.model} driving to {city}')
        else:
            print('Engine is not started')

    def honk(self):
        print('HONK-HONK')

    def colorize(self, new_color):
        self.color = new_color


c1 = Car('blue', 'Lamborgini', 'Aventador')
# c1.engine_started = True - BAD
c1.colorize('red')
c1.drive_to('Washington')

c2 = Car('grey', 'Tesla', 'Model X')
c2.drive_to('Berlin')
