'''
To use the program with UI, PyQt is needed.
Installation on Ubuntu 14.04:
In terminal, run:
sudo apt-get install python-qt4 pyqt4-dev-tools
'''
from PyQt4 import QtGui
import sys
import ui_design
import os

class MyApp(QtGui.QMainWindow, ui_design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # handle button click
        self.pushButtonEditMap.clicked.connect(self.edit_map_file)
        self.pushButtonMapFormat.clicked.connect(self.show_map_file_format)
        self.pushButtonRun.clicked.connect(self.run_click)

    def edit_map_file(self):
        map_file = str(self.lineEditMapFile.text())
        os.system('gedit ' + map_file)

    def show_map_file_format(self):
        msg_box = QtGui.QMessageBox()     
        msg_box.setIcon(QtGui.QMessageBox.Information)
        
        msg_box.setText('Format of map input file')
        msg_box.setInformativeText('Click Show Details to view the format of map input file')
        msg_box.setWindowTitle('Map File Format')
        map_format = '''First line: n_node - the number of nodes\n\n\
            Next n_node lines contain information of each node in the form "node_id node_name latitude longtitude"\n\n\
            Next line: n_edge - the number of edges\n\n\
            Next n_edge lines contain information of each edge in the form "vertice_1 vertice_2 length"\n\n\
            Last line: start_node end_node\n'''
        msg_box.setDetailedText(map_format)
        msg_box.setStandardButtons(QtGui.QMessageBox.Ok)
        msg_box.exec_()
        
    def run_click(self):
        map_file = str(self.lineEditMapFile.text())
        image_file = str(self.lineEditImageFile.text())
        chosen_algorithm = str(self.lineEditAlgorithm.text())
        print 'Calculating shortest path...'
        os.system('python demo.py {} {} {}'.format(chosen_algorithm, map_file, image_file))

def main():
    app = QtGui.QApplication(sys.argv)  
    form = MyApp() 
    form.show()                        
    app.exec_() 


if __name__ == '__main__':            
    main()
