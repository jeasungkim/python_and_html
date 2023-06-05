from tkinter import *

window = Tk()

window.title("레이블")
label1 = Label(window, text = "안녕하세요! 김재성 입니다.")
label2 = Label(window, text = "I love Python", font = ("궁서체",30), fg = "red")
label3 = Label(window, text = "Love is", bg = "yellow", width = 20, height = 30, anchor = NE)

label1.pack()
label2.pack()
label3.pack()
window.mainloop()