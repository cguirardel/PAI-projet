
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from guira_slider import Slider

class Onglet_generique(QWidget):
    def __init__(self):
        super().__init__()
        self.layout_generic = QVBoxLayout()
        self.layout_specific = QHBoxLayout()
        slider = Slider()
        self.layout_generic.addStretch()
        self.layout_generic.addLayout(self.layout_specific)
        self.layout_generic.addStretch()
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

        self.label = QLabel("Onglet Ages : Coming very soon...")
        self.layout_specific.addStretch()
        self.layout_specific.addWidget(self.label)
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

