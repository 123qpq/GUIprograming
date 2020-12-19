from tkinter import * 


root = Tk()
root.title("kyongmin GUI") 
root.geometry("500x300+100+200")

txt = Text(root, width=40, height=3) #여러줄 입력 시
txt.pack()

txt.insert(END, "글자를 입력하세요.")

e = Entry(root, width=30) #한줄만 입력시(id, pwd)
e.pack()
e.insert(0, "아이디 및 비밀번호 입력")

def btncmd():
    print(txt.get("1.0", END)) #1.0 의미 : 1은 라인 1부터, 0은 colum기준 0번째부터~end까지
    print(e.get()) #entry는 한줄이므로 컬럼필요없음

    txt.delete("1.0", END) #내용 삭제
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()