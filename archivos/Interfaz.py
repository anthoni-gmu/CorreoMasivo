from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
        
        def setupUi(self, Dialog):
                Dialog.setObjectName("Dialog")
                Dialog.resize(561, 369)
                Dialog.setStyleSheet("background-color: rgb(85, 85, 127);\n"
        "")
                self.label = QtWidgets.QLabel(Dialog)
                self.label.setGeometry(QtCore.QRect(50, 130, 68, 19))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label.setFont(font)
                self.label.setStyleSheet("color: rgb(255, 255, 255);")
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(Dialog)
                self.label_2.setGeometry(QtCore.QRect(50, 180, 121, 19))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_2.setObjectName("label_2")
                self.textBrowser = QtWidgets.QTextBrowser(Dialog)
                self.textBrowser.setGeometry(QtCore.QRect(0, 0, 561, 81))
                self.textBrowser.setObjectName("textBrowser")
                self.correo = QtWidgets.QLineEdit(Dialog)
                self.correo.setGeometry(QtCore.QRect(170, 120, 321, 41))
                self.correo.setObjectName("correo")
                self.passs = QtWidgets.QLineEdit(Dialog)
                self.passs.setGeometry(QtCore.QRect(170, 170, 321, 41))
                self.passs.setObjectName("pass")
                self.passs.setStyleSheet("color: rgb(85, 85, 127);")
                self.progressBar = QtWidgets.QProgressBar(Dialog)
                self.progressBar.setGeometry(QtCore.QRect(20, 280, 521, 20))
                self.progressBar.setProperty("value", 0)
                self.progressBar.setObjectName("progressBar")
                self.progressBar.setVisible(False)
                self.pushButton = QtWidgets.QPushButton(Dialog)
                self.pushButton.setGeometry(QtCore.QRect(210, 230, 121, 41))
                self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                
        "font: 10pt \"Microsoft JhengHei\";\n"
        "background-color: rgb(85, 170, 127);")
                self.pushButton.setObjectName("pushButton")
                self.label_3 = QtWidgets.QLabel(Dialog)
                self.label_3.setGeometry(QtCore.QRect(200, 330, 181, 19))
                self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
                self.label_3.setObjectName("label_3")

                self.retranslateUi(Dialog)
                QtCore.QMetaObject.connectSlotsByName(Dialog)

        def retranslateUi(self, Dialog):
                _translate = QtCore.QCoreApplication.translate
                Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
                self.label.setText(_translate("Dialog", "Correo:"))
                self.label_2.setText(_translate("Dialog", "Contraseña: "))
                self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#282828;\">CORREO MASIVO</span></p></body></html>"))
                self.pushButton.setText(_translate("Dialog", "ENVIAR") )
                self.label_3.setText(_translate("Dialog", "OPERACION EXITOSA!"))
                self.label_3.setVisible(False)

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

