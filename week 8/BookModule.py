class Book:
    def __init__(self, title: str, author: str, genre: str):
        self._title = title
        self._author = author
        self._genre = genre

    #accessor and mutator

    def __str__(self):
        return f'{self._title} \t {self._author} \t {self._genre}'