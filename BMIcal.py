import tkinter as tk
import tkinter.font as tkFont
import math
from PIL import ImageTk

class jiji(tk.Frame):
    shouldReset = True
    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createWidgets()


    def createWidgets(self):
        f1 = tkFont.Font(size = 32, family = "Courier New")
        f2 = tkFont.Font(size = 16, family = "Courier New")
        
        self.blank = tk.Label(self, text = None, height = 1, width = 4, font = f2)
        self.labheight = tk.Label(self, text = "身高（cm）", height = 1, width = 8, font = f2) 
        self.labweight = tk.Label(self, text = "體重（kg）", height = 1, width = 8, font = f2) 
        self.entheight = tk.Entry(self, show = None, font = f2)
        self.entweight = tk.Entry(self, show = None, font = f2)
        self.btncomfirm = tk.Button(self, text = "確定", height = 1, width = 8,command = self.clickcomfirm, font = f2) 
        self.labBMI = tk.Label(self, height = 2, width = 8, text = "BMI", font = f2)
        self.blank.grid(row = 1, column = 0)
        self.labheight.grid(row = 1, column = 1)
        self.labweight.grid(row = 2, column = 1)
        self.entheight.grid(row = 1, column = 2)
        self.entweight.grid(row = 2, column = 2)
        self.btncomfirm.grid(row = 3, column = 2)
        self.labBMI.grid(row = 1, column = 3, rowspan = 2)
        
    def clickcomfirm(self):
        try:
            height = float(self.entheight.get())
            weight = float(self.entweight.get())
            height *= 0.01
            height *= height
            BMI = round(float(weight / height), 2)
            self.labBMI.configure(text = BMI)
            self.shouldReset = True
        except:
            self.labBMI.configure(text = "請輸入數字")

cal = jiji()
cal.master.title("My jiji")
cal.mainloop()
