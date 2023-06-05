#count
from tkinter import *

tk = Tk()
counter = 0

def clicked1():
    global counter
    counter += 1
    label1['text'] = '버튼 클릭 수:' + str(counter)

def clicked2():
    global counter
    counter -= 1
    label1['text'] = '버튼 클릭 수:' + str(counter)

def reset():
    global counter
    counter = 0
    label1['text'] = '카운트 :'

tk.title('GUI 카운터')
label1 = Label(tk, text='옆에 버튼 있음', fg='blue',font =20)
label1.pack(side = LEFT, padx = 10, pady = 10)

#button1
button1 = Button(tk,text='카운트 증가', bg='green', font=15, width=30, height=5, command= clicked1)
button1.pack(side=LEFT,padx=10, pady=10)

button2 = Button(tk,text='리셋', bg='red', font=15, width=30, height=5, command=reset)
button2.pack(side=LEFT,padx=10, pady=10)

button3 = Button(tk,text='카운트 감소', bg='green', font=15, width=30, height=5, command= clicked2)
button3.pack(side=LEFT,padx=10, pady=10)

tk.mainloop()