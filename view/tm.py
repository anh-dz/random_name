# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 441)
        MainWindow.setStyleSheet("background: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Fname = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Fname.setGeometry(QtCore.QRect(40, 110, 291, 101))
        self.btn_Fname.setStyleSheet("font: 28pt \"Arial\";\n"
"border: 0pt;\n"
"color: white;")
        self.btn_Fname.setObjectName("btn_Fname")
        self.btn_Sname = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Sname.setGeometry(QtCore.QRect(470, 110, 291, 101))
        self.btn_Sname.setStyleSheet("font: 28pt \"Arial\";\n"
"border: 0pt;\n"
"color: white;")
        self.btn_Sname.setObjectName("btn_Sname")
        self.btn_Press = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Press.setGeometry(QtCore.QRect(270, 280, 251, 101))
        self.btn_Press.setStyleSheet("border: 0pt;")
        self.btn_Press.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assert/gift.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_Press.setIcon(icon)
        self.btn_Press.setIconSize(QtCore.QSize(90, 90))
        self.btn_Press.setObjectName("btn_Press")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tặng quà"))
        self.btn_Fname.setText(_translate("MainWindow", "???"))
        self.btn_Sname.setText(_translate("MainWindow", "???"))
