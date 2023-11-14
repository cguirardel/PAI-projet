
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from Modules_Graphiques.guira_slider import Slider
from DATA.guira_extract import sports


class Onglet_generique(QWidget):
    def __init__(self):
        super().__init__()
        self.layout_generic = QVBoxLayout()
        self.layout_specific = QHBoxLayout()
        slider = Slider()
        self.layout_generic.addStretch(10)
        self.layout_generic.addLayout(self.layout_specific)
        self.layout_generic.addStretch(10)
        self.layout_generic.addWidget(slider)
        self.setLayout(self.layout_generic)



class Ong_Carte(Onglet_generique):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Onglet Carte : Coming soon...")
        self.layout_specific.addStretch()
        self.layout_specific.addWidget(self.label)
        self.layout_specific.addStretch()
        self.setLayout(self.layout_generic)



class ComboBox_Sports(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItem('-')
        self.addItem('Tous sports confondu')
        self.addItems(sports)

class Ong_Age(Onglet_generique):
    def __init__(self):
        super().__init__()

        label = QLabel("Histogramme : Coming very soon...")

        label2 = QLabel("Selection sports :")
        self.sport1 = ComboBox_Sports()
        self.sport1.setCurrentIndex(1)
        self.sport2 = ComboBox_Sports()
        self.sport3 = ComboBox_Sports()
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.setStyleSheet("background-color: lightGray")


        layoutV = QVBoxLayout()
        layoutV.addWidget(label2)
        layoutV.addStretch()
        layoutV.addWidget(self.sport1)
        layoutV.addWidget(self.sport2)
        layoutV.addWidget(self.sport3)
        layoutV.addWidget(self.refresh_button)


        #self.canvas = FigureCanvasQTAgg
        label = QLabel("Histogramm : Comin soon...")

        self.layout_specific.addLayout(layoutV)
        self.layout_specific.addStretch()
        self.layout_specific.addWidget(label)
        self.layout_specific.addStretch()

        self.setLayout(self.layout_generic)








class Ong_PIB(Onglet_generique):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Onglet PIB : Coming very soon...")
        self.layout_specific.addStretch()
        self.layout_specific.addWidget(self.label)
        self.layout_specific.addStretch()
        self.setLayout(self.layout_generic)



class Ong_Rech(Onglet_generique):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Onglet Recherche : Coming less soon...")
        self.layout_specific.addStretch()
        self.layout_specific.addWidget(self.label)
        self.layout_specific.addStretch()
        self.setLayout(self.layout_generic)


