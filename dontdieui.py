# Form implementation generated from reading ui file 'dontdie.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 537)
        MainWindow.setMaximumSize(QtCore.QSize(936, 537))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(7, 7, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(7, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.LeftSide = QtWidgets.QVBoxLayout()
        self.LeftSide.setSpacing(0)
        self.LeftSide.setObjectName("LeftSide")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(15, -1, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.Image = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image.sizePolicy().hasHeightForWidth())
        self.Image.setSizePolicy(sizePolicy)
        self.Image.setMaximumSize(QtCore.QSize(64, 64))
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.horizontalLayout_10.addWidget(self.Image)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(24)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.LeftSide.addLayout(self.horizontalLayout_10)
        self.LeftTop = QtWidgets.QGridLayout()
        self.LeftTop.setContentsMargins(-1, -1, 0, -1)
        self.LeftTop.setSpacing(0)
        self.LeftTop.setObjectName("LeftTop")
        self.stopButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.stopButton.setObjectName("stopButton")
        self.LeftTop.addWidget(self.stopButton, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.LeftTop.addWidget(self.label, 0, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.startButton.setObjectName("startButton")
        self.LeftTop.addWidget(self.startButton, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.LeftTop.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(150, 75))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.LeftTop.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.LeftTop.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.LeftSide.addLayout(self.LeftTop)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(95, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(12)
        font.setKerning(True)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("")
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_4.addWidget(self.checkBox)
        self.LeftSide.addLayout(self.verticalLayout_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 6, -1, -1)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.console = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy)
        self.console.setMinimumSize(QtCore.QSize(0, 150))
        self.console.setMaximumSize(QtCore.QSize(16777215, 155))
        self.console.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.console.setObjectName("console")
        self.verticalLayout_7.addWidget(self.console)
        self.LeftSide.addLayout(self.verticalLayout_7)
        self.horizontalLayout_3.addLayout(self.LeftSide)
        spacerItem2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.RightSide = QtWidgets.QVBoxLayout()
        self.RightSide.setObjectName("RightSide")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(15)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.RightSide.addWidget(self.label_4)
        self.deathlist = QtWidgets.QListWidget(parent=self.centralwidget)
        self.deathlist.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(12)
        self.deathlist.setFont(font)
        self.deathlist.setProperty("isWrapping", False)
        self.deathlist.setObjectName("deathlist")
        self.RightSide.addWidget(self.deathlist)
        self.RightButtons = QtWidgets.QHBoxLayout()
        self.RightButtons.setObjectName("RightButtons")
        self.removeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.removeButton.setObjectName("removeButton")
        self.RightButtons.addWidget(self.removeButton)
        self.addButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.RightButtons.addWidget(self.addButton)
        self.resetButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.resetButton.setEnabled(True)
        self.resetButton.setObjectName("resetButton")
        self.RightButtons.addWidget(self.resetButton)
        self.RightSide.addLayout(self.RightButtons)
        self.horizontalLayout_3.addLayout(self.RightSide)
        spacerItem3 = QtWidgets.QSpacerItem(7, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minecraft Server Manager"))
        self.label_3.setText(_translate("MainWindow", " Don\'t Die v1.3"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Username</p></body></html>"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1.19.1+"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1.18-1.19"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Pre 1.18 (Not Tested)"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Game Version</p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "case-sensitive"))
        self.checkBox.setText(_translate("MainWindow", "Use User Death Message Triggers"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Console</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Customize Death Message Triggers</p></body></html>"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.resetButton.setText(_translate("MainWindow", "Reset List"))
