class Author:
    def __init__(self, name, email, gender):
        self.name, self.email, self.gender = name, email, gender

    def __str__(self):
        return f"Author[name={self.name}, email={self.email}, gender={self.gender}]"


author = Author("Nuriman Baltabayev", "n_baltabayev@kbtu.kz", "male")
print(author)