from ExceptionModule import NumberTooSmallError
from ExceptionModule import NumberTooHighError

class ExceptionHandling:

    def avg(self, numbers):
        assert len(numbers) != 0, "List of numbers cannot be empty"
        return sum(numbers) / len(numbers)

    def playAttempt(self):
        count = 10
        correctNumber = 50

        while count > 0:
            try:
                inputNumber = int(input("Enter your guessed number : "))

                if inputNumber < correctNumber:
                    raise NumberTooSmallError
                elif inputNumber > correctNumber:
                    raise NumberTooHighError
                else:
                    print("You won the game")
                    break

            except ValueError as ve:
                print(ve)
            except NumberTooHighError as he:
                print(he)
            except NumberTooSmallError as se:
                print(se)
            finally:
                count -= 1

    def divide(self, num1, num2):

        result = 0
        try:
            # num1 = int(input("Enter number 1 : "))
            # num2 = int(input("Enter number 2 : "))
            result = num1 / num2
        except ZeroDivisionError:
            print("Division by zero is not allowed")
        except ValueError as ve:
            print(f'The given input is not in the correct type : {ve}')
        except TypeError as te:
            print(f'Division needs two integer numbers : {te}')
        except:
            print("Somethign went wrong. Couldn't complete the operation.")
        else:
            print(f'Result of {num1} / {num2} = {result}')
        finally:
            print(f'-----------This statement is from finally block')
        
