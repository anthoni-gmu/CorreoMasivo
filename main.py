from archivos.Interfaz import * 
from archivos.excel import * 
from archivos.containerMsg import * 
from archivos.mail import * 
from math import floor

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.clicked)
    def clicked(self):
                self.progressBar.setVisible(True)
                correoEmisor=self.correo.text()
                passEmisor=self.passs.text()
                print(correoEmisor)
                print(passEmisor)
                lista=correosCliente()
                progress=len(lista)/100
                progress=floor(progress)
                i=0
                e=0
                for key in lista:
                    i+=1
                    if(progress==i):
                        i=0
                        e+=1
                        self.progressBar.setProperty("value",e)
                    print (key, ":", lista[key])
                    msg=container(key)
                    
                    dest=lista[key]
                    correoContainer(correoEmisor,passEmisor,msg,dest)
                self.label_3.setVisible(True)
        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()