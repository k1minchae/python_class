# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, x, y):
        self.width = x
        self.height = y
    
    def print_info(self):
        print(f'Width: {self.width}\nHeight: {self.height}\nArea: {self.width * self.height}\nPerimeter: {2*(self.height + self.width)}')

shape1 = Shape(5, 3)
shape1.print_info()
