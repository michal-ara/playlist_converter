import sys
from PyQt4 import QtCore, QtGui

from SpotifyConverterUI import Ui_MainWindows


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindows()
        self.ui.setupUi(self)
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())