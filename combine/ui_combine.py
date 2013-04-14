# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combine.ui'
#
# Created: Fri Aug 19 09:17:24 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PySide  import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(731, 475)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionShow_GPL = QtGui.QAction(MainWindow)
        self.actionShow_GPL.setText(QtGui.QApplication.translate("MainWindow", "Show &GPL", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_GPL.setObjectName(_fromUtf8("actionShow_GPL"))
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setObjectName(_fromUtf8("action_About"))
        self.action_Close = QtGui.QAction(MainWindow)
        self.action_Close.setCheckable(False)
        self.action_Close.setText(QtGui.QApplication.translate("MainWindow", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Close.setObjectName(_fromUtf8("action_Close"))
        self.menu_File.addAction(self.actionShow_GPL)
        self.menu_File.addAction(self.action_About)
        self.menu_File.addAction(self.action_Close)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Close, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

