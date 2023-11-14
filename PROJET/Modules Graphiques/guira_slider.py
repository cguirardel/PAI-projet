
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from superqt import QRangeSlider

class Slider(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        self.box_saison = QComboBox()
        self.box_saison.addItem("Tous les jeux")
        self.box_saison.addItem("Jeux d'été uniquement")
        self.box_saison.addItem("Jeux d'hiver uniquement")
        
        self.box_saison.setFixedWidth(100)
        
        self.slider = QRangeSlider(Qt.Horizontal)
        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(4)
        self.slider.setSingleStep(1)
        self.slider.setMaximum(2016)
        self.slider.setMinimum(1996)
        self.slider.setValue((1996, 2016))
        self.slider.valueChanged.connect(self.update_label)
        
        self.label = QLabel()
        self.update_label()
        
        
        layout.addWidget(self.box_saison)
        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        
        
        self.setLayout(layout)
    
    def update_label(self):
        start = self.slider.value()[0] 
        stop = self.slider.value()[1] 
        s = f'De {start} à {stop}'
        self.label.setText(s)


