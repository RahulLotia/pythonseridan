import random


class Player:
    #attributes - name, guessed Number
    #operation - play game

    def __init__(self, nm):
        #private field variable using __ (double underscore) as prefix to variable name
        # self._name = "Unknwon"
        self.__name = nm
        self.__guessedNumber = -1

    #accessor and mutator functions

    #accessor method for guessedNumber
    def getGuessedNumber(self):
        return self.__guessedNumber

    def getName(self):
        return self.__name

    def playGame(self):
        #guess a random number between 1 to 100
        # self._guessedNumber = random.randint(1, 100)

        self.__guessedNumber = int(input("Enter your guess : "))
        print(f'{self.__name} guessed {self.__guessedNumber}')