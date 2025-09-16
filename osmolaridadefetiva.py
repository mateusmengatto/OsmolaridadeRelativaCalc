from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QScrollArea, QWidget, QVBoxLayout
from PySide6.QtGui import QIcon, QKeyEvent
from ui.mainwindow_osmo import Ui_MainWindow
from PySide6.QtCore import QTimer, QEvent, QObject
import PySide6.QtGui as qtg
import sys
import os

basedir=os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Osmolaridade Efetiva")

        self.calcule_btn.clicked.connect(self.osmolaridade_efetiva)



    def osmolaridade_efetiva(self):
        na_medido = float(self.na_medido_linedit.text())
        glicemia_medida = float(self.glicemia_medida_linedit.text())

        na_corrigido = na_medido + 1.6 *((glicemia_medida-100)/100)
        osmolaridade_efetiva = 2*(na_corrigido) + glicemia_medida/18
        if osmolaridade_efetiva > 320:
            x = 'Hiperosmolaridade'
        else:
            x = ''   
        text = (
            f'Na+ Corrigido = {na_corrigido} \n \n'
            f'*** Osmolaridade Efetiva = {osmolaridade_efetiva} ({x}) ***\n \n'
            f'(Obs: Hiperosmolaridade = Valores > 320 mosm/kg)'
            )
        self.result_osmolaridade_text.setPlainText(text)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(qtg.QIcon(os.path.join(basedir, 'drop_icon.ico')))
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()