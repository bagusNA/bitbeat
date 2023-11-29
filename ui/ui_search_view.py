# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_view.ui'
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
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)
import assets_rc

class Ui_search_view(object):
    def setupUi(self, search_view):
        if not search_view.objectName():
            search_view.setObjectName(u"search_view")
        search_view.resize(596, 536)
        self.gridLayout = QGridLayout(search_view)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.scrollArea = QScrollArea(search_view)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.view_slot = QWidget()
        self.view_slot.setObjectName(u"view_slot")
        self.view_slot.setGeometry(QRect(0, 0, 584, 455))
        self.gridLayout_2 = QGridLayout(self.view_slot)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.search_container = QVBoxLayout()
        self.search_container.setObjectName(u"search_container")

        self.gridLayout_2.addLayout(self.search_container, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.view_slot)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(18)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 12)
        self.lineEdit = QLineEdit(search_view)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 36))

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(search_view)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 48))
        icon = QIcon()
        icon.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(search_view)

        QMetaObject.connectSlotsByName(search_view)
    # setupUi

    def retranslateUi(self, search_view):
        search_view.setWindowTitle(QCoreApplication.translate("search_view", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("search_view", u"Search", None))
    # retranslateUi

