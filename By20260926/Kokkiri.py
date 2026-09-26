class Fridge:
    def __init__(self):
        self.isOpened = False
        self.foods = []
    
    def open(self):
        self.isOpened = True
        print("냉장고의 문을 열었습니다.")

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print(f"냉장고 속에 {thing}이 들어갔습니다.")
        else:
            print("냉장고가 닫혀져 있기 때문에 음식을 넣을 수 없습니다.")
    
    def close(self):
        self.isOpened = False
        print("냉장고의 문을 닫았습니다.")

class Food:
    pass

