from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self , master = None):
        self.feet_value = StringVar()
        self.meter_value = StringVar()

        Frame.__init__(self, master)
        self.pack()

        # self.createWidgets()
        self.createConverter()

    def createWidgets(self):
        #creating widget
        self.btn_hello = Button(self)
        self.btn_hello["text"] = "Say Hello"
        self.btn_hello["command"] = self.sayingHello
        self.btn_hello['fg'] = "blue"
        self.btn_hello.pack()

        self.btn_quit = Button(self, text="Close Window", command = root.destroy, fg="red")
        self.btn_quit.pack()

    def sayingHello(self):
        # print("hello Tkinter")
        self.dialog = messagebox.showinfo(title="Greetings !", message="Hello from Tkinter")

    def createConverter(self):
        self.lbl_header = Label(self, text = "Feet to Meter Converter", bg = "blue", fg = "#ffffff")
        # self.lbl_header.pack()
        self.lbl_header.grid(column=3, row=1)

        self.lbl_feet = Label(self, text= "Feet")
        self.lbl_feet.grid(column=1, row=2)

        self.lbl_meter = Label(self, text= "Meter")
        self.lbl_meter.grid(column=5, row=2)

        self.lbl_equal = Label(self, text= "=")
        self.lbl_equal.grid(column=3, row=2)

        #take input from user
        self.entry_feet = Entry(self, textvariable = self.feet_value, width=7)
        self.entry_feet.grid(column=2, row=2)

        self.lbl_meter_output = Label(self, text= "output", bg = "lightgrey", fg = "red")
        self.lbl_meter_output.grid(column=4, row=2)

        self.btn_convert = Button(self, text= "Convert", command= self.conversion)
        self.btn_convert.grid(column=3, row=3)

    def conversion(self):
        try:
            feet = float(self.entry_feet.get())
            meters = round((feet / 3.28), 3)

            self.lbl_meter_output["text"] = meters

        except ValueError as ve:
            print("Unable to perform conversions", ve)
        except:
            print("Something went wrong")


root = Tk()
root.title("Hello Tkinter")
root.geometry("400x200")
app = Application(master = root)
app.mainloop()