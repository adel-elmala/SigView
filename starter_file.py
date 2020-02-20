from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
from design import Ui_MainWindow
import sys
import pyqtgraph as pg
import sys
import numpy as np


class ApplicationWindow(QtWidgets.QMainWindow):
    signal = list()
    cur = 0
    flag = 1
    ran = 50
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.pan)
        self.timer.start()
    
     
    
    def open_dialog_box(self):
        print("heelll")
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        signal = np.genfromtxt(path , delimiter=',')
        self.ui.plotWindow.plot(list(range(len(signal))), signal)
        self.ui.plotWindow.setXRange(self.cur, self.cur + self.ran)
    
    
    def pan(self):
        if not self.flag:
            self.ui.plotWindow.setXRange(self.cur, self.cur + self.ran)
            self.cur = self.cur + 0.1
    
    def play(self):
        self.flag = 0
        
    def pause(self):
        self.flag = 1
    
    def zoomin(self):
        self.ran = max(5, self.ran - 5)
        self.ui.plotWindow.setXRange(self.cur, self.cur + self.ran)
        
    def zoomout(self):
        self.ran = min(100, self.ran + 5)
        self.ui.plotWindow.setXRange(self.cur, self.cur + self.ran)
        
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.ui.Play.clicked.connect(application.play)
    application.ui.Stop.clicked.connect(application.pause)
    application.ui.Openfile.clicked.connect(application.open_dialog_box)
    application.ui.Zoomin.clicked.connect(application.zoomin)
    application.ui.Zoomout.clicked.connect(application.zoomout)
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()