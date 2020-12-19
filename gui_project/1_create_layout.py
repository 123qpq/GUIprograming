import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("kyongmin GUI")
root.geometry("480x600+100+200") #가로x세로+x위치+y위치 지정
root.resizable(False, False)



#파일 프레임
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일 추가") #width 는 버튼 여백크기 지정
btn_add_file.pack(side = "left", padx=5, pady=5)

btn_del_file = Button(file_frame,padx=5, pady=5, width=12, text = "선택 삭제")
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

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
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
lb_space = ttk.Combobox(frame_option, state = " readonly", values=opt_space, width=8)
lb_space.current(0) #처음 값 지정
lb_space.pack(side="left", padx=5, pady=5)

    #파일포멧옵션
lb_format = Label(frame_option, text="포멧", width=8)
lb_format.pack(side="left", padx=5, pady=5)

opt_format = ["png", "jpg", "bmp"]
lb_format = ttk.Combobox(frame_option, state = " readonly", values=opt_format, width=8)
lb_format.current(0) #처음 값 지정
lb_format.pack(side="left", padx=5, pady=5)


#진행상황 프레임
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_Var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_Var)
progress_bar.pack(fill="x", padx=5, pady=5)


#실행프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)


btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12)
btn_start.pack(side="right", padx=5, pady=5)





root.mainloop()

