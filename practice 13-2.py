import tkinter as tk
from tkinter import ttk

class ConvTempWin():
    def __init__(self):
        self.win=tk.Tk()
        self.win.title("온도변환기-1단계")
        self.win.geometry('350x50')
        self.__buildGUI()

    def __buildGUI(self):
       
        fahr_Label=ttk.Label(self.win, text='화씨')

        self.__fahr=tk.IntVar()
        fahr_entry=ttk.Entry(self.win, justify=tk.RIGHT,
                         textvariable=self.__fahr, width=11)
    
        cel_Label=ttk.Label(self.win, text='섭씨')

        self.__cels=tk.DoubleVar()
        cel_entry=ttk.Entry(self.win, justify=tk.RIGHT,
                         textvariable=self.__cels, width=11)

        f2c_btn=ttk.Button(self.win, text='화씨->섭씨',
                         command=self.__f2c_handler)
        c2f_btn=ttk.Button(self.win, text='섭씨->화씨',
                            command=self.__c2f_handler)
    
        reset_btn=ttk.Button(self.win, text='초기화',
                            command=self.__reset_handler)
        quit_btn=ttk.Button(self.win, text='종료',
                            command=self.win.destroy)
    
    
        fahr_Label.grid(row=0, column=0,)
        fahr_entry.grid(row=0, column=1)
        cel_Label.grid(row=0, column=2)
        cel_entry.grid(row=0, column=3)

        f2c_btn.grid(row=1, column=0)
        c2f_btn.grid(row=1, column=1)
        reset_btn.grid(row=1, column=2)
        quit_btn.grid(row=1, column=3)

    def __f2c_handler(self):
        fahr=self.__fahr.get()
        cels=(fahr-32)*5/9
        self.__cels.set(f'{cels:.2f}')
    
    def __c2f_handler(self):
        cels=self.__cels.get()
        fahr=cels*9/5+32
        self.__fahr.set(f'{fahr:.2f}')
    
    def __reset_handler(self):
        self.__fahr.set('')
        self.__cels.set('')

    def start(self):
        self.win.mainloop()

tConverter=ConvTempWin()
tConverter.start()