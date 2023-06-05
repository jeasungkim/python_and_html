from tkinter import *

window = Tk()
window.geometry("400x400")
photo = PhotoImage(file = "D:\\python\\b41915014\\3B_0420\\jjjj.png")
photo2 = PhotoImage(file = "D:\\python\\b41915014\\3B_0420\\kkkk.png")
label1 =Label(window, image = photo)
label2 =Label(window, image = photo2)
label1.pack(side = LEFT)
label2.pack(side = RIGHT)
window.mainloop()