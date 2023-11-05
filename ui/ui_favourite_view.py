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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_favourite_view(object):
    def setupUi(self, favourite_view):
        if not favourite_view.objectName():
            favourite_view.setObjectName(u"favourite_view")
        favourite_view.resize(594, 347)
        self.gridLayout = QGridLayout(favourite_view)
        self.gridLayout.setObjectName(u"gridLayout")
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

        self.verticalSpacer_2 = QSpacerItem(20, 258, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.retranslateUi(favourite_view)

        QMetaObject.connectSlotsByName(favourite_view)
    # setupUi

    def retranslateUi(self, favourite_view):
        favourite_view.setWindowTitle(QCoreApplication.translate("favourite_view", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("favourite_view", u"Favourite", None))
    # retranslateUi

