# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MusicPlayer(object):
    def setupUi(self, MusicPlayer):
        MusicPlayer.setObjectName("MusicPlayer")
        MusicPlayer.resize(1200, 720)
        self.centralwidget = QtWidgets.QWidget(MusicPlayer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.songsWidget = QtWidgets.QWidget(self.centralwidget)
        self.songsWidget.setObjectName("songsWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.songsWidget)
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.songsListView = QtWidgets.QListView(self.songsWidget)
        self.songsListView.setAlternatingRowColors(True)
        self.songsListView.setObjectName("songsListView")
        self.horizontalLayout_3.addWidget(self.songsListView)
        self.verticalLayout_2.addWidget(self.songsWidget)
        self.timerWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timerWidget.sizePolicy().hasHeightForWidth())
        self.timerWidget.setSizePolicy(sizePolicy)
        self.timerWidget.setMinimumSize(QtCore.QSize(0, 30))
        self.timerWidget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.timerWidget.setObjectName("timerWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.timerWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.currentTime = QtWidgets.QLabel(self.timerWidget)
        self.currentTime.setObjectName("currentTime")
        self.horizontalLayout_2.addWidget(self.currentTime)
        self.timeSlider = QtWidgets.QSlider(self.timerWidget)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.horizontalLayout_2.addWidget(self.timeSlider)
        self.totalTime = QtWidgets.QLabel(self.timerWidget)
        self.totalTime.setObjectName("totalTime")
        self.horizontalLayout_2.addWidget(self.totalTime)
        self.verticalLayout_2.addWidget(self.timerWidget)
        self.controlsWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlsWidget.sizePolicy().hasHeightForWidth())
        self.controlsWidget.setSizePolicy(sizePolicy)
        self.controlsWidget.setMinimumSize(QtCore.QSize(0, 60))
        self.controlsWidget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.controlsWidget.setObjectName("controlsWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.controlsWidget)
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.play_pausebtn = QtWidgets.QPushButton(self.controlsWidget)
        self.play_pausebtn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_pausebtn.sizePolicy().hasHeightForWidth())
        self.play_pausebtn.setSizePolicy(sizePolicy)
        self.play_pausebtn.setMinimumSize(QtCore.QSize(40, 40))
        self.play_pausebtn.setMaximumSize(QtCore.QSize(40, 40))
        self.play_pausebtn.setText("")
        self.play_pausebtn.setIconSize(QtCore.QSize(35, 35))
        self.play_pausebtn.setObjectName("play_pausebtn")
        self.horizontalLayout.addWidget(self.play_pausebtn)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.previousbtn = QtWidgets.QPushButton(self.controlsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousbtn.sizePolicy().hasHeightForWidth())
        self.previousbtn.setSizePolicy(sizePolicy)
        self.previousbtn.setMinimumSize(QtCore.QSize(30, 30))
        self.previousbtn.setMaximumSize(QtCore.QSize(30, 30))
        self.previousbtn.setText("")
        self.previousbtn.setIconSize(QtCore.QSize(25, 25))
        self.previousbtn.setObjectName("previousbtn")
        self.horizontalLayout.addWidget(self.previousbtn)
        self.stopbtn = QtWidgets.QPushButton(self.controlsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopbtn.sizePolicy().hasHeightForWidth())
        self.stopbtn.setSizePolicy(sizePolicy)
        self.stopbtn.setMinimumSize(QtCore.QSize(30, 30))
        self.stopbtn.setMaximumSize(QtCore.QSize(30, 30))
        self.stopbtn.setText("")
        self.stopbtn.setIconSize(QtCore.QSize(25, 25))
        self.stopbtn.setObjectName("stopbtn")
        self.horizontalLayout.addWidget(self.stopbtn)
        self.nextbtn = QtWidgets.QPushButton(self.controlsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextbtn.sizePolicy().hasHeightForWidth())
        self.nextbtn.setSizePolicy(sizePolicy)
        self.nextbtn.setMinimumSize(QtCore.QSize(30, 30))
        self.nextbtn.setMaximumSize(QtCore.QSize(30, 30))
        self.nextbtn.setText("")
        self.nextbtn.setIconSize(QtCore.QSize(25, 25))
        self.nextbtn.setObjectName("nextbtn")
        self.horizontalLayout.addWidget(self.nextbtn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.shufflebtn = QtWidgets.QPushButton(self.controlsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shufflebtn.sizePolicy().hasHeightForWidth())
        self.shufflebtn.setSizePolicy(sizePolicy)
        self.shufflebtn.setMinimumSize(QtCore.QSize(30, 30))
        self.shufflebtn.setMaximumSize(QtCore.QSize(30, 30))
        self.shufflebtn.setText("")
        self.shufflebtn.setIconSize(QtCore.QSize(25, 25))
        self.shufflebtn.setObjectName("shufflebtn")
        self.horizontalLayout.addWidget(self.shufflebtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.addDirbtn = QtWidgets.QPushButton(self.controlsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addDirbtn.sizePolicy().hasHeightForWidth())
        self.addDirbtn.setSizePolicy(sizePolicy)
        self.addDirbtn.setMinimumSize(QtCore.QSize(30, 30))
        self.addDirbtn.setMaximumSize(QtCore.QSize(30, 30))
        self.addDirbtn.setText("")
        self.addDirbtn.setIconSize(QtCore.QSize(25, 25))
        self.addDirbtn.setObjectName("addDirbtn")
        self.horizontalLayout.addWidget(self.addDirbtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.speakerbtn = QtWidgets.QPushButton(self.controlsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speakerbtn.sizePolicy().hasHeightForWidth())
        self.speakerbtn.setSizePolicy(sizePolicy)
        self.speakerbtn.setMinimumSize(QtCore.QSize(30, 30))
        self.speakerbtn.setMaximumSize(QtCore.QSize(30, 30))
        self.speakerbtn.setText("")
        self.speakerbtn.setIconSize(QtCore.QSize(25, 25))
        self.speakerbtn.setObjectName("speakerbtn")
        self.horizontalLayout.addWidget(self.speakerbtn)
        self.volumeSlider = QtWidgets.QSlider(self.controlsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeSlider.sizePolicy().hasHeightForWidth())
        self.volumeSlider.setSizePolicy(sizePolicy)
        self.volumeSlider.setMinimumSize(QtCore.QSize(200, 30))
        self.volumeSlider.setMaximumSize(QtCore.QSize(200, 30))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 25)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.volumeSlider.setTickInterval(0)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout.addWidget(self.volumeSlider)
        self.verticalLayout_2.addWidget(self.controlsWidget)
        MusicPlayer.setCentralWidget(self.centralwidget)

        self.retranslateUi(MusicPlayer)
        QtCore.QMetaObject.connectSlotsByName(MusicPlayer)

    def retranslateUi(self, MusicPlayer):
        _translate = QtCore.QCoreApplication.translate
        MusicPlayer.setWindowTitle(_translate("MusicPlayer", "Music Player"))
        self.currentTime.setText(_translate("MusicPlayer", "0:00"))
        self.totalTime.setText(_translate("MusicPlayer", "0:00"))
