# make-an-.exe-by-python
用python制作带图形界面的 .exe
## 模块版本
altgraph                  0.17.2  
future                    0.18.2  
numpy                     1.22.3  
pandas                    1.4.2  
pefile                    2021.9.3  
pip                       22.0.4  
pyinstaller               4.10  
pyinstaller-hooks-contrib 2022.3  
python-dateutil           2.8.2  
pytz                      2022.1  
pywin32-ctypes            0.2.0  
setuptools                61.0.0  
six                       1.16.0  
wheel                     0.37.1  

本人用的是虚拟环境打包，所以python比较干净，部分包需要下载。

## 下载和打包说明

#### 1.下载必须的包
- pip install pyinstall  
- pip install pipenv  
#### 2.启用虚拟环境
- pipenv install
#### 3.进入虚拟环境
- pipenv shell
#### 4.打包你的程序
- pyinstaller -F -w xxx.py (-F可不加，这样打开.exe会快一点。-w是去掉命令窗口）
