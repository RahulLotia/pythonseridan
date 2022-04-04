from MortgageModule import Mortgage
from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.housePrice = DoubleVar()
        self.term = IntVar()
        self.rateOfInterest = DoubleVar()
        self.downPer = DoubleVar()
        self.lbl_mortgage_amount = Label()

        self.pack()
        self.showGUI()

    def showGUI(self):
        self.lbl_header = Label(self, text = "Mortgage Calculator" , fg="#ffffff")
        self.lbl_header["bg"] = "dodger blue"
        self.lbl_header.grid(row = 1, columnspan = 5)

        self.lbl_house_price = Label(self, text = "House Price : ")
        self.lbl_house_price.grid(row = 3, column = 2)

        self.lbl_term = Label(self, text = "Term (years) : ")
        self.lbl_term.grid(row = 4, column = 2)

        self.lbl_rate = Label(self, text = "Rate of Interest (%) : ")
        self.lbl_rate.grid(row = 6, column = 2)

        self.lbl_down = Label(self, text = "Down Payment (%) : ")
        self.lbl_down.grid(row = 7, column = 2)

        # self.lbl_header.pack()
        # self.lbl_house_price.pack();
        # self.lbl_term.pack()
        # self.lbl_rate.pack()
        # self.lbl_down.pack()

        self.entry_house_price = Entry(self, width = 10, textvariable = self.housePrice).grid(row=3, column=3)

        self.rbt_term5 = Radiobutton(self, text = "05 Years", variable = self.term, value = 5).grid(row=4, column=3)
        self.rbt_term10 = Radiobutton(self, text = "10 Years", variable = self.term, value = 10).grid(row=5, column=3)
        self.rbt_term25 = Radiobutton(self, text = "25 Years", variable = self.term, value = 25).grid(row=4, column=4)
        self.rbt_term30 = Radiobutton(self, text = "30 Years", variable = self.term, value = 30).grid(row=5, column=4)

        self.entry_rate = Entry(self, textvariable = self.rateOfInterest, width=10).grid(row = 6, column=3)

        self.rbt_down5 = Radiobutton(self, text = "05 %", variable = self.downPer, value = 5).grid(row=7, column=3)
        self.rbt_down10 = Radiobutton(self, text = "10 %", variable = self.downPer, value = 10).grid(row=8, column=3)
        self.rbt_down20 = Radiobutton(self, text = "20 %", variable = self.downPer, value = 20).grid(row=9, column=3)

        self.btn_calculate = Button(self, text = "Calculate Monthly Mortgage", fg = "dodger blue", command = self.showOutput).grid(row=11, columnspan=5)

    def showOutput(self):
        print("Button clicked")

        hp = 0.0
        n = 0
        r = 0.00000001
        dp = 0.0

        try:
            hp = self.housePrice.get()
            n = self.term.get()
            r = self.rateOfInterest.get()
            dp = self.downPer.get()
        except ValueError as ve:
            self.error_dialog = messagebox.showerror(title="Error !", message=f'Something went wrong {ve}')
        except:
            self.error_dialog = messagebox.showerror(title="Error !", message="Something went wrong")
        else:
            mortgageObj = Mortgage(housePrice = hp, term = n, rate = r, downPer = dp)
            mortgageAmt = mortgageObj.getMonthlyMortgage()
            self.output_dialog = messagebox.showinfo(title = "Output", message = f'Monthly Mortgage Amount : $ {round(mortgageAmt, 2)}')


root = Tk()
root.title("Mortgage Calculator")
root.geometry("500x500")
app = Application(master=root)
app.mainloop()