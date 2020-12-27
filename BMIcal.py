import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import math
from PIL import ImageTk


class base(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self) 
        page1()

class page1(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createWidgets()


    def createWidgets(self):
        f1 = tkFont.Font(size = 32, family = "Courier New")
        f2 = tkFont.Font(size = 16, family = "Courier New")
        
        self.radioValue = tk.IntVar()
        self.blank1 = tk.Label(self, text = None, height = 1, width = 4, font = f2)
        self.blank2 = tk.Label(self, text = None, height = 1, width = 4, font = f2)
        self.labage = tk.Label(self, text = "年齡（歲）", height = 1, width = 8, font = f2)
        self.labheight = tk.Label(self, text = "身高（cm）", height = 1, width = 8, font = f2) 
        self.labweight = tk.Label(self, text = "體重（kg）", height = 1, width = 8, font = f2) 
        self.labsex = tk.Label(self, text = "性別", height = 1, width = 11, font = f2)
        self.entage = tk.Entry(self, show = None, font = f2)
        self.entheight = tk.Entry(self, show = None, font = f2)
        self.entweight = tk.Entry(self, show = None, font = f2)
        self.radiomale = tk.Radiobutton(self,text="男", variable = self.radioValue, value = 1, font = f2)
        self.radiofemale = tk.Radiobutton(self,text="女", variable = self.radioValue, value = 2, font = f2)
        self.btncomfirm = tk.Button(self, text = "確定", height = 1, width = 8, command = self.clickcomfirm, font = f2) 
        self.labBMI = tk.Label(self, height = 2, width = 8, text = "BMI", font = f2)
        self.btnswitch = tk.Button(self, text = "下一步", height = 1, width = 8, command = self.clickswitch, font = f2)
        
        self.blank1.grid(row = 0, column = 0)
        self.labage.grid(row = 1, column = 1, sticky = tk.E)
        self.labsex.grid(row = 4, column = 1, sticky = tk.E)
        self.labheight.grid(row = 2, column = 1, sticky = tk.E)
        self.labweight.grid(row = 3, column = 1, sticky = tk.E)
        self.entage.grid(row = 1, column = 2)
        self.entheight.grid(row = 2, column = 2)
        self.entweight.grid(row = 3, column = 2)
        self.radiomale.grid(row = 4, column = 2, sticky = tk.W)
        self.radiofemale.grid(row = 4, column = 2, sticky = tk.E)
        self.btncomfirm.grid(row = 5, column = 2, sticky = tk.W)
        self.labBMI.grid(row = 2, column = 3, rowspan = 2)
        self.btnswitch.grid(row = 5, column = 2, sticky = tk.E)
        self.blank2.grid(row = 6, column = 0)
        
    def clickcomfirm(self):
        # try:
            age = int(self.entage.get())
            height = float(self.entheight.get())
            weight = float(self.entweight.get())
            sexual = self.radioValue.get()
            height *= 0.01
            height *= height
            BMI = round(float(weight / height), 2)
            if sexual == 0:
                self.labBMI.configure(text = "請選擇性別")
            else:
                self.labBMI.configure(text = BMI)
        # except:
            # self.labBMI.configure(text = "請輸入數字")
            
    def clickswitch(self):
        self.destroy()
        page2()   

class page2(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size = 32, family = "Courier New")
        f2 = tkFont.Font(size = 16, family = "Courier New")
        self.labDailyCal = tk.Label(self, text = "基礎代謝率              kcal", height = 1, width = 8, font = f2)
        self.labDailyCal = tk.Label(self, text = dailycal, height = 1, width = 8, font = f2)
        


cal = base()
cal.master.title("ya")
cal.mainloop()
