class book:
    def __init__ (self, title, author):
        self.book_title = title
        self.book_author = author

    def __str__(self):
        
        return f"이 책의 제목은 {self.book_title}이고, 저자는 {self.book_author}입니다."
    

