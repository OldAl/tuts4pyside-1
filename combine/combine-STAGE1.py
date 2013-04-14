#!/usr/bin/env python3
# combine.py - combination of ShowCCPL, About, Close scripts

# Copyright (c) 2010-2011 Algis Kabaila. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public Licence as published
# by the Free Software Foundation, either version 2 of the Licence, or
# version 3 of the Licence, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public Licence for more details.

import sys
import platform

import PySide
from PySide.QtGui import QApplication, QMainWindow, QTextEdit,\
                         QPushButton,  QMessageBox

__version__ = '3.0.2'
from ui_combine import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionShow_GPL.triggered.connect(self.showGPL)
        self.action_About.triggered.connect(self.about)        
               
    def showGPL(self):
        '''Read and display CCPL licence.'''
        with open('CCPL.txt') as nonamefile:
            self.textEdit.setText(nonamefile.read())

    def about(self):
        '''Popup a box with about message.'''
        QMessageBox.about(self, "About PySide, Platform and version.",
                """<b> about.py version %s </b> 
                <p>Copyright &copy; 2013 by Algis Kabaila. 
                This work is made available under  the terms of
                Creative Commons Attribution-ShareAlike 3.0 license,
                http://creativecommons.org/licenses/by-sa/3.0/.
                <p>This application is useful for displaying  
                Qt version and other details.
                <p>Python %s -  PySide version %s - Qt version %s on %s""" % (__version__, 
                platform.python_version(), PySide.__version__,  PySide.QtCore.__version__,
                platform.system()))
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()
