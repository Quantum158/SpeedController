# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Benja\source\repos\Quantum158\SpeedController\src\main\python\modules\LogGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 700)
        MainWindow.setMinimumSize(QtCore.QSize(400, 700))
        MainWindow.setMaximumSize(QtCore.QSize(800, 700))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.MainFrame = QtWidgets.QWidget(MainWindow)
        self.MainFrame.setEnabled(True)
        self.MainFrame.setMinimumSize(QtCore.QSize(800, 700))
        self.MainFrame.setMaximumSize(QtCore.QSize(800, 700))
        self.MainFrame.setObjectName("MainFrame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.MainFrame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 701))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.MainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setObjectName("MainLayout")
        self.LogList = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.LogList.setObjectName("LogList")
        self.MainLayout.addWidget(self.LogList)
        MainWindow.setCentralWidget(self.MainFrame)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Speed Controller Log"))
        MainWindow.setToolTip(_translate("MainWindow", "Wow! Words"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

