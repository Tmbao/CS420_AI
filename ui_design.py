# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Fri Apr 22 07:03:49 2016
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
        MainWindow.resize(310, 372)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(310, 372))
        MainWindow.setMaximumSize(QtCore.QSize(310, 372))
        self.widget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget1 = QtGui.QWidget(self.widget)
        self.widget1.setGeometry(QtCore.QRect(20, 10, 271, 346))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditHeuristicFile = QtGui.QLineEdit(self.widget1)
        self.lineEditHeuristicFile.setObjectName(_fromUtf8("lineEditHeuristicFile"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditHeuristicFile)
        self.label_5 = QtGui.QLabel(self.widget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEditEdgeFile = QtGui.QLineEdit(self.widget1)
        self.lineEditEdgeFile.setObjectName(_fromUtf8("lineEditEdgeFile"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditEdgeFile)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.splitter_5 = QtGui.QSplitter(self.widget1)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.pushButtonEditHeuristic = QtGui.QPushButton(self.splitter_5)
        self.pushButtonEditHeuristic.setObjectName(_fromUtf8("pushButtonEditHeuristic"))
        self.pushButtonEditEdge = QtGui.QPushButton(self.splitter_5)
        self.pushButtonEditEdge.setObjectName(_fromUtf8("pushButtonEditEdge"))
        self.verticalLayout.addWidget(self.splitter_5)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_6 = QtGui.QLabel(self.widget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEditSrc = QtGui.QLineEdit(self.widget1)
        self.lineEditSrc.setObjectName(_fromUtf8("lineEditSrc"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditSrc)
        self.label_7 = QtGui.QLabel(self.widget1)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEditTarget = QtGui.QLineEdit(self.widget1)
        self.lineEditTarget.setObjectName(_fromUtf8("lineEditTarget"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditTarget)
        self.verticalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.widget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEditAlgorithm = QtGui.QLineEdit(self.widget1)
        self.lineEditAlgorithm.setObjectName(_fromUtf8("lineEditAlgorithm"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditAlgorithm)
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditImageFile = QtGui.QLineEdit(self.widget1)
        self.lineEditImageFile.setObjectName(_fromUtf8("lineEditImageFile"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditImageFile)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.pushButtonRun = QtGui.QPushButton(self.widget1)
        self.pushButtonRun.setObjectName(_fromUtf8("pushButtonRun"))
        self.verticalLayout.addWidget(self.pushButtonRun)
        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Shortest Path Finder", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#550000;\">SHORTEST PATH</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#550000;\">FINDER</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "Heuristic File:", None))
        self.lineEditHeuristicFile.setText(_translate("MainWindow", "data/Astar/input1b.txt", None))
        self.label_5.setText(_translate("MainWindow", "Edge File:    ", None))
        self.lineEditEdgeFile.setText(_translate("MainWindow", "data/Astar/input1a.txt", None))
        self.pushButtonEditHeuristic.setText(_translate("MainWindow", "Edit Heuristic File", None))
        self.pushButtonEditEdge.setText(_translate("MainWindow", "Edit Edge File", None))
        self.label_6.setText(_translate("MainWindow", "Source:", None))
        self.lineEditSrc.setText(_translate("MainWindow", "Arad", None))
        self.label_7.setText(_translate("MainWindow", "Target:", None))
        self.lineEditTarget.setText(_translate("MainWindow", "Bucharest", None))
        self.label_4.setText(_translate("MainWindow", "Algorithm:", None))
        self.lineEditAlgorithm.setToolTip(_translate("MainWindow", "<html><head/><body><p>Astar, UCS, or BFS</p></body></html>", None))
        self.lineEditAlgorithm.setText(_translate("MainWindow", "Astar", None))
        self.label_3.setText(_translate("MainWindow", "Output image:", None))
        self.lineEditImageFile.setText(_translate("MainWindow", "demo.png", None))
        self.pushButtonRun.setText(_translate("MainWindow", "RUN!", None))

