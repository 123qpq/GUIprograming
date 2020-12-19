import tkinter.ttk as ttk
from tkinter import * 


root = Tk()
root.title("kyongmin GUI") 
root.geometry("640x480+100+200")

values = [str(i) + "일" for i in range(1, 32)] #1~31까지 숫자
combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
combobox.current(1) #0번째 인덱스 값 선택
combobox.pack()
combobox.set("카드 결제일")

def btncmd():
    print(combobox.get())


btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()