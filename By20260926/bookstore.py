class book:

    def setdata(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def printdata(self):
        print(f"제목: {self.title}")
        print(f"가격: {self.price}")
        print(f"작가: {self.author}")

    def __init__(self, title, price, author) -> None:
        self.setdata(title, price, author)
        print('새 책을 만들었습니다.')