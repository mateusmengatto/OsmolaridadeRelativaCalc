# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(743, 167)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.calcule_btn = QPushButton(self.centralwidget)
        self.calcule_btn.setObjectName(u"calcule_btn")
        self.calcule_btn.setGeometry(QRect(230, 30, 75, 51))
        self.na_medido_lbl = QLabel(self.centralwidget)
        self.na_medido_lbl.setObjectName(u"na_medido_lbl")
        self.na_medido_lbl.setGeometry(QRect(40, 20, 101, 16))
        font = QFont()
        font.setPointSize(12)
        self.na_medido_lbl.setFont(font)
        self.na_medido_lbl.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.glicemia_medida_lbl = QLabel(self.centralwidget)
        self.glicemia_medida_lbl.setObjectName(u"glicemia_medida_lbl")
        self.glicemia_medida_lbl.setGeometry(QRect(10, 70, 131, 20))
        self.glicemia_medida_lbl.setFont(font)
        self.na_medido_linedit = QLineEdit(self.centralwidget)
        self.na_medido_linedit.setObjectName(u"na_medido_linedit")
        self.na_medido_linedit.setGeometry(QRect(142, 20, 71, 21))
        self.glicemia_medida_linedit = QLineEdit(self.centralwidget)
        self.glicemia_medida_linedit.setObjectName(u"glicemia_medida_linedit")
        self.glicemia_medida_linedit.setGeometry(QRect(142, 70, 71, 21))
        self.result_osmolaridade_text = QPlainTextEdit(self.centralwidget)
        self.result_osmolaridade_text.setObjectName(u"result_osmolaridade_text")
        self.result_osmolaridade_text.setGeometry(QRect(310, 0, 421, 111))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(700, 110, 31, 20))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift Light"])
        font1.setPointSize(6)
        self.label.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 743, 22))
        self.menuCalcule_Osmolaridade = QMenu(self.menubar)
        self.menuCalcule_Osmolaridade.setObjectName(u"menuCalcule_Osmolaridade")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCalcule_Osmolaridade.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.calcule_btn.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.na_medido_lbl.setText(QCoreApplication.translate("MainWindow", u"Na+ Medido :", None))
        self.glicemia_medida_lbl.setText(QCoreApplication.translate("MainWindow", u"Glicemia Medida :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"by MM.", None))
        self.menuCalcule_Osmolaridade.setTitle(QCoreApplication.translate("MainWindow", u"Calcule Osmolaridade Efetiva", None))
    # retranslateUi

