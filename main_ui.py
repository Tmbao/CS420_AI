#!/usr/bin/python

from PyQt4 import QtGui
import sys
import ui_design
import os
import webbrowser

class MyApp(QtGui.QMainWindow, ui_design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # handle button click
        self.pushButtonEditHeuristic.clicked.connect(self.edit_heuristic_file)
        self.pushButtonEditEdge.clicked.connect(self.edit_edge_file)
        self.pushButtonRun.clicked.connect(self.run_click)

    def edit_heuristic_file(self):
        file_name = str(self.lineEditHeuristicFile.text())
        webbrowser.open(file_name)
        
    def edit_edge_file(self):
        file_name = str(self.lineEditEdgeFile.text())
        webbrowser.open(file_name)

    def run_click(self):
        print 'Computing shortest path...\n'
        heuristic_file = str(self.lineEditHeuristicFile.text())
        edge_file = str(self.lineEditEdgeFile.text())
        image_file = str(self.lineEditImageFile.text())
        chosen_algorithm = str(self.lineEditAlgorithm.text())
        source = str(self.lineEditSrc.text())
        target = str(self.lineEditTarget.text())

        os.system('python demo.py {} {} {} {} {} {}'.format(chosen_algorithm, heuristic_file, edge_file, source, target, image_file))

def main():
    app = QtGui.QApplication(sys.argv)  
    form = MyApp() 
    form.show()                        
    app.exec_() 


if __name__ == '__main__':            
    main()
