import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *   #서브모듈은 따로 import 해주지 않음
from tkinter import filedialog   #서브모듈
from PIL import Image

root = Tk()
root.title("kyongmin GUI")
root.geometry("480x600+100+200") #가로x세로+x위치+y위치 지정
root.resizable(False, False)

#파일추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", filetypes=(("PNG파일", "*.png"), ("모든 파일","*.*")), \
    initialdir=r"C:\Users") #r: \와 같은 탈출문자 상관없이 그대로 사용하겠다는 의미

    for file in files:
        list_file.insert(END, file)


#파일 삭제
def del_file():

    for index in reversed(list_file.curselection()): #reverse : 주소 참조(실제값 영향o), 내장함수 reversed : 값 참조(실제값 영향x) 
        list_file.delete(index) #curselection :현재 선택한 정보의 인덱스값을 리스트형태로 반환

#저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected =="": #사용자가 취소를 누를 때
        return
    txt_dest_path.delete(0, END) #엔트리는 (0,END) 텍스트는 (1.0, END)
    txt_dest_path.insert(0, folder_selected)

#이미지 통합
def marge_image():
    images = [Image.open(x) for x in list_file.get(0, END)]
    width = [x.size[0] for x in images] #size[0] : width
    height = [x.size[1] for x in images] #size[1] : height

    # 최대 넓이, 전체 높이
    max_width, total_height = max(width), sum(height)

    result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255)) #배경 흰색
    y_offset = 0 #y 위치정보

    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1] #height 만큼 더해줌

        progress = (idx + 1) / len(images) * 100 #실제 퍼센트 계산(완료 개수 / 전체 이미지 개수)
        p_Var.set(progress)
        progress_bar.update()

    dest_path = os.path.join(txt_dest_path.get(), "phtoto.jpg")
    result_img.save(dest_path)
    msgbox.showinfo("알림", "작업이 완료되었습니다.")



#시작
def start():
    #옵션들 확인
    print("가로 넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포멧 : ", cmb_format.get())

    #파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요!")

    #저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요!")

    marge_image()






#파일 프레임
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일 추가", command=add_file) #width 는 버튼 여백크기 지정
btn_add_file.pack(side = "left", padx=5, pady=5)

btn_del_file = Button(file_frame,padx=5, pady=5, width=12, text = "선택 삭제", command=del_file)
btn_del_file.pack(side = "right", padx=5, pady=5)


#리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)#fill="both" : 좌우로 프레임을 붙임

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand = scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


#저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로") #프레임 자체에 이름 지정
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)


#옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(fill="x", padx=5, pady=5, ipady=5)

    #가로넓이 옵션
lb_width = Label(frame_option, text="가로넓이", width=8)
lb_width.pack(side="left", padx=5, pady=5)

opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state = " readonly", values=opt_width, width=8)
cmb_width.current(0) #처음 값 지정
cmb_width.pack(side="left", padx=5, pady=5)

    #간격옵션
lb_space = Label(frame_option, text="간격", width=8)
lb_space.pack(side="left", padx=5, pady=5)

opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state = " readonly", values=opt_space, width=8)
cmb_space.current(0) #처음 값 지정
cmb_space.pack(side="left", padx=5, pady=5)

    #파일포멧옵션
lb_format = Label(frame_option, text="포멧", width=8)
lb_format.pack(side="left", padx=5, pady=5)

opt_format = ["png", "jpg", "bmp"]
cmb_format = ttk.Combobox(frame_option, state = " readonly", values=opt_format, width=8)
cmb_format.current(0) #처음 값 지정
cmb_format.pack(side="left", padx=5, pady=5)


#진행상황 프레임
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_Var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_Var)
progress_bar.pack(fill="x", padx=5, pady=5)


#실행프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)


btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)





root.mainloop()

