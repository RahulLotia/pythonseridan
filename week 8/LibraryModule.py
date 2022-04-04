from BookModule import Book

class Library:
    def __init__(self, name: str, books : list):
        self._libraryName = name
        #Library HAS-A Books
        self._bookList = books #List of books

    def __str__(self):
        outputString  = f'{self._libraryName}'  #Sacred Library

        for book in self._bookList:
            outputString += f'\n{book}'   #The pyramid, Pharao, Egypt
                                        #The Alchemist, Coelho, Mars Publishers

        return outputString

