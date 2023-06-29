import abc #抽象化(不在母類別定義，在子類別定義)

class Poultry(abc.ABC):
    def __init__(self, color, sound, specy):
        self.color = color
        self.sound = sound
        self.specy = specy

    def make_sound(self):
        print(f"{self.specy} is making some noise!!{self.sound * 3}")

    def move(self):
        print(f"{self.specy} move.")

    @abc.abstractmethod #抽象化
    def eat(self):
        pass

    def hatch(self):
        print(f"{self.specy} hatch zzz.")

class Duck(Poultry):
    def __init__(self, color, sound):
        super().__init__(color, sound, "Duck")

    def swim(self):
        print(f"{self.specy} swim~")

    def eat(self):
        print(f"{self.specy} eat vegetable.")

    def move(self):
        print(f"{self.specy} don't want to move.") #當子類別有定義時，以子類別為優先

class Chicken(Poultry):  #繼承
    def __init__(self, color, sound):
        super().__init__(color, sound, "Chicken")

    def morning_call(self, time):
        print(f"{self.sound*3}, It's{time} am now!")

    def eat(self):
        print(f"{self.specy} eat sworm.")

if __name__ == '__main__':
    duck_1 = Duck('yellow', "Ba")
    duck_2 = Duck('black', "Ga")
    duck_3 = Duck("White", "Gua")
    duck_2.make_sound()
    print(duck_2.sound)
    duck_2.eat()
    duck_2.move()

    chicken_1 = Chicken('Brown', "Gu")
    print(chicken_1.sound)
    chicken_1.eat()
    chicken_1.move()