# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, x, y):
        self.width = x
        self.height = y

    def __str__(self):
        return f'Shape: width={self.width}, height={self.height}'

shape1 = Shape(5, 3)
print(shape1)
