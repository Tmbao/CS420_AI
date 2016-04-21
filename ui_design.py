# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Tue Apr 19 06:49:14 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(235, 366)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(235, 366))
        MainWindow.setMaximumSize(QtCore.QSize(235, 366))
        self.widget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 40, 192, 68))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButtonRun = QtGui.QPushButton(self.widget)
        self.pushButtonRun.setGeometry(QtCore.QRect(70, 320, 98, 27))
        self.pushButtonRun.setObjectName(_fromUtf8("pushButtonRun"))
        self.splitter = QtGui.QSplitter(self.widget)
        self.splitter.setGeometry(QtCore.QRect(20, 150, 189, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_2 = QtGui.QLabel(self.splitter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEditMapFile = QtGui.QLineEdit(self.splitter)
        self.lineEditMapFile.setObjectName(_fromUtf8("lineEditMapFile"))
        self.splitter_2 = QtGui.QSplitter(self.widget)
        self.splitter_2.setGeometry(QtCore.QRect(10, 190, 212, 27))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.pushButtonEditMap = QtGui.QPushButton(self.splitter_2)
        self.pushButtonEditMap.setObjectName(_fromUtf8("pushButtonEditMap"))
        self.pushButtonMapFormat = QtGui.QPushButton(self.splitter_2)
        self.pushButtonMapFormat.setObjectName(_fromUtf8("pushButtonMapFormat"))
        self.splitter_3 = QtGui.QSplitter(self.widget)
        self.splitter_3.setGeometry(QtCore.QRect(0, 240, 226, 27))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.label_3 = QtGui.QLabel(self.splitter_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEditImageFile = QtGui.QLineEdit(self.splitter_3)
        self.lineEditImageFile.setObjectName(_fromUtf8("lineEditImageFile"))
        self.splitter_4 = QtGui.QSplitter(self.widget)
        self.splitter_4.setGeometry(QtCore.QRect(20, 270, 201, 27))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.label_4 = QtGui.QLabel(self.splitter_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEditAlgorithm = QtGui.QLineEdit(self.splitter_4)
        self.lineEditAlgorithm.setObjectName(_fromUtf8("lineEditAlgorithm"))
        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Pathfinding", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#000055;\">SHORTEST PATH</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#550000;\">FINDER</span></p></body></html>", None))
        self.pushButtonRun.setText(_translate("MainWindow", "RUN!", None))
        self.label_2.setText(_translate("MainWindow", "Map File:", None))
        self.lineEditMapFile.setText(_translate("MainWindow", "demo_map.txt", None))
        self.pushButtonEditMap.setText(_translate("MainWindow", "Edit Map", None))
        self.pushButtonMapFormat.setText(_translate("MainWindow", "Map File Format", None))
        self.label_3.setText(_translate("MainWindow", "Output image:", None))
        self.lineEditImageFile.setText(_translate("MainWindow", "demo.png", None))
        self.label_4.setText(_translate("MainWindow", "Algorithm:  ", None))
        self.lineEditAlgorithm.setToolTip(_translate("MainWindow", "<html><head/><body><p>Astar, DFS, or HillClimbing</p></body></html>", None))
        self.lineEditAlgorithm.setText(_translate("MainWindow", "Astar", None))

