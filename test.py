from tkinter import*

window = Tk()
window.title("test")
window.geometry("240x360")
window.resizable(width=TRUE,height=TRUE)


for i in range(0,10):
    label1=Label(window,text=(i,"'번째 테스트'" ))
    label1.pack()

window.mainloop()
