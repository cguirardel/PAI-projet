
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


from Modules_Graphiques.guira_slider import Slider

from Modules_Traitement.guira_extract import liste_sports
from Modules_Traitement.traitementV0 import compteMedailles, olympics


## placeholders

from numpy.random import randint

def placeholder_histogram(N,sport_ID,start_year,end_year,saison):
    print(start_year,end_year,saison)
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
        self.slider = Slider()
        self.layout_generic.addStretch(10)
        self.layout_generic.addLayout(self.layout_specific)
        self.layout_generic.addStretch(10)
        self.layout_generic.addWidget(self.slider)
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

        label2 = QLabel("Selection sports :")
        self.sport1 = ComboBox_Sports()
        self.sport1.setCurrentIndex(1)
        self.sport2 = ComboBox_Sports()
        self.sport3 = ComboBox_Sports()
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.setStyleSheet("background-color: lightGray")
        self.refresh_button.clicked.connect(self._update_canvas)

        self.slider.slider.sliderReleased.connect(self._update_canvas)

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


        self.canvas = FigureCanvasQTAgg(Figure())
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
                start_year,end_year = self.slider.slider.sliderPosition()
                saison = self.slider.box_saison.currentIndex() #0->tous, 1-> été, 2 -> Hiver
                hist_data = placeholder_histogram(1000,id_sport[i],start_year,end_year,saison)
                self.ax.hist(hist_data,alpha = 1/N_hist, label = liste_sports[id_sport[i]])
        self.ax.legend()
        self.ax.set_xlabel("Age")
        self.ax.set_ylabel("Médailles")
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


class Ong_Cred(QWidget):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap('Modules_Graphiques/images/Olympy.png')
        rect = QRect(0, 350, 18000, 1000)
        pixmap = pixmap.copy(rect)
        self.label_pic = QLabel()
        height_label = 300
        self.label_pic.resize(self.width(), height_label)

        layoutV = QVBoxLayout()


        self.label_pic.setPixmap(pixmap.scaled(self.label_pic.size(), Qt.KeepAspectRatio))

        layoutV.addStretch()
        layoutV.addWidget(QLabel("Ce logiciel a été réalisé avec Python dans le cadre d'un projet 3A à l'IOGS"))

        layoutV.addWidget(self.label_pic)
        layoutV.addWidget(QLabel(""))
        layoutV.addWidget(QLabel("""Les développeurs souhaitent remercier Oriane Koellsch pour le dessin du logo

Bases de données utilisées :
    - Jex Olympiques : https://www.kaggle.com/datasets/bhanupratapbiswas/olympic-data

Bibilothèques utilisées :
    - PyQt5
    - pandas
    - numpy
    - matplotlib
    - superqt
    - sys

Merci à celles et ceux qui les développent et les maintiennent !

Développement / Traitement : Gabriel Lecarme
Développement / Interface : Colin Guirardel"""))


        layoutV.addStretch()

        self.setLayout(layoutV)

