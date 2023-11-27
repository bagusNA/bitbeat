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
from PySide6.QtWidgets import (QApplication, QGridLayout, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_lyrics_view(object):
    def setupUi(self, lyrics_view):
        if not lyrics_view.objectName():
            lyrics_view.setObjectName(u"lyrics_view")
        lyrics_view.resize(596, 536)
        self.gridLayout = QGridLayout(lyrics_view)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(lyrics_view)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.view_slot = QWidget()
        self.view_slot.setObjectName(u"view_slot")
        self.view_slot.setGeometry(QRect(0, 0, 586, 526))
        self.gridLayout_2 = QGridLayout(self.view_slot)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lyrics_container = QVBoxLayout()
        self.lyrics_container.setObjectName(u"lyrics_container")

        self.gridLayout_2.addLayout(self.lyrics_container, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.view_slot)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(lyrics_view)

        QMetaObject.connectSlotsByName(lyrics_view)
    # setupUi

    def retranslateUi(self, lyrics_view):
        lyrics_view.setWindowTitle(QCoreApplication.translate("lyrics_view", u"Form", None))
    # retranslateUi

