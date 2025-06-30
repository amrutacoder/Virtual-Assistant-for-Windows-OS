
from JarvisUi import Ui_JarvisUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
import Main1
import os
import webbrowser as web
import sys


# class Main1Thread(QThread):

#     def __init__(self):

#         super(Main1Thread, self).__init__()

#     def run(self):
#         Main1.TaskExe()


# startExe = Main1Thread()

class MainThread(QThread):

    def __init__(self):

        super(MainThread, self).__init__()

    def run(self):
        print("Running Main Thread")
        Main1.TaskExe()


startExe = MainThread()


class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.gui = Ui_JarvisUi()
        self.gui.setupUi(self)

        self.gui.pushButton_start.clicked.connect(self.startTask)
        self.gui.pushButton_exit.clicked.connect(self.close)
        self.gui.pushButton_chrome.clicked.connect(self.chrome_app)
        self.gui.pushButton_whatsapp.clicked.connect(self.whatsapp_app)
        self.gui.pushButton_youtube.clicked.connect(self.yt_app)

    def chrome_app(self):
        os.startfile(
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    def yt_app(self):
        web.open("https://www.youtube.com/")

    def whatsapp_app(self):
        web.open("https://web.whatsapp.com/")

    def startTask(self):

        self.gui.lable1 = QtGui.QMovie("GUI matrials/pIron_Template_9.gif")
        self.gui.Gif_1.setMovie(self.gui.lable1)
        self.gui.lable1.start()

        self.gui.lable2 = QtGui.QMovie("GUI matrials/live.gif")
        self.gui.Gif_2.setMovie(self.gui.lable2)
        self.gui.lable2.start()

        self.gui.lable3 = QtGui.QMovie("GUI matrials/Ntuks.gif")
        self.gui.Gif_3.setMovie(self.gui.lable3)
        self.gui.lable3.start()

        self.gui.lable4 = QtGui.QMovie("GUI matrials/Earth_Template.gif")
        self.gui.Gif_4.setMovie(self.gui.lable4)
        self.gui.lable4.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        startExe.start()

    def showTimeLive(self):
        t_ime = QTime.currentTime()
        time = t_ime.toString()
        d_ate = QDate.currentDate()
        date = d_ate.toString()
        lable_time = "Time :" + time
        lable_date = "Date :" + date

        self.gui.Test_Time.setText(lable_time)
        self.gui.Test_Day.setText(lable_date)


GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()

exit(GuiApp.exec_())
