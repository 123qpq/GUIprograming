import tkinter.messagebox as msgbox
from tkinter import * 


root = Tk()
root.title("kyongmin GUI") 
root.geometry("640x480+100+200")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side = "right", fill="y")

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set)#yscrollcommand 가 없으면 동작안함

for i in range(1, 32):
    listbox.insert(END, str(i) + "일")

listbox.pack(side="left")

scrollbar.config(command=listbox.yview) #scroll 과 listbox 동기화


root.mainloop()