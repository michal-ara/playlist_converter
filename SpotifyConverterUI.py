# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Oct 16 22:26:57 2014
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_MainWindows(object):
    def setupUi(self, MainWindows):
        MainWindows.setObjectName(_fromUtf8("MainWindows"))
        MainWindows.resize(800, 600)
        self.centralWidget = QtGui.QWidget(MainWindows)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.InputText = QtGui.QTextEdit(self.centralWidget)
        self.InputText.setGeometry(QtCore.QRect(19, 29, 371, 411))
        self.InputText.setObjectName(_fromUtf8("InputText"))
        self.OutputText = QtGui.QTextEdit(self.centralWidget)
        self.OutputText.setGeometry(QtCore.QRect(409, 29, 371, 411))
        self.OutputText.setObjectName(_fromUtf8("OutputText"))
        self.LabelInputText = QtGui.QLabel(self.centralWidget)
        self.LabelInputText.setGeometry(QtCore.QRect(20, 0, 411, 31))
        self.LabelInputText.setObjectName(_fromUtf8("LabelInputText"))
        self.LabelOutputText = QtGui.QLabel(self.centralWidget)
        self.LabelOutputText.setGeometry(QtCore.QRect(410, 0, 411, 31))
        self.LabelOutputText.setObjectName(_fromUtf8("LabelOutputText"))
        self.SetupBox = QtGui.QGroupBox(self.centralWidget)
        self.SetupBox.setGeometry(QtCore.QRect(10, 450, 381, 111))
        self.SetupBox.setObjectName(_fromUtf8("SetupBox"))
        self.SetupLabel1 = QtGui.QLabel(self.SetupBox)
        self.SetupLabel1.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.SetupLabel1.setObjectName(_fromUtf8("SetupLabel1"))
        self.SetupLabel2 = QtGui.QLabel(self.SetupBox)
        self.SetupLabel2.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.SetupLabel2.setObjectName(_fromUtf8("SetupLabel2"))
        self.SetupLabel3 = QtGui.QLabel(self.SetupBox)
        self.SetupLabel3.setGeometry(QtCore.QRect(10, 60, 91, 21))
        self.SetupLabel3.setObjectName(_fromUtf8("SetupLabel3"))
        self.SetupLabel4 = QtGui.QLabel(self.SetupBox)
        self.SetupLabel4.setGeometry(QtCore.QRect(10, 80, 91, 21))
        self.SetupLabel4.setObjectName(_fromUtf8("SetupLabel4"))
        self.SetupLine1 = QtGui.QLineEdit(self.SetupBox)
        self.SetupLine1.setGeometry(QtCore.QRect(110, 20, 131, 20))
        self.SetupLine1.setObjectName(_fromUtf8("SetupLine1"))
        self.SetupLine2 = QtGui.QLineEdit(self.SetupBox)
        self.SetupLine2.setGeometry(QtCore.QRect(110, 40, 131, 20))
        self.SetupLine2.setObjectName(_fromUtf8("SetupLine2"))
        self.SetupLine3 = QtGui.QLineEdit(self.SetupBox)
        self.SetupLine3.setGeometry(QtCore.QRect(110, 60, 131, 20))
        self.SetupLine3.setObjectName(_fromUtf8("SetupLine3"))
        self.SetupLine4 = QtGui.QLineEdit(self.SetupBox)
        self.SetupLine4.setGeometry(QtCore.QRect(110, 80, 131, 20))
        self.SetupLine4.setObjectName(_fromUtf8("SetupLine4"))
        self.SetupComboBox1 = QtGui.QComboBox(self.SetupBox)
        self.SetupComboBox1.setGeometry(QtCore.QRect(250, 20, 111, 22))
        self.SetupComboBox1.setObjectName(_fromUtf8("SetupComboBox1"))
        self.SetupComboBox2 = QtGui.QComboBox(self.SetupBox)
        self.SetupComboBox2.setGeometry(QtCore.QRect(250, 50, 111, 22))
        self.SetupComboBox2.setObjectName(_fromUtf8("SetupComboBox2"))
        self.SetupComboBox3 = QtGui.QComboBox(self.SetupBox)
        self.SetupComboBox3.setGeometry(QtCore.QRect(250, 80, 111, 22))
        self.SetupComboBox3.setObjectName(_fromUtf8("SetupComboBox3"))
        self.ButtonHelper1 = QtGui.QPushButton(self.centralWidget)
        self.ButtonHelper1.setGeometry(QtCore.QRect(410, 460, 100, 30))
        self.ButtonHelper1.setObjectName(_fromUtf8("ButtonHelper1"))
        self.ButtonHelper3 = QtGui.QPushButton(self.centralWidget)
        self.ButtonHelper3.setGeometry(QtCore.QRect(670, 460, 100, 30))
        self.ButtonHelper3.setObjectName(_fromUtf8("ButtonHelper3"))
        self.ButtonHelper2 = QtGui.QPushButton(self.centralWidget)
        self.ButtonHelper2.setGeometry(QtCore.QRect(540, 460, 100, 30))
        self.ButtonHelper2.setObjectName(_fromUtf8("ButtonHelper2"))
        self.ButtonStart = QtGui.QPushButton(self.centralWidget)
        self.ButtonStart.setGeometry(QtCore.QRect(410, 520, 361, 41))
        self.ButtonStart.setObjectName(_fromUtf8("ButtonStart"))
        self.LabelHelper1 = QtGui.QLabel(self.centralWidget)
        self.LabelHelper1.setGeometry(QtCore.QRect(399, 492, 120, 30))
        self.LabelHelper1.setObjectName(_fromUtf8("LabelHelper1"))
        self.LabelHelper2 = QtGui.QLabel(self.centralWidget)
        self.LabelHelper2.setGeometry(QtCore.QRect(530, 490, 120, 30))
        self.LabelHelper2.setObjectName(_fromUtf8("LabelHelper2"))
        self.LabelHelper3 = QtGui.QLabel(self.centralWidget)
        self.LabelHelper3.setGeometry(QtCore.QRect(660, 490, 120, 30))
        self.LabelHelper3.setObjectName(_fromUtf8("LabelHelper3"))
        MainWindows.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindows)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindows.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindows)
        QtCore.QMetaObject.connectSlotsByName(MainWindows)

    def retranslateUi(self, MainWindows):
        MainWindows.setWindowTitle(_translate("MainWindows", "Spotify Converter", None))
        self.LabelInputText.setText(_translate("MainWindows", "Text to convert:", None))
        self.LabelOutputText.setText(_translate("MainWindows", "Log:", None))
        self.SetupBox.setTitle(_translate("MainWindows", "Setup", None))
        self.SetupLabel1.setText(_translate("MainWindows", "TextLabel", None))
        self.SetupLabel2.setText(_translate("MainWindows", "TextLabel", None))
        self.SetupLabel3.setText(_translate("MainWindows", "TextLabel", None))
        self.SetupLabel4.setText(_translate("MainWindows", "TextLabel", None))
        self.ButtonHelper1.setText(_translate("MainWindows", "TEST", None))
        self.ButtonHelper3.setText(_translate("MainWindows", "TEST", None))
        self.ButtonHelper2.setText(_translate("MainWindows", "TEST", None))
        self.ButtonStart.setText(_translate("MainWindows", "START", None))
        self.LabelHelper1.setText(_translate("MainWindows", "TextLabel", None))
        self.LabelHelper2.setText(_translate("MainWindows", "TextLabel", None))
        self.LabelHelper3.setText(_translate("MainWindows", "TextLabel", None))