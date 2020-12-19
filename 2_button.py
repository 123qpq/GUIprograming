from tkinter import * #tkinter 에 있는 모든 페키지를 임포트 하겠다.

root = Tk()
root.title("kyongmin GUI") #제목 지정
root.geometry("640x480+100+200") #가로x세로+x위치+y위치 지정

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2") #버튼의 공간을 추가 확장, 가변크기(여백)
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=5, text="버튼4") #버튼의 크기를 지정, 고정크기
btn4.pack()

btn5 = Button(root, fg = "red", bg="yellow", text="버튼5") #fg : 글자 색, bg : 버튼 색
btn5.pack()

photo = PhotoImage(file="img.png")
btn6 = Button(root, image = photo) #그림판 이미지를 버튼모양으로 지정
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작버튼", command=btncmd) #버튼이 클릭되었을 시 동작 수행
btn7.pack()


root.mainloop()
