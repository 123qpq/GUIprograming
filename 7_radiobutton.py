from tkinter import * 


root = Tk()
root.title("kyongmin GUI") 
root.geometry("640x480+100+200")

label1 = Label(root, text="메뉴를 선택하세요").pack()


burger_var = IntVar() #int 이므로 정수 반환(value)
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="불고기버거", value=3, variable=burger_var)

btn_burger1.select() #기본값 선택
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label1 = Label(root, text="음료를 선택하세요").pack()


drink_var = StringVar() #string 이므로 문자열 반환(value)
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var).pack()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var).pack()

def btncmd():
    print(burger_var.get()) #선택된 항목의 값(value)을 반환
    print(drink_var.get())



btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()