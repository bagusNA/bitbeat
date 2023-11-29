# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playlist_view.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_playlist_view(object):
    def setupUi(self, playlist_view):
        if not playlist_view.objectName():
            playlist_view.setObjectName(u"playlist_view")
        playlist_view.resize(596, 349)
        self.gridLayout = QGridLayout(playlist_view)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(playlist_view)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 584, 263))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.playlist_list = QVBoxLayout()
        self.playlist_list.setObjectName(u"playlist_list")

        self.gridLayout_2.addLayout(self.playlist_list, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 447, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 24)
        self.label_3 = QLabel(playlist_view)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.retranslateUi(playlist_view)

        QMetaObject.connectSlotsByName(playlist_view)
    # setupUi

    def retranslateUi(self, playlist_view):
        playlist_view.setWindowTitle(QCoreApplication.translate("playlist_view", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("playlist_view", u"Playlist", None))
    # retranslateUi

