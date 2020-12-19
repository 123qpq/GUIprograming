from tkinter import * 


root = Tk()
root.title("kyongmin GUI") 
root.geometry("640x480+100+200")

listbox = Listbox(root, selectmode="extended", height=0) #single : 1개만 선택, extended : 여러개 선택
listbox.insert(0, "사과")                                   #height 가 0이면 다보여줌. 나머지 숫자는 그 개수만큼만 보여줌
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()



def btncmd():
    #listbox.delete(END) #0 : 맨 앞 항목 삭제,END : 맨 뒤 항목 삭제

    #print("리스트에는", listbox.size(), "개가 있어요") #개수 확인
    #print("1번째부터 3번째까지 항목 : ", listbox.get(0,2)) #항목 확인
    print("선택된 항목 확인 : ", listbox.curselection())




btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()