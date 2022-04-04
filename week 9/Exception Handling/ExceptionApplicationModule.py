from ExceptionMethodModule import ExceptionHandling


class Application:
    def run(self):
        # self.testException()
        eh1 = ExceptionHandling()
        # eh1.divide(12, 6)
        # eh1.divide(12, 0)
        # eh1.divide(12, "ten")

        # eh1.playAttempt()

        print(f' avg = {eh1.avg(numbers = [1, 2, 3, 4, 5])}')
        print(f' avg = {eh1.avg(numbers = [])}')

        print("This statement is the last in run() method")

    def testException(self):
        
        #validate input
        while True:
            try:
                number = int(input("Enter number : "))
                print(f'Number = {number}')
                break
            except ValueError:
                print("Something went wrong. Incorrect type of value.")
            # except:
            #     print("Something went wrong.")

app = Application()
app.run()