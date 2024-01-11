
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


from Modules_Graphiques.guira_slider import Slider

from Modules_Traitement.guira_extract import liste_sports
from Modules_Traitement.traitementV11012024 import compteMedailles, olympics


import geopandas as gpd

## placeholders

from numpy.random import randint

def placeholder_histogram(N,sport_ID,start_year,end_year,saison):
    #print(start_year,end_year,saison)
    h = randint(16,30,N)
    return h


def placeholder_table() :
    pass

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

        self.label1 = QLabel("Carte : Coming soon...")
        self.label2 = QLabel("Tableau : Coming soon...")


        self.canvas = FigureCanvasQTAgg(Figure())
        self.ax = self.canvas.figure.subplots()

        self.tableau_medailles = QTableWidget()
        self.tableau_medailles.setRowCount(230)
        self.tableau_medailles.setColumnCount(4)
        horHeaders = ['NOC', 'Or','Argent','Bronze']
        self.tableau_medailles.setHorizontalHeaderLabels(horHeaders)
        self.tableau_medailles.resizeColumnsToContents()

        #self.layout_specific.addStretch()
        self.layout_specific.addWidget(self.canvas)
        #self.layout_specific.addStretch()
        self.layout_specific.addWidget(self.tableau_medailles)
        #self.layout_specific.addStretch()
        self.setLayout(self.layout_generic)

        self._update()

    def _update(self):
        self._update_table()
        self._update_map()
    def _update_table(self):
        pass
    def _update_map(self):
        self.ax.clear()
        countries = gpd.read_file('./Modules_Traitement/data/map')
        countries.plot(color="lightgrey",ax=self.ax)
        self.canvas.draw()



class Ong_Age(Onglet_generique):
    def __init__(self):
        super().__init__()

        label2 = QLabel("Selection sports :")
        self.sport1 = ComboBox_Sports()
        self.sport1.setCurrentIndex(1)
        self.sport2 = ComboBox_Sports()
        self.sport3 = ComboBox_Sports()

        self.slider.slider.sliderReleased.connect(self._update_canvas)
        self.slider.box_saison.currentIndexChanged.connect(self._update_canvas)

        self.sport1.currentIndexChanged.connect(self._update_canvas)
        self.sport2.currentIndexChanged.connect(self._update_canvas)
        self.sport3.currentIndexChanged.connect(self._update_canvas)



        layoutV = QVBoxLayout()
        layoutV.addStretch(10)
        layoutV.addWidget(label2)
        layoutV.addStretch(1)
        layoutV.addWidget(self.sport1)
        layoutV.addWidget(self.sport2)
        layoutV.addWidget(self.sport3)
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
        start_year,end_year = self.slider.slider.sliderPosition()
        saison = self.slider.box_saison.currentIndex() #0->tous, 1-> été, 2 -> Hiver

        hist_val = []
        hist_age = []

        for i in range(3):
            if id_sport[i] != 0:
                if id_sport[i] == 1: df =  olympics
                else : df = olympics[olympics.Sport==liste_sports[id_sport[i]]]
                #print(liste_sports[id_sport[i]])
                #print(df)
                ages = compteMedailles(df, 'Age', start_year, end_year, edition = saison)
                #print(ages)
                hist_val.append(list(ages.Medal))
                hist_age.append(list(ages.index))
        #print(hist_val)
        self.ax.hist(hist_age, weights = hist_val, label = [liste_sports[id_sport[i]] for i in range(3)])
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
    - Jeux Olympiques : https://www.kaggle.com/datasets/bhanupratapbiswas/olympic-data
    - Carte du monde : http//www.naturalearthdata.com/download/110m/cultural/ne_110m_admin_0_countries.zip

Bibilothèques utilisées :
    - PyQt5
    - pandas
    - geopandas
    - numpy
    - matplotlib
    - superqt
    - sys

Merci à celles et ceux qui les développent et les maintiennent !

Développement / Traitement : Gabriel Lecarme
Développement / Interface : Colin Guirardel"""))


        layoutV.addStretch()

        self.setLayout(layoutV)

