# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 389)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Openfile = QtWidgets.QPushButton(self.centralwidget)
        self.Openfile.setGeometry(QtCore.QRect(20, 10, 81, 51))
        self.Openfile.setObjectName("Openfile")
        self.plotWindow = PlotWidget(self.centralwidget)
        self.plotWindow.setGeometry(QtCore.QRect(5, 71, 481, 281))
        self.plotWindow.setObjectName("plotWindow")
        self.Play = QtWidgets.QPushButton(self.centralwidget)
        self.Play.setGeometry(QtCore.QRect(110, 10, 71, 51))
        self.Play.setObjectName("Play")
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(190, 10, 71, 51))
        self.Stop.setObjectName("Stop")
        self.Zoomin = QtWidgets.QPushButton(self.centralwidget)
        self.Zoomin.setGeometry(QtCore.QRect(270, 10, 71, 51))
        self.Zoomin.setObjectName("Zoomin")
        self.Zoomout = QtWidgets.QPushButton(self.centralwidget)
        self.Zoomout.setGeometry(QtCore.QRect(350, 10, 71, 51))
        self.Zoomout.setObjectName("Zoomout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Openfile.setText(_translate("MainWindow", "openfile"))
        self.Play.setText(_translate("MainWindow", "play"))
        self.Stop.setText(_translate("MainWindow", "stop"))
        self.Zoomin.setText(_translate("MainWindow", "zoom in"))
        self.Zoomout.setText(_translate("MainWindow", "zoom out"))

