from tkinter import * #tkinter 에 있는 모든 페키지를 임포트 하겠다.

root = Tk()
root.title("kyongmin GUI") #제목 지정
root.geometry("640x480+100+200") #가로x세로+x위치+y위치 지정

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file = "img.png")
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text = "또만나요")

    global photo2 #garbage collectton은 불필요한 메모리를 정리해주는데 
    photo2 = PhotoImage(file = "img2.png") #이로부터 변수가 삭제되지 않도록 전역변수 설정을 해줌
    label2.config(image = photo2)


btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()
