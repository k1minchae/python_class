# 아래 클래스를 수정하시오.
class StringRepeater:
    def __init__(self, times, greet):
        self.times = times
        self.greet = greet

    def repeat_string(self):
        for _ in range(self.times):
            print(self.greet)

repeater1 = StringRepeater(3, 'Hello') # 인스턴스 변수 생성
repeater1.repeat_string()   # 메서드 호출



