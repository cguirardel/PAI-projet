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

from Modules_Graphiques.guira_slider import Slider
from Modules_Graphiques.guira_onglets import Ong_Carte, Ong_Age, Ong_PIB, Ong_Rech, Ong_Cred


# This part changes taskbar icon for windows
import ctypes
myappid = 'Olympy.project' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class MaFenetre(QTabWidget):
    def __init__(self):
        super().__init__()
        height = 400
        width = 500
        #self.resize(width,height)
        self.setWindowIcon(QIcon('Modules_Graphiques/images/Olympy.png'))
        self.setWindowTitle("Olympy")

        layoutV0 = QVBoxLayout()

        ong_carte=Ong_Carte()
        ong_age=Ong_Age()
        ong_pib=Ong_PIB()
        ong_rech=Ong_Rech()
        ong_cred=Ong_Cred()

        # self.addTab(ong_carte,'Carte')
        self.addTab(ong_age,'Ages')
        self.addTab(ong_pib,'PIB')
        self.addTab(ong_rech,'Recherche')
        self.addTab(ong_cred,'Remerciements')







def main():
    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    fenetre.show()
    app.exec()

if __name__ == '__main__':
    main()