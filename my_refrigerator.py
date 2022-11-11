from tkinter import *
from datetime import datetime

window = Tk()  # 윈도우 생성
window.title("나만의 냉장고")
window.geometry("300x500")
window.configure(background='azure')

now = datetime.now()

foodlist=[]
date_expired_list=[]
erase_foodlist=[]
update_erase_food=[]

def input_food(): #음식, 개수, 유통기한을 입력하는 함수
    top1 = Toplevel()
    top1.title('음식의 유통기한 입력하기')
    top1.geometry("330x160")

    l1= Label(top1, text = "음식을 입력하세요") 
    l2 = Label(top1, text = "수량을 입력하세요")
    l3 = Label(top1, text = '유통기한을 입력하세요')

    l1.place(x=10,y=10)
    l2.place(x=10,y=40)
    l3.place(x=10,y=70)

    global e_input_food #음식 입력 엔트리
    e_input_food = Entry(top1)
    global e_input_num #수량 입력 엔트리
    e_input_num = Entry(top1)
    global e_input_expiration_date #유통기한 입력 엔트리
    e_input_expiration_date = Entry(top1)

    e_input_food.place(x=150,y=10)
    e_input_num.place(x=150,y=40)
    e_input_expiration_date.place(x=150,y=70)

    b3 = Button(top1, text="입력완료", font=('맑은고딕','10'),command=input_done) #입력완료버튼. 누르면 input_done이 실행됨
    b3.place(x=130,y=110)

def refrigerator():
    top1=Toplevel()
    top1.title("냉장고 안")
    top1.geometry("500x500")
    foodlist.sort(key=lambda x: x[2])

    def warning_message(): #유통기한까지 남은 일수에 따라 나타나는 경고 메세지
        for i in range(0,len(foodlist)):
            if(foodlist[i][2]<0):
                foodMsglabel = Label(top1,text=(foodlist[i],"유통기한이 지났군요!! 먹으면 위험할 듯한데..."),fg = "dark red")
                foodMsglabel.pack()
            elif(foodlist[i][2]<=2):
                foodMsglabel = Label(top1,text=(foodlist[i],"유통기한이 얼마 안 남았어요!! 얼른 드시길..."),fg = "coral")
                foodMsglabel.pack()
            elif(foodlist[i][2]<=5):
                foodMsglabel = Label(top1,text=(foodlist[i],"조만간 드셔야겠네요!^^"),fg = "dark green")
                foodMsglabel.pack()
            else:
                foodMsglabel = Label(top1,text=(foodlist[i],"유통기한이 넉넉하네요!! 먹고 싶을 때 드세요~^^"))
                foodMsglabel.pack()
    
    warning_message()

 
def input_done(): #입력된 음식, 개수, 남은 일수를 리스트에 저장하는 함수 
    global food
    food = e_input_food.get()
    global expiration_date 
    expiration_date = e_input_expiration_date.get()
    global date_to_compare
    global num
    num = e_input_num.get()

    date_to_compare = datetime.strptime(expiration_date,"%Y%m%d")
    global date_diff
    date_diff = date_to_compare - now
    
    foodlist.append([food,num,date_diff.days+1])

def expired_date_food(): #유통기한이 지난 음식을 date_expired_list에 저장하는 함수
    top1=Toplevel()
    top1.title("유통기한 지난 음식")
    top1.geometry("300x300")
    for i in range(0,len(foodlist)):
        if(foodlist[i][2]<0):
            if(foodlist[i] in date_expired_list):
                continue
            else :
                date_expired_list.append(foodlist[i])
        date_expired_list.sort(key=lambda x:x[2])
    
    global listbox
    listbox = Listbox(top1, selectmode = 'extended')
    for i in range (0, len(date_expired_list)):
        listbox.insert(i,date_expired_list[i])
    listbox.pack()

    btn = Button(top1, text ="삭제",command = delete_anchor)
    btn.pack()

    
def delete_anchor():
    a = listbox.get(ANCHOR)
    update_erase_food.append(list(a))
    print(update_erase_food)
    global date_expired_list
    for i in range(0, len(update_erase_food)):
        if update_erase_food[i] in date_expired_list:
           date_expired_list.remove(update_erase_food[i])
           foodlist.remove(update_erase_food[i])
           
            
        
def erase_food(): #먹은 음식의 이름, 수량을 입력하는 함수
    top1=Toplevel()
    top1.title("먹은 음식 지우기")
    top1.geometry("330x160")

    l1 = Label(top1, text = "음식을 입력하세요") 
    l2 = Label(top1, text = "수량을 입력하세요")

    l1.place(x=10,y=10)
    l2.place(x=10,y=40)

    global e_erase_food
    e_erase_food = Entry(top1)
    global e_erase_num
    e_erase_num = Entry(top1)

    e_erase_food.place(x=150,y=10)
    e_erase_num.place(x=150,y=40)

    b3 = Button(top1, text="입력완료", font=('맑은고딕','10'),command = erase_done) #erase_done이 실행됨
    b3.place(x=130,y=110)

def erase_done(): #erase_food에서 입력된 음식과 수량만큼 foodlist에서 빼줌. 만약 다 먹었으면 foodlist에서 제외
    global erase_food
    erase_food = e_erase_food.get()
    global erase_num
    erase_num = e_erase_num.get()

    erase_foodlist.append([erase_food,erase_num])

    for i in range(0,len(foodlist)):
        for j in range(0,len(erase_foodlist)):
            if(foodlist[i][0]==erase_foodlist[j][0]):
                foodlist[i][1] = int(foodlist[i][1])-int(erase_foodlist[j][1])
                if(foodlist[i][1]==0):
                  del foodlist[i]

#'음식 추가' 버튼
b1 = Button(window, text = "음식 추가",font=('맑은고딕','12'), command=input_food)
b1.place(x=110,y=140)

#'냉장고 안' 버튼
b2 = Button(window, text='냉장고 안', font=('맑은고딕','12'), command=refrigerator)
b2.place(x=110,y=202.5)

#'추천 음식' 버튼
b3 = Button(window, text='추천 음식', font=('맑은고딕','12'))
b3.place(x=110,y=265)

#쓰레기통 버튼
photo = PhotoImage(file='bin (1).png')
b4 = Button(window, image = photo,  width=40, height=40, command = expired_date_food)
b4.place(x=240,y=440)

#음식 삭제 버튼
b_erase_food = Button(window, text = "음식 삭제", font=('맑은고딕','12'), command = erase_food)
b_erase_food.place(x=110,y=327.5)

window.mainloop()





