from tkinter import * 
import os

root = Tk()
root.title("제목없음 - Windows 메모장") 
root.geometry("640x480+100+200")

filename = "mynote.txt"

#menu
menu = Menu(root)


def open_file():
    if os.path.isfile(filename): #파일 있으면 true
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) #텍스트 본문 삭제
            txt.insert(END, file.read()) #파일내용 본문에 입력

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) #모든내용 가져와서 저장

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="새로 만들기")
menu_file.add_command(label="새 창")
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_command(label="다른 이름으로 저장")
menu_file.add_separator()
menu_file.add_command(label="페이지 설정")
menu_file.add_command(label="인쇄")
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)



menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")


root.config(menu=menu)

#scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side = "right", fill = "y")



#body
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side = "left", fill="both", expand=True) #공간 꽉꽉 채움

scrollbar.config(command=txt.yview)


root.mainloop()
