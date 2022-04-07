from tkinter import *
import pandas as pd
from sys import exit
from tkinter.filedialog import asksaveasfilename

class GUI:
    def __init__(self):
        # 创建窗口
        self.root = Tk()
        # 标题
        self.root.title('Run')
        # 窗口大小
        self.root.geometry("550x170")
        # 窗口位置
        self.root.geometry("+300+200")
        
        self.path = StringVar()
        self.path.set(os.path.abspath("."))

        self.entry = Entry(self.root, textvariable=self.path, width=61)
        self.result = Text(self.root, width=45, height=5)
        self.result_button1 = Button(self.root, text='Run', command=self.find1, width=10, height=1)
        self.select_button = Button(self.root, text = "select path", command=self.selectPath)
        self.label1 = Label(self.root, text="Input Path")
        self.label2 = Label(self.root, text="Remark:Input Path must be a path like D:/file/test.csv",font=18,bg='red') 
        self.quit_button = Button(self.root, text='Quit', command=self.root.destroy, width=10, height=1)
        self.clear = Button(self.root, text='Delete', command=self.clear, width=10, height=1)
                
    def clear(self):
        for _ in range(100):
            self.result.delete(1.0)
     
    def selectPath(self):
        path_ = asksaveasfilename()
        if path_ == "":
            self.path.get()
        else:
            path_ = path_.replace("/", "\\")
            self.path.set(path_)
                
    def find1(self):
        self.result.insert(END, InputPath().getresult(self.entry.get()))

    def gui_arrang(self):
        
        self.entry.grid(rowspan=1, row=0, column=1, sticky=W, padx=1,pady=5)
        self.result_button1.grid(row=3, column=0, sticky=E, padx=5,pady=2)
        self.result.grid(rowspan=8, row=2, column=1)
        self.quit_button.grid(row=4, column=0,sticky=E, padx=5, pady=2)
        self.clear.grid(row=5, column=0, sticky=E, padx=5, pady=2)
        self.label1.grid(row=0, padx=5, pady=5) 
        self.label2.grid(row=20, column=1, sticky=W, padx=5, pady=2)
        self.select_button.grid(row=0, column=2, padx=1, pady=1)
        # self.entry.pack(expand=YES, side='left', fill='both')
        # self.result_button1.pack(expand=YES, side='top', fill='both')
        # self.result_button2.pack(expand=YES, side='bottom', fill='both')
        # self.result.pack(expand=YES, side='right', fill='both')


class InputPath:
    def __init__(self):
        pass

    def getresult(self, info):
        
        if ':/' in str(info) or ':' + '\\' in str(info):
            try:
                asD = pd.DataFrame([['AAAAA',800]],columns = ['WAFER','ini_capa_actual'])
                asD.to_csv(str(info))
                result = '完成'
                self.result = '完成'
                print('结果： ', result)
            except Exception as e:
                
                if len(info) == 0:
                    result = '请输入地址'
                    self.result = '请输入地址' 
                    print('结果： ', result)
                else:
                    result = '输入地址有误，请重新输入'
                    self.result = '输入地址有误，请重新输入' 
                    print('结果： ', result)
        else:
            result = '输入地址有误，请重新输入'
            self.result = '输入地址有误，请重新输入' 
            print('结果： ', result)
        
        return result


def main():
    fl = GUI()
    fl.gui_arrang()
    mainloop()
    pass

if __name__ == "__main__":
    main()