# import PlayerModule
from PlayerModule import Player
import random

class GuessingGame:
    #attribute - correct number, player1, player2,..
    #operation - start the game, declare the winner

    def __init__(self):
        self.correctAnswer = -1
        self.rounds = 10

        #GuessingGame class object HAS-A Player class object
        self.player1 = Player("Daniel")     #object of Player class
        # self.player1.__name = "Abira"
        # self.player1.__guessedNumber = 40 #shouldn't be allowed - only player can change/decide their guessed number

        self.player2 = Player("Deni")
        self.player3 = Player("Hyder")

    def startGame(self):
        self.correctAnswer = random.randint(1, 100)
        print(f'The correct number is {self.correctAnswer}')
        print("I have number between 1 to 100..Can you guess it correctly ?")

        winner = False

        for i in range(self.rounds):
            self.player1.playGame()
            # self.player2.playGame()
            # self.player3.playGame()
            winner = self.checkWinner()
            print(f'Number of attempts remaining : {self.rounds - (i + 1)}')

            if winner:
                print(f'The correct number is {self.correctAnswer}')
                break
            elif self.player1.getGuessedNumber() > self.correctAnswer:
                print(f'Your guessed number {self.player1.getGuessedNumber()} is too high')
            elif self.player1.getGuessedNumber() < self.correctAnswer:
                print(f'Your guessed number {self.player1.getGuessedNumber()} is too low')

            # if winner:
            #     print(f'The correct number is {self.correctAnswer}')
            #     break
            # elif self.player1.__guessedNumber > self.correctAnswer:
            #     print(f'Your guessed number {self.player1.__guessedNumber} is too high')
            # elif self.player1.__guessedNumber < self.correctAnswer:
            #     print(f'Your guessed number {self.player1.__guessedNumber} is too low')
        else:
            print("Game Over...Better luck next time")
            

        # while winner == False:
        #     self.player1.playGame()
        #     # self.player2.playGame()
        #     # self.player3.playGame()

        #     winner = self.checkWinner()

        #     if winner:
        #         print(f'The correct number is {self.correctAnswer}')
        #     else:
        #         print(f'Winner not found..continuing the game..')


    def checkWinner(self):
        winnerFound = False #winner not found currently

        if self.player1.getGuessedNumber() == self.correctAnswer:
            print(f'{self.player1.getName()} is the winner')
            winnerFound = True

        # if self.player2._guessedNumber == self.correctAnswer:
        #     print(f'{self.player2._name} is the winner')
        #     winnerFound = True

        # if self.player3._guessedNumber == self.correctAnswer:
        #     print(f'{self.player3._name} is the winner')
        #     winnerFound = True

        return winnerFound






