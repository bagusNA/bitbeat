# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_view.ui'
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

class Ui_setting_view(object):
    def setupUi(self, setting_view):
        if not setting_view.objectName():
            setting_view.setObjectName(u"setting_view")
        setting_view.resize(591, 347)
        self.gridLayout = QGridLayout(setting_view)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 24)
        self.label_6 = QLabel(setting_view)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(24)
        self.label_6.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 258, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 1, 0, 1, 1)


        self.retranslateUi(setting_view)

        QMetaObject.connectSlotsByName(setting_view)
    # setupUi

    def retranslateUi(self, setting_view):
        setting_view.setWindowTitle(QCoreApplication.translate("setting_view", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("setting_view", u"Settings", None))
    # retranslateUi

