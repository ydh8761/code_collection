import tkinter as tk
from tkinter import ttk

def buildGUI():
    s=ttk.Style()
    s.configure('WR.TLabel',
                foreground='white',
                background='red',
                font=('맑은 고딕',20))
    
    text_label1=ttk.Label(win,text='안녕하세요', style='WR.TLabel')

    text_label2=ttk.Label(win)
    text_label2.configure(text='반가워요', style='WR.TLabel')

    text_label1.pack()
    text_label2.pack()

win=tk.Tk()
win.title("라벨 위젯 예시1")
buildGUI()
win.mainloop()