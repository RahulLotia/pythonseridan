
from GuessingGameModule import GuessingGame

class Application:
    def run(self):
        game = GuessingGame()
        game.startGame()

app = Application()
app.run()