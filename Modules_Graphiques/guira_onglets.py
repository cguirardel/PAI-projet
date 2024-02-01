if __name__ == "__main__":
    from Olym import main
    main()

## Imports


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


from Modules_Graphiques.guira_slider import Slider

from Modules_Traitement.guira_extract import liste_sports
from Modules_Traitement.traitementV11012024 import compteMedailles, constructionCarte, recherche, olympics, countries, correspondances

# import geopandas as gpd
# import pandas as pd


## placeholders

need_placeholders = True

if need_placeholders :
    from numpy.random import randint
    from numpy import NaN

    def placeholder_histogram(N,sport_ID,start_year,end_year,saison):
        #print(start_year,end_year,saison)
        h = randint(16,30,N)
        return h


    def placeholder_table() :
        pass


    def placeholder_map():
        countries.MEDALS = randint(0,100,countries.shape[0])
        countries.loc[4,'MEDALS'] = NaN
## Widgets

class ComboBox_Sports(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItems(liste_sports)




class pandasTableModel_Medal(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data
    def rowCount(self, parent=None):
        return self._data.shape[0]
    def columnCount(self, parnet=None):
        return self._data.shape[1]+1
    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                if index.column() == 0 :
                    return str(self._data.index[index.row()])
                else : return str(self._data.iloc[index.row(), index.column()-1])
        return None
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if col == 0 : return 'NOC'
            return self._data.columns[col-1]
        return None


class pandasTableModel_Rech(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data
    def rowCount(self, parent=None):
        return self._data.shape[0]
    def columnCount(self, parnet=None):
        return self._data.shape[1]
    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None




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
        self.ax, self.cax = self.canvas.figure.subplots(1,2,gridspec_kw={'width_ratios':[20,1]})
        #self.cax = self.canvas.figure.subplots(1,2,2)


        # Creating a QTableView
        self.tableau_medailles =  QTableView()


        #self.layout_specific.addStretch()
        self.layout_specific.addWidget(self.canvas)
        #self.layout_specific.addStretch()
        self.layout_specific.addWidget(self.tableau_medailles)
        #self.layout_specific.addStretch()
        self.setLayout(self.layout_generic)

        self.slider.slider.sliderReleased.connect(self._update)
        self.slider.box_saison.currentIndexChanged.connect(self._update)

        self._update()

    def _update(self):
        self._update_table()
        self._update_map()
    def _update_table(self):

        start_year,end_year = self.slider.slider.sliderPosition()
        saison = self.slider.box_saison.currentIndex() #0->tous, 1-> été, 2 -> Hiver

        data_gold = compteMedailles(olympics, 'NOC', start_year, end_year, edition = saison, medal_type='Gold')
        data_silver = compteMedailles(olympics, 'NOC', start_year, end_year, edition = saison, medal_type='Silver')
        data_bronze = compteMedailles(olympics, 'NOC', start_year, end_year, edition = saison, medal_type='Bronze')

        data = data_gold.merge(right = data_silver, on = 'NOC', how = 'outer')
        data = data.merge(right = data_bronze, on = 'NOC', how = 'outer')
        data = data.rename(columns={"Medal_x":"Or" , "Medal_y":"Argent", "Medal":"Bronze"})
        data.sort_values(by = ["Or","Argent","Bronze"],ascending=False, inplace=True)
        data[data.isna()] = 0
        data = data.astype('int32')
        # Getting the Model
        self.model = pandasTableModel_Medal(data)
        self.tableau_medailles.setModel(self.model)
    def _update_map(self):
        self.ax.clear()
        self.cax.clear()
        placeholder_map()
        missing_kwds = dict(color='grey', label='No Data')

        start_year,end_year = self.slider.slider.sliderPosition()
        saison = self.slider.box_saison.currentIndex() #0->tous, 1-> été, 2 -> Hiver

        data = constructionCarte(olympics, countries, start_year,end_year,saison)
        data.plot(ax=self.ax, column = 'Medal', legend=True,missing_kwds=missing_kwds, cax=self.cax)
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

        self.label = QLabel("Onglet PIB : Coming very soon... or not at all")
        self.layout_specific.addStretch()
        self.layout_specific.addWidget(self.label)
        self.layout_specific.addStretch()
        self.setLayout(self.layout_generic)



class Ong_Rech(Onglet_generique):
    def __init__(self):
        super().__init__()

        self.slider.slider.sliderReleased.connect(self.search)
        self.slider.box_saison.currentIndexChanged.connect(self.search)

        self.label = QLabel("Onglet Recherche : Coming soon...")
        label_name = QLabel("Nom :")
        label_NOC = QLabel("NOC du pays :")
        label_sport = QLabel("Sport :")

        button_search = QPushButton("Rechercher")
        button_search.clicked.connect(self.search)

        self.textbox_name = QLineEdit()
        self.textbox_NOC = QLineEdit()
        self.textbox_sport = QLineEdit()

        self.tableau_recherche =  QTableView()

        layoutV = QVBoxLayout()
        #layoutV.addStretch()
        layoutV.addWidget(label_name)
        layoutV.addWidget(self.textbox_name)

        layoutV.addStretch()
        layoutV.addWidget(label_NOC)
        layoutV.addWidget(self.textbox_NOC)

        layoutV.addStretch()
        layoutV.addWidget(label_sport)
        layoutV.addWidget(self.textbox_sport)
        layoutV.addStretch()

        layoutV.addWidget(button_search)
        #layoutV.addStretch()

        #self.layout_specific.addStretch()
        self.layout_specific.addLayout(layoutV)
        #self.layout_specific.addStretch()
        self.layout_specific.addWidget(self.tableau_recherche)
        #self.layout_specific.addStretch()
        self.setLayout(self.layout_generic)

        self.search()

    def search(self):
        start_year,end_year = self.slider.slider.sliderPosition()
        saison = self.slider.box_saison.currentIndex() #0->tous, 1-> été, 2 -> Hiver

        nameValue = self.textbox_name.text()
        NOCValue = self.textbox_NOC.text()
        sportValue = self.textbox_sport.text()
        data = recherche(olympics, start_year, end_year, saison, nameValue=nameValue, NOCValue=NOCValue, sportValue=sportValue)

        self.model = pandasTableModel_Rech(data)
        self.tableau_recherche.setModel(self.model)

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