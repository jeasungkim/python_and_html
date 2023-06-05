from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("강아지 버튼", "우강귀")

tk = Tk()
photo = PhotoImage(file = "D:\\python\\b41915014\\3B_0420\\jjjj.png")
tk.geometry("1000x600")
#button1 = Button(tk, text="파이썬 종료", fg="blue", bg= "yellow",command=quit)
button1 = Button(tk, image = photo, command=myFunc)
button1.pack()

tk.mainloop()