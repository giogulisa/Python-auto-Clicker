from tkinter import *
from tkinter import ttk
from Clicker import clicker


class Main:

    def __init__(self, root):
        self.entry_value = StringVar(root, value="")
        self.entry_value_Delay = StringVar(root, value="")
        root.title("Clicker")
        root.geometry("210x300")
        root.resizable(width=False, height=False)
        style = ttk.Style()

        style.configure("TButton",
                        font="Serif 8",
                        padding=5)

        style.configure("TLabel",
                        font="Serif 12",
                        padding=8)

        style.configure("TEntry",
                        font="Serif 18",
                        padding=5)

        self.number = ttk.Label(root, text="Enter number of Clicks:")
        self.number.grid(row=0, columnspan=4)

        self.number_entry1 = ttk.Entry(root,
                                       textvariable=self.entry_value, width=10)
        self.number_entry1.grid(row=1, columnspan=1)

        # delay
        self.numberDelay = ttk.Label(root, text="Enter number of Delay:")
        self.numberDelay.grid(row=2, column=0)

        self.number_delay = ttk.Entry(root,
                                      textvariable=self.entry_value_Delay, width=10)
        self.number_delay.grid(row=3, columnspan=1)

        self.button_start = ttk.Button(root, text="Start",
                                       command=lambda: self.start_button_press()).grid(row=4, column=0)

        self.start_Warn = ttk.Label(root, text="press S for Start/Stop")
        self.start_Warn.grid(row=5, column=0)
        self.exit_Warn = ttk.Label(root, text="press E for Exit")
        self.exit_Warn.grid(row=6, column=0)

    def start_button_press(self):
        print("click numer is: " + self.entry_value.get())
        print("delay numer is: " + self.entry_value_Delay.get())
        click_number = self.entry_value.get()
        delay_number = float(self.entry_value_Delay.get())

        clicker(click_number, delay_number)


root = Tk()

main = Main(root)
root.mainloop()
