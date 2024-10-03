class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_horsepower(self):
        return self.__engine_power

    def set_horsepower(self, engine_power):
        self.__engine_power = engine_power

    def get_color(self):
        return self.__color

    def set_color(self, color):
        if color.lower() not in Vehicle.__COLOR_VARIANTS:
            print(f"Нельзя сменить цвет на {color}")

        self.__color = color

    def print_info(self):
        print(f"Модель: {self.get_model()}")
        print(f"Мощность двигателя: {self.get_horsepower()}")
        print(f"Цвет: {self.get_color()}")
        print(f"Владелец: {self.owner}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
