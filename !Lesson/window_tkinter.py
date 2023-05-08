from tkinter import *


def print_use():
    print("Work")

root = Tk()
root.title("bot")
root.geometry('800x400')
l1 = Label(text="Ссылка на комментарий", bg="#ffaaaa")
l1.place(x=220, y=3)
l3 = Label(text="Текст для поиска.", bg="#ffaaaa")
l3.place(x=220, y=83)
l4 = Label(text="Общее количество комментариев", bg="#ffaaaa")
l4.place(x=220, y=103)
l5 = Label(text="Количество комментариев под одним видео", bg="#ffaaaa")
l5.place(x=220, y=123)
l6 = Label(text="Задержка", bg="#ffaaaa")
l6.place(x=220, y=143)
l7 = Label(text="Количество комментариев в топе", bg="#ffaaaa")
l7.place(x=220, y=163)

text2 = Entry(bg="white", fg='black')
text2.place(x=0, y=3)
text3 = Entry(bg="white", fg='black')
text3.place(x=0, y=83)
text4 = Entry(bg="white", fg='black')
text4.place(x=0, y=103)
text5 = Entry(bg="white", fg='black')
text5.place(x=0, y=123)
text6 = Entry(bg="white", fg='black')
text6.place(x=0, y=143)
text7 = Entry(bg="white", fg='black')
text7.place(x=0, y=163)

chkValue2 = BooleanVar()
chkValue2.set(False)
chk2 = Checkbutton(root, text='Отвечать на комментарии в топе', var="chkValue2")
chk2.place(x=0, y=63)

btn1 = Button(root, text="Режим комментирования", bg="white", fg="black", command=print_use)
btn1.place(x=300, y=260)

btn2 = Button(root, text="Режим проставления лайков", bg="white", fg="black", command="like")
btn2.place(x=300, y=290)

btn3 = Button(root, text="shorts", bg="white", fg="black", command="shorts")
btn3.place(x=300, y=320)

btn4 = Button(root, text="Комментирование одного видео", bg="white", fg="black", command="one_video")
btn4.place(x=300, y=350)

root.mainloop()