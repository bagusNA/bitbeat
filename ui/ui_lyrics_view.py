# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lyrics_view.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QWidget)

class Ui_lyrics_view(object):
    def setupUi(self, lyrics_view):
        if not lyrics_view.objectName():
            lyrics_view.setObjectName(u"lyrics_view")
        lyrics_view.resize(596, 536)
        self.gridLayout = QGridLayout(lyrics_view)
        self.gridLayout.setObjectName(u"gridLayout")
        self.view_slot = QWidget(lyrics_view)
        self.view_slot.setObjectName(u"view_slot")

        self.gridLayout.addWidget(self.view_slot, 0, 0, 1, 1)


        self.retranslateUi(lyrics_view)

        QMetaObject.connectSlotsByName(lyrics_view)
    # setupUi

    def retranslateUi(self, lyrics_view):
        lyrics_view.setWindowTitle(QCoreApplication.translate("lyrics_view", u"Form", None))
    # retranslateUi

