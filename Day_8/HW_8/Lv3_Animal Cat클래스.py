# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1

class Cat:
    def __init__(self, cats):
        super().__init__()
        self.cats = cats

    def meow(self):
        print('야 옹 !')


cat1 = Cat("야옹")
cat1.meow()
