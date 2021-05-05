# -*- coding: utf-8 -*-
"""
Created on Sun May  2 20:15:48 2021

@author: joe
"""
import matplotlib.pyplot as plt
import sys


import matplotlib
import matplotlib.pyplot
import matplotlib.image as img
import numpy as np
import matplotlib.pylab

from PyQt5 import QtWidgets, uic
import requests
 
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('showimageui.ui', self)
        self.show()
    def do(self):
        url = 'https://www.sws.bom.gov.au/Images/HF%20Systems/Global%20HF/Ionospheric%20Map/WorldIMap.gif'
        myfile = requests.get(url)
 
        open('color.gif', 'wb').write(myfile.content)
        
        lena =img.imread('color.gif') # 讀取和程式碼處於同一目錄下的 lena.png
# 此時 lena 就已經是一個 np.array 了，可以對它進行任意處理
        lena.shape #(512, 512, 3)
        plt.imshow(lena) # 顯示圖片
        plt.axis('off') # 不顯示座標軸
        plt.show()
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()