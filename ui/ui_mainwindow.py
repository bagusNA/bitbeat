# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import assets_rc
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(947, 648)
        icon = QIcon()
        icon.addFile(u":/images/images/logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.container = QWidget(MainWindow)
        self.container.setObjectName(u"container")
        self.gridLayout_2 = QGridLayout(self.container)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.collapsed_sidebar_widget = QWidget(self.container)
        self.collapsed_sidebar_widget.setObjectName(u"collapsed_sidebar_widget")
        self.collapsed_sidebar_widget.setMinimumSize(QSize(64, 0))
        self.collapsed_sidebar_widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.collapsed_sidebar_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.label = QLabel(self.collapsed_sidebar_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(64, 52))
        self.label.setMaximumSize(QSize(64, 52))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setPixmap(QPixmap(u":/images/images/logo-compact.svg"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 24, -1, 0)
        self.pushButton = QPushButton(self.collapsed_sidebar_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(64, 64))
        self.pushButton.setMaximumSize(QSize(64, 64))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.collapsed_sidebar_widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(64, 64))
        self.pushButton_2.setMaximumSize(QSize(64, 64))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/music-album.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.collapsed_sidebar_widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(64, 64))
        self.pushButton_3.setMaximumSize(QSize(64, 64))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/heart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_13 = QPushButton(self.collapsed_sidebar_widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(64, 64))
        self.pushButton_13.setMaximumSize(QSize(64, 64))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon4)
        self.pushButton_13.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.pushButton_13)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 309, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.collapsed_sidebar_widget, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.container)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(24)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(24, 12, 24, 12)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(12)
        self.album_cover = QLabel(self.widget_3)
        self.album_cover.setObjectName(u"album_cover")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.album_cover.sizePolicy().hasHeightForWidth())
        self.album_cover.setSizePolicy(sizePolicy)
        self.album_cover.setMinimumSize(QSize(64, 64))
        self.album_cover.setMaximumSize(QSize(64, 64))
        self.album_cover.setScaledContents(False)
        self.album_cover.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.album_cover, 0, 0, 2, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.song_title_label = QLabel(self.widget_3)
        self.song_title_label.setObjectName(u"song_title_label")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.song_title_label.setFont(font1)
        self.song_title_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_5.addWidget(self.song_title_label)

        self.song_artist_label = QLabel(self.widget_3)
        self.song_artist_label.setObjectName(u"song_artist_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.song_artist_label.setFont(font2)
        self.song_artist_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_5.addWidget(self.song_artist_label)


        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 1, 2, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_lyrics = QPushButton(self.widget_3)
        self.btn_lyrics.setObjectName(u"btn_lyrics")
        self.btn_lyrics.setMinimumSize(QSize(48, 32))
        self.btn_lyrics.setMaximumSize(QSize(48, 32))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/playlist.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lyrics.setIcon(icon5)

        self.horizontalLayout.addWidget(self.btn_lyrics)

        self.btn_volume = QPushButton(self.widget_3)
        self.btn_volume.setObjectName(u"btn_volume")
        self.btn_volume.setMinimumSize(QSize(48, 32))
        self.btn_volume.setMaximumSize(QSize(48, 32))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/volume-up-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_volume.setIcon(icon6)

        self.horizontalLayout.addWidget(self.btn_volume)

        self.btn_volume_muted = QPushButton(self.widget_3)
        self.btn_volume_muted.setObjectName(u"btn_volume_muted")
        self.btn_volume_muted.setMinimumSize(QSize(48, 32))
        self.btn_volume_muted.setMaximumSize(QSize(48, 32))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/volume-off-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_volume_muted.setIcon(icon7)

        self.horizontalLayout.addWidget(self.btn_volume_muted)

        self.volume_slider = QSlider(self.widget_3)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setEnabled(True)
        self.volume_slider.setMinimumSize(QSize(96, 24))
        self.volume_slider.setMaximumSize(QSize(96, 24))
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(100)
        self.volume_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.volume_slider)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 2, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(12)
        self.gridLayout_6.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.btn_shuffle = QPushButton(self.widget_3)
        self.btn_shuffle.setObjectName(u"btn_shuffle")
        self.btn_shuffle.setMinimumSize(QSize(48, 32))
        self.btn_shuffle.setMaximumSize(QSize(32, 32))
        self.btn_shuffle.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/playlist-shuffle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_shuffle.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.btn_shuffle)

        self.btn_previous = QPushButton(self.widget_3)
        self.btn_previous.setObjectName(u"btn_previous")
        self.btn_previous.setMinimumSize(QSize(48, 32))
        self.btn_previous.setMaximumSize(QSize(32, 32))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/player-start-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_previous.setIcon(icon9)

        self.horizontalLayout_2.addWidget(self.btn_previous)

        self.btn_play = QPushButton(self.widget_3)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setMinimumSize(QSize(48, 32))
        self.btn_play.setMaximumSize(QSize(32, 32))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/player-play-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_play.setIcon(icon10)

        self.horizontalLayout_2.addWidget(self.btn_play)

        self.btn_pause = QPushButton(self.widget_3)
        self.btn_pause.setObjectName(u"btn_pause")
        self.btn_pause.setEnabled(True)
        self.btn_pause.setMinimumSize(QSize(48, 32))
        self.btn_pause.setMaximumSize(QSize(32, 32))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/player-pause-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pause.setIcon(icon11)

        self.horizontalLayout_2.addWidget(self.btn_pause)

        self.btn_next = QPushButton(self.widget_3)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setMinimumSize(QSize(48, 32))
        self.btn_next.setMaximumSize(QSize(32, 32))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/player-end-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next.setIcon(icon12)

        self.horizontalLayout_2.addWidget(self.btn_next)

        self.btn_favorite = QPushButton(self.widget_3)
        self.btn_favorite.setObjectName(u"btn_favorite")
        self.btn_favorite.setMinimumSize(QSize(48, 32))
        self.btn_favorite.setMaximumSize(QSize(32, 32))
        self.btn_favorite.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_favorite)


        self.gridLayout_6.addLayout(self.horizontalLayout_2, 1, 2, 1, 2)

        self.current_duration_label = QLabel(self.widget_3)
        self.current_duration_label.setObjectName(u"current_duration_label")
        self.current_duration_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.current_duration_label, 2, 0, 1, 1)

        self.playback_slider = QSlider(self.widget_3)
        self.playback_slider.setObjectName(u"playback_slider")
        self.playback_slider.setMaximum(100)
        self.playback_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.playback_slider, 2, 2, 1, 2)

        self.total_duration_label = QLabel(self.widget_3)
        self.total_duration_label.setObjectName(u"total_duration_label")

        self.gridLayout_6.addWidget(self.total_duration_label, 2, 4, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_6, 0, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 1)

        self.gridLayout_2.addWidget(self.widget_3, 1, 0, 1, 3)

        self.topbar_widget = QWidget(self.container)
        self.topbar_widget.setObjectName(u"topbar_widget")
        self.gridLayout_4 = QGridLayout(self.topbar_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_2 = QWidget(self.topbar_widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_4.addWidget(self.widget_2, 1, 1, 1, 1)

        self.stackedWidget = QStackedWidget(self.topbar_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_7 = QGridLayout(self.page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.pushButton_16 = QPushButton(self.page)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.verticalLayout_6.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.page)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.verticalLayout_6.addWidget(self.pushButton_17)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.gridLayout_7.addLayout(self.verticalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 24)
        self.page_title_label = QLabel(self.page)
        self.page_title_label.setObjectName(u"page_title_label")
        font3 = QFont()
        font3.setPointSize(24)
        self.page_title_label.setFont(font3)

        self.horizontalLayout_4.addWidget(self.page_title_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.input_search = QLineEdit(self.page)
        self.input_search.setObjectName(u"input_search")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_search.sizePolicy().hasHeightForWidth())
        self.input_search.setSizePolicy(sizePolicy1)
        self.input_search.setMinimumSize(QSize(0, 36))
        self.input_search.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.input_search)

        self.btn_search = QPushButton(self.page)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(0, 36))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon13)

        self.horizontalLayout_4.addWidget(self.btn_search)


        self.gridLayout_7.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_8 = QGridLayout(self.page_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 24)
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_3)


        self.gridLayout_8.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_9 = QGridLayout(self.page_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 24)
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_4)


        self.gridLayout_9.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_10 = QGridLayout(self.page_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 24)
        self.label_6 = QLabel(self.page_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.gridLayout_10.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout_4.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.topbar_widget, 0, 1, 1, 1)

        self.widget = QWidget(self.container)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(24, 24, 24, 24)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 48))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5.setMargin(0)

        self.verticalLayout_3.addWidget(self.label_5)

        self.queue_list = QVBoxLayout()
        self.queue_list.setObjectName(u"queue_list")

        self.verticalLayout_3.addLayout(self.queue_list)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.gridLayout_2.addWidget(self.widget, 0, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.container)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BitBeat Music Player", None))
        self.label.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_13.setText("")
        self.album_cover.setText(QCoreApplication.translate("MainWindow", u"Album", None))
        self.song_title_label.setText(QCoreApplication.translate("MainWindow", u"ReI", None))
        self.song_artist_label.setText(QCoreApplication.translate("MainWindow", u"The Oral Cigarettes", None))
        self.btn_lyrics.setText("")
        self.btn_volume.setText("")
        self.btn_volume_muted.setText("")
        self.btn_shuffle.setText("")
        self.btn_previous.setText("")
        self.btn_play.setText("")
        self.btn_pause.setText("")
        self.btn_next.setText("")
        self.btn_favorite.setText("")
        self.current_duration_label.setText(QCoreApplication.translate("MainWindow", u"-:-", None))
        self.total_duration_label.setText(QCoreApplication.translate("MainWindow", u"-:-", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.page_title_label.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Favorites", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Queue", None))
    # retranslateUi

