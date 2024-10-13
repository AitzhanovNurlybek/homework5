class Book:
    def __init__(self, name, author, price, qty=0):
        self.name, self.author, self.price, self.qty = name, author, price, qty

    def __str__(self):
        return f"Book[name={self.name}, {self.author}, price={self.price}, qty={self.qty}]"


book = Book("Pride and Prejudice", author, 19.99, 5)
print(book)