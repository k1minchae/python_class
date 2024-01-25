# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1


class Dog(Animal):
    def __init__(self):
        super().__init__()
    def bark(self):
        print('멍 멍 !')
    

class Cat:
    def __init__(self):
        super().__init__()


    def meow(self):
        print('야 옹 !')


class Pet(Dog, Cat):
    def __init__(self, sound):
        super().__init__()
        self.sound = sound

    def play(self):
        print('애완동물과 놀기')

    def make_sound(self):
        print(f'{self.sound}')


pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
