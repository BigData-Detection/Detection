# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graduation3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

#GUI
from PyQt5 import QtCore, QtGui, QtWidgets
from hybridDetection import hybridDetect
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1592, 783)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 631, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 91, 15))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(670, 70, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButton_cliked)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 130, 781, 641))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 639))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(400, 20, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 141, 16))
        self.label_2.setObjectName("label_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView_2.setGeometry(QtCore.QRect(400, 340, 361, 271))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(400, 320, 141, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(10, 320, 141, 16))
        self.label_5.setObjectName("label_5")
        self.graphicsView = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView.setGeometry(QtCore.QRect(400, 40, 361, 261))
        self.graphicsView.setObjectName("graphicsView")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 351, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 340, 351, 271))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_2.setGeometry(QtCore.QRect(800, 130, 781, 641))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 779, 639))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setGeometry(QtCore.QRect(400, 20, 131, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 211, 16))
        self.label_7.setObjectName("label_7")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents_2)
        self.graphicsView_3.setGeometry(QtCore.QRect(400, 340, 361, 271))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setGeometry(QtCore.QRect(400, 320, 141, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setGeometry(QtCore.QRect(10, 320, 251, 16))
        self.label_9.setObjectName("label_9")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents_2)
        self.graphicsView_4.setGeometry(QtCore.QRect(400, 40, 361, 261))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 40, 351, 271))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 340, 351, 271))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def pushButton_cliked(self):
        path = self.lineEdit.text()
        #send text_file paht hybridDetect function in  hybridDetection.py
        hybridDetect(path)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Input File path"))
        self.pushButton.setText(_translate("Dialog", "Enter"))
        self.label_3.setText(_translate("Dialog", "misuse attack chart"))
        self.label_2.setText(_translate("Dialog", "misuse attack data"))
        self.label_4.setText(_translate("Dialog", "anomoly attack chart"))
        self.label_5.setText(_translate("Dialog", "anomoly attack data"))
        self.label_6.setText(_translate("Dialog", "misuse ROC curve"))
        self.label_7.setText(_translate("Dialog", "misuse attack models accuarcy"))
        self.label_8.setText(_translate("Dialog", "anomoly Roc curve"))
        self.label_9.setText(_translate("Dialog", "anomoly attack models accuarcy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
