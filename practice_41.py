# super 이어서
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self) # 다중상속, 모든 부모 클라스로 부터 추가가 필요할때
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()