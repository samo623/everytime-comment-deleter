# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindownqxXqU.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)
from version import __version__

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(373, 191)
        self.actionvuswlq = QAction(MainWindow)
        self.actionvuswlq.setObjectName(u"actionvuswlq")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 60, 131, 21))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 90, 131, 21))
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(160, 10, 211, 161))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setCenterOnScroll(False)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 130, 91, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 181, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionvuswlq.setText(QCoreApplication.translate("MainWindow", u"vuswlq", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\uac1c\uc778\uc815\ubcf4 \ucde8\uae09\ubc29\uce68", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\uc774\uc6a9\uc57d\uad00", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\ubc84\uadf8 \uc81c\ubcf4", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\uac1c\ubc1c\uc790 \uc815\ubcf4", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc5d0\ube0c\ub9ac\ud0c0\uc784 \uc544\uc774\ub514", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc5d0\ube0c\ub9ac\ud0c0\uc784 \ube44\ubc00\ubc88\ud638", None))
        self.plainTextEdit.setDocumentTitle("")
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Github : https://github.com/samo623/everytime-comment-deleter/\n"
"\n"
"\ubcf8 \ud504\ub85c\uadf8\ub7a8\uc740 GNU GENERAL PUBLIC LICENSE Version 3 \ub97c \uc801\uc6a9\ubc1b\uace0 \uc788\uc2b5\ub2c8\ub2e4\n"
"\n"
"\uc624\ub958\ubb38\uc758\ub294 Github Isuue \ub610\ub294 sxmo623@gmail.com\uc73c\ub85c \ubd80\ud0c1\ub4dc\ub9bd\ub2c8\ub2e4.\n"
"\n"
"Version : 1.0.0"
"\n"
"\n"
"", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\ub313\uae00 \uc0ad\uc81c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID\uc640 PW\ub97c \uc801\uc73c\uc2dc\uace0 \n"
"\ub313\uae00\uc0ad\uc81c\ubc84\ud2bc\uc744 \ub20c\ub7ec\uc8fc\uc138\uc694", None))
    # retranslateUi

