# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'favourite_view.ui'
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

class Ui_favourite_view(object):
    def setupUi(self, favourite_view):
        if not favourite_view.objectName():
            favourite_view.setObjectName(u"favourite_view")
        favourite_view.resize(594, 347)
        self.gridLayout = QGridLayout(favourite_view)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(favourite_view)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 582, 261))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.favourite_list = QVBoxLayout()
        self.favourite_list.setObjectName(u"favourite_list")
        self.favourite_list.setContentsMargins(-1, -1, -1, 0)

        self.gridLayout_2.addLayout(self.favourite_list, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 24)
        self.label_3 = QLabel(favourite_view)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.retranslateUi(favourite_view)

        QMetaObject.connectSlotsByName(favourite_view)
    # setupUi

    def retranslateUi(self, favourite_view):
        favourite_view.setWindowTitle(QCoreApplication.translate("favourite_view", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("favourite_view", u"Favourite", None))
    # retranslateUi

