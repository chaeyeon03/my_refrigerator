from tkinter import *
from datetime import datetime

window = Tk()  # 윈도우 생성
window.title("나만의 냉장고")
window.geometry("300x500")
window.configure(background='azure')

list=[[]]

#음식, 유통기한을 입력하는 함수
def input_food():
    top1 = Toplevel()
    top1.title('음식의 유통기한 입력하기')
    top1.geometry("330x160")
    l1 = Label(top1, text = "음식을 입력하세요")
    l2 = Label(top1, text = "수량을 입력하세요")
    l3 = Label(top1, text = '유통기한을 입력하세요')
    l1.place(x=10,y=10)
    l2.place(x=10,y=40)
    l3.place(x=10,y=70)
    global e1
    e1 = Entry(top1)
    global e2
    e2 = Entry(top1)
    global e3
    e3 = Entry(top1)
    e1.place(x=150,y=10)
    e2.place(x=150,y=40)
    e3.place(x=150,y=70)
    b3 = Button(top1, text="입력완료", font=('맑은고딕','10'),command=input_done)
    b3.place(x=130,y=110)

def refrigerator():
    top2=Toplevel()
    top2.title("냉장고 안")
    top2.geometry("500x500")
    l1 = Label(top2, text = list)
    l1.pack()
    
def input_done():
    global food
    food = e1.get()
    global expiration_date 
    expiration_date = e3.get()
    global num
    num = e2.get()
    list.append((food,num,expiration_date))

def trash():
    top3=Toplevel()
    top3.title("유통기한 지난 음식")
    top3.geometry("500x500")
    
#현재 날짜와 유통기한 비교하는 함수
def compare_date():
    now = datetime.now()
    date_to_compare = datetime.strptime(expiration_date,"%Y%m%d")
    date_diff = date_to_compare - now


b1 = Button(window, text = "음식 추가",font=('맑은고딕','12'), command=input_food)
b1.place(x=110,y=180)

b2 = Button(window, text='냉장고 안', font=('맑은고딕','12'), command=refrigerator)
b2.place(x=110,y=242.5)

b3 = Button(window, text='추천 음식', font=('맑은고딕','12'))
b3.place(x=110,y=305)

photo = PhotoImage(file='bin (1).png')
b4 = Button(window, image = photo,  width=40, height=40)
b4.place(x=240,y=440)

window.mainloop()





