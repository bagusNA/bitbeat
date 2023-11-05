# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_view.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import assets_rc

class Ui_home_view(object):
    def setupUi(self, home_view):
        if not home_view.objectName():
            home_view.setObjectName(u"home_view")
        home_view.resize(592, 532)
        self.gridLayout = QGridLayout(home_view)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 24)
        self.page_title_label = QLabel(home_view)
        self.page_title_label.setObjectName(u"page_title_label")
        font = QFont()
        font.setPointSize(24)
        self.page_title_label.setFont(font)

        self.horizontalLayout_4.addWidget(self.page_title_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.input_search = QLineEdit(home_view)
        self.input_search.setObjectName(u"input_search")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_search.sizePolicy().hasHeightForWidth())
        self.input_search.setSizePolicy(sizePolicy)
        self.input_search.setMinimumSize(QSize(0, 36))
        self.input_search.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.input_search)

        self.btn_search = QPushButton(home_view)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(0, 36))
        icon = QIcon()
        icon.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btn_search)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.pushButton_16 = QPushButton(home_view)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.verticalLayout_6.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(home_view)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.verticalLayout_6.addWidget(self.pushButton_17)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout_6, 1, 0, 1, 1)


        self.retranslateUi(home_view)

        QMetaObject.connectSlotsByName(home_view)
    # setupUi

    def retranslateUi(self, home_view):
        home_view.setWindowTitle(QCoreApplication.translate("home_view", u"Form", None))
        self.page_title_label.setText(QCoreApplication.translate("home_view", u"Home", None))
        self.btn_search.setText(QCoreApplication.translate("home_view", u"Search", None))
        self.pushButton_16.setText(QCoreApplication.translate("home_view", u"PushButton", None))
        self.pushButton_17.setText(QCoreApplication.translate("home_view", u"PushButton", None))
    # retranslateUi

