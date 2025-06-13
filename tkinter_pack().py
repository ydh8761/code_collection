import tkinter as tk
from tkinter import ttk

def buildGUI():
    btn1=ttk.Button(win,text='버튼1')
    btn2=ttk.Button(win,text='버튼2')
    btn3=ttk.Button(win,text='버튼3')
    btn4=ttk.Button(win,text='버튼4')
    btn5=ttk.Button(win,text='버튼5')

    btn1.pack(ipadx=10,ipady=10)
    btn2.pack()
    btn3.pack(padx=10,pady=10)
    btn4.pack(fill=tk.X)
    btn5.pack(fill=tk.X,padx=10,pady=10,ipadx=10,ipady=10)

win=tk.Tk()
win.title('pack() 배치의 예')
win.geometry('300x200')
buildGUI()
win.mainloop()