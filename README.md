## 模块版本
altgraph                   0.17.2  
future                     0.18.2  
numpy                      1.22.3  
pandas                     1.4.2  
pefile                     2021.9.3  
pip                        22.0.4  
pyinstaller                4.10  
pyinstaller-hooks-contrib  2022.3  
python-dateutil            2.8.2  
pytz                       2022.1  
pywin32-ctypes             0.2.0  
setuptools                 61.0.0  
six                        1.16.0  
wheel                      0.37.1  

本人用的是虚拟环境打包，所以python比较干净，部分包需要下载。

## 下载和打包说明

#### 1.下载必须的包
- pip install pyinstaller   
- pip install pipenv  
#### 2.启用虚拟环境
- pipenv install
#### 3.进入虚拟环境
- pipenv shell
#### 4.打包你的程序
- pyinstaller -F -w xxx.py (-F可不加，这样打开.exe会快一点。-w是去掉命令窗口）

## 图形界面
这部分代码主要是设置图形界面大小，控件位置等等

```python
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
```
## 备注
![image](https://github.com/myy258/make-an-.exe-by-python/blob/main/Screenshot%202022-04-07%20163833.png)  
该脚本只是本人练习使用，功能比较简陋。
