# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:15:25 2023

@author: colin.guirardel
"""

import sys
import PyQt5 as qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import numpy as np
import matplotlib.pyplot as plt

from guira_slider import Slider
from guira_onglets import Ong_Carte # Ong_Age, Ong_Ath, Ong_Rech





class MaFenetre(QTabWidget):
    def __init__(self):
        super().__init__()
        height = 400
        width = 500
        self.resize(width,height)
        self.setWindowIcon(QIcon('images/Olympy.png'))
        self.setWindowTitle("Olympy")

        layoutV0 = QVBoxLayout()

        ong2=Ong_Carte("Work in progress...")
        ong1=Ong_Test("1")
        self.addTab(ong1,'Onglet 1')
        self.addTab(ong2,'Carte')



class Ong_Test(QWidget):
    def __init__(self,numTab):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel('Ceci est l\'onglet '+ numTab)
        slider = slider()

        layout.addStretch()
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(slider)
        self.setLayout(layout)





def main():
    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    fenetre.show()
    app.exec()

if __name__ == '__main__':
    main()