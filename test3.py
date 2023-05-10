from tkinter import *


def print_use():
    print("Молодец!")


root = Tk()
root.title("bot")
root.geometry('800x400')


btn1 = Button(root, text="Жми ты же молодец", bg="white", fg="black", command=print_use)
btn1.place(x=300, y=260)

root.mainloop()