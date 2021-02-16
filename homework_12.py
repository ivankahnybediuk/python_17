import math

"""
Task 1
Method overloading.
Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, and make their
own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be
to print ‘meow’.
Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method
on input parameter.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Субклас должен имплементировать абстрактій метод!")


class Cat(Animal):
    voice = "Meov"

    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print(self.name + " says " + self.voice)


class Dog(Animal):
    voice = "Woof"

    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print(self.name + " says " + self.voice)


def changeVoice(animal):
    animal.voice = input("Enter new animal voice ")


if __name__ == "__main__":
    cat = Cat("Cat")
    dog = Dog("Dog")
    cat.talk()
    changeVoice(cat)
    cat.talk()

"""
Task 2
Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []
Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books 
list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year
All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books
```
class Library:
    pass
class Book:
    pass
class Author:
    pass
"""


class Library:
    def __init__(self, name, books, authors):
        self.name = name
        self.books = books
        self.authors = authors

    def new_book(self, book):
        original = False
        if self.books:
            for item in self.books:
                if item == book:
                    item.amountBooks += 1
                    original = False
                else:
                    original = True
        else:
            original = True
        if original:
            self.books.append(book)
            self.authors.add(book.author.name)
            book.author.books.append(book.name)

    def __str__(self):
        for book in self.books:
            print(book)

    def group_by_author(self, author):
        for book in self.books:
            if book.author.name == author:
                print(book)

    def group_by_year(self, year):
        for book in self.books:
            if book.year == year:
                print(book)


class Book:
    amountBooks = 1

    def __init__(self, name, year, author):
        self.name = name
        self.year = int(year)
        self.author = author

    def __str__(self):
        return f"Название: {self.name}\nГод: {self.year}\nАвтор: {self.author.name}\nКоличество: {self.amountBooks}\n" \
               f"Книги этого автора: {self.author.books}\n\n"

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.name == other.name


class Author:
    def __init__(self, name, country, birthday, books):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f"Имя: {self.name}\nСтрана: {self.country}\nДень рождения: {self.birthday}\n\n" \
               f"books: {self.books}"


if __name__ == "__main__":
    rowling = Author("Джоан Роулинг", "Великобритания", "31 июля 1965г", [])
    king = Author("Стивен Кинг", "США", "21 сентября 1947г", [])
    orwell = Author("Джордж Оруел", "Великобритания", "25 июня 1903г", [])
    firstLibrary = Library("FirstLibrary", [], set())
    firstLibrary.new_book(Book("Гарри Поттер и философский камень", 1997, rowling))
    firstLibrary.new_book(Book("Гарри Поттер и философский камень", 1997, rowling))
    firstLibrary.new_book(Book("Гарри Поттер и тайная комната", 1998, rowling))
    firstLibrary.new_book(Book("Стрелок", 1982, king))
    firstLibrary.new_book(Book("Извлечение троих", 1987, king))
    firstLibrary.new_book(Book("Скотный двор", 1945, orwell))
    firstLibrary.new_book(Book("1984", 1949, orwell))
    firstLibrary.new_book(Book("1984", 1949, orwell))
    firstLibrary.new_book(Book("1984", 1949, orwell))
    firstLibrary.new_book(Book("1984", 1949, orwell))
    firstLibrary.__str__()
    firstLibrary.group_by_author("Джордж Оруел")
    firstLibrary.group_by_year(1997)


"""
Task 3
Fraction
Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) 
with appropriate checking and error handling
```
class Fraction:
pass
x = Fraction(1/2)
y = Fraction(1/4)
x + y == Fraction(3/4)
"""


class Fraction:
    def __init__(self, number):
        self.number = number.split('/')
        self.num = int(self.number[0])
        self.det = int(self.number[1])

    def __add__(self, other):
        if self.det == other.det:
            num = self.num + other.num
            det = self.det
        else:
            num = self.num * other.det + other.num * self.det
            det = self.det * other.det
            i = math.gcd(num, det)
            num = num // i
            det = det // i
        return f'{num}/{det}'

    def __sub__(self, other):
        if self.det == other.det:
            num = self.num - other.num
            det = self.det
        else:
            num = self.num * other.det - other.num * self.det
            det = self.det * other.det
            i = math.gcd(num, det)
            num = num // i
            det = det // i
        return f'{num}/{det}'

    def __mul__(self, other):
        num = self.num * other.num
        det = self.det * other.det
        i = math.gcd(num, det)
        num = num // i
        det = det // i
        return f'{num}/{det}'

    def __floordiv__(self, other):
        num = self.num * other.det
        det = self.det * other.num
        i = math.gcd(num, det)
        num = num // i
        det = det // i
        if det != 1:
            return f'{num}/{det}'
        else:
            return num


    def __str__(self):
        return f"{self.num} / {self.det}"





if __name__ == "__main__":
    x = Fraction('1/2')
    y = Fraction('1/4')
    print(x + y)
    print(x - y)
    print(x * y)
    d = x // y
    print(d)
