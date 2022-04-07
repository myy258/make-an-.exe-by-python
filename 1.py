from tkinter import *
import pandas as pd
from sys import exit

class TranslateGUI:
    def __init__(self):
        # 创建窗口
        self.root = Tk()
        # 标题
        self.root.title('Run')
        # 窗口大小 小写的x
        self.root.geometry("500x200")
        # 窗口位置
        self.root.geometry("+300+200")

        self.entry = Entry(self.root, width=60)
        self.result = Text(self.root, width=45, height=5)
        self.result_button1 = Button(self.root, text='Run', command=self.find1, width=10, height=1)
        self.label1 = Label(self.root, text="Input Path")
        self.label2 = Label(self.root, text="Remark:Input Path must be a path like D:/file/test.csv",font=18,bg='red') 
        self.quit_button = Button(self.root, text='Quit', command=self.root.destroy, width=10, height=1)
        self.clear = Button(self.root, text='delete', command=self.clear, width=10, height=1)
                
    def clear(self):
        for _ in range(100):
            self.result.delete(1.0)
                     
    def find1(self):
        self.result.insert(END, InputPath().getresult(self.entry.get()))

    def gui_arrang(self):
        
        self.entry.grid(rowspan=1, row=0, column=1, sticky=E, padx=20,pady=5)
        self.result_button1.grid(row=3, column=0, sticky=E, padx=5,pady=2)
        self.result.grid(rowspan=8, row=2, column=1)
        self.quit_button.grid(row=4, column=0,sticky=E, padx=5, pady=2)
        self.clear.grid(row=5, column=0, sticky=E, padx=5, pady=2)
        self.label1.grid(row=0) 
        self.label2.grid(row=20, column=1, sticky=W, padx=5, pady=2)

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
    fl = TranslateGUI()
    fl.gui_arrang()
    mainloop()
    pass

if __name__ == "__main__":
    main()
