
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


from Modules_Graphiques.guira_slider import Slider
from DATA.guira_extract import liste_sports


## placeholders

from numpy.random import randint

def placeholder_histogram(N,sport_ID):
    h = randint(16,30,N)
    return h

## Widgets

class ComboBox_Sports(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItems(liste_sports)


## Onglets
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
        self.refresh_button.clicked.connect(self._update_canvas)

        layoutV = QVBoxLayout()
        layoutV.addStretch(10)
        layoutV.addWidget(label2)
        layoutV.addStretch(1)
        layoutV.addWidget(self.sport1)
        layoutV.addWidget(self.sport2)
        layoutV.addWidget(self.sport3)
        layoutV.addStretch(2)
        layoutV.addWidget(self.refresh_button)
        layoutV.addStretch(10)


        label = QLabel("Histogramm : Coming soon...")

        self.canvas = FigureCanvasQTAgg(Figure(figsize=(10,10)))
        self.ax = self.canvas.figure.subplots()

        self.layout_specific.addStretch()
        self.layout_specific.addLayout(layoutV)
        #self.layout_specific.addStretch()
        self.layout_specific.addWidget(self.canvas)
        self.layout_specific.addStretch()

        self.setLayout(self.layout_generic)
        self._update_canvas()
    def _update_canvas(self):

        self.ax.clear()
        id_sport = [[self.sport1,self.sport2,self.sport3][i].currentIndex()for i in range(3)]
        N_hist = 3-id_sport.count(0)

        for i in range(3):
            if id_sport[i] != 0:
                hist_data = placeholder_histogram(1000,id_sport[i])
                self.ax.hist(hist_data,alpha = 1/N_hist, label = liste_sports[id_sport[i]])
        self.ax.legend()
        self.canvas.draw()



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


