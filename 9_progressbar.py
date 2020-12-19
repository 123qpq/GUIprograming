import time
import tkinter.ttk as ttk
from tkinter import * 


root = Tk()
root.title("kyongmin GUI") 
root.geometry("640x480+100+200")

p_var = DoubleVar() #실수범위
#progressbar = ttk.Progressbar(root, maximum = 100, mode = "determinate") #mode에 determinate:한방향(시작과 끝), indeterminate:양방향(무한)
progressbar = ttk.Progressbar(root, maximum = 100, length = 200, variable = p_var)
#progressbar.start(10) #10ms 마다 움직임
progressbar.pack()

def btncmd():
    #progressbar.stop() #작동 중지
    for i in range(1, 101):
        time.sleep(0.01)

        p_var.set(i) #progress bar 값 설정
        progressbar.update() # for문 동작할 때 마다 업데이트
        print(p_var.get())



btn = Button(root, text="시작", command=btncmd)
btn.pack()

root.mainloop()