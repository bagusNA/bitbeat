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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)
import assets_rc
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(956, 648)
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
        self.widget_3 = QWidget(self.container)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(24)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.song_info = QHBoxLayout()
        self.song_info.setSpacing(24)
        self.song_info.setObjectName(u"song_info")
        self.song_info.setContentsMargins(0, -1, 0, -1)
        self.placeholder_album_cover = QLabel(self.widget_3)
        self.placeholder_album_cover.setObjectName(u"placeholder_album_cover")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.placeholder_album_cover.sizePolicy().hasHeightForWidth())
        self.placeholder_album_cover.setSizePolicy(sizePolicy)
        self.placeholder_album_cover.setMinimumSize(QSize(64, 64))
        self.placeholder_album_cover.setMaximumSize(QSize(64, 64))
        self.placeholder_album_cover.setScaledContents(False)
        self.placeholder_album_cover.setAlignment(Qt.AlignCenter)

        self.song_info.addWidget(self.placeholder_album_cover)

        self.song_info_labels = QVBoxLayout()
        self.song_info_labels.setSpacing(0)
        self.song_info_labels.setObjectName(u"song_info_labels")
        self.song_info_labels.setContentsMargins(0, -1, -1, -1)
        self.song_title_label = QLabel(self.widget_3)
        self.song_title_label.setObjectName(u"song_title_label")
        self.song_title_label.setMinimumSize(QSize(0, 0))
        self.song_title_label.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.song_title_label.setFont(font)
        self.song_title_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.song_info_labels.addWidget(self.song_title_label)

        self.song_artist_label = QLabel(self.widget_3)
        self.song_artist_label.setObjectName(u"song_artist_label")
        self.song_artist_label.setMaximumSize(QSize(300, 16777215))
        font1 = QFont()
        font1.setPointSize(8)
        self.song_artist_label.setFont(font1)
        self.song_artist_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.song_info_labels.addWidget(self.song_artist_label)


        self.song_info.addLayout(self.song_info_labels)


        self.gridLayout_3.addLayout(self.song_info, 0, 0, 1, 1)

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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/playlist-shuffle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_shuffle.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_shuffle)

        self.btn_previous = QPushButton(self.widget_3)
        self.btn_previous.setObjectName(u"btn_previous")
        self.btn_previous.setMinimumSize(QSize(48, 32))
        self.btn_previous.setMaximumSize(QSize(32, 32))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/player-start-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_previous.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_previous)

        self.btn_play = QPushButton(self.widget_3)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setMinimumSize(QSize(48, 32))
        self.btn_play.setMaximumSize(QSize(32, 32))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/player-play-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_play.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btn_play)

        self.btn_pause = QPushButton(self.widget_3)
        self.btn_pause.setObjectName(u"btn_pause")
        self.btn_pause.setEnabled(True)
        self.btn_pause.setMinimumSize(QSize(48, 32))
        self.btn_pause.setMaximumSize(QSize(32, 32))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/player-pause-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pause.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.btn_pause)

        self.btn_next = QPushButton(self.widget_3)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setMinimumSize(QSize(48, 32))
        self.btn_next.setMaximumSize(QSize(32, 32))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/player-end-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.btn_next)

        self.btn_favourited = QPushButton(self.widget_3)
        self.btn_favourited.setObjectName(u"btn_favourited")
        self.btn_favourited.setMinimumSize(QSize(48, 32))
        self.btn_favourited.setMaximumSize(QSize(48, 32))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/heart-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_favourited.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.btn_favourited)

        self.btn_not_favourited = QPushButton(self.widget_3)
        self.btn_not_favourited.setObjectName(u"btn_not_favourited")
        self.btn_not_favourited.setMinimumSize(QSize(48, 32))
        self.btn_not_favourited.setMaximumSize(QSize(32, 32))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/heart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_not_favourited.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.btn_not_favourited)


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
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/playlist.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lyrics.setIcon(icon8)

        self.horizontalLayout.addWidget(self.btn_lyrics)

        self.btn_volume = QPushButton(self.widget_3)
        self.btn_volume.setObjectName(u"btn_volume")
        self.btn_volume.setMinimumSize(QSize(48, 32))
        self.btn_volume.setMaximumSize(QSize(48, 32))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/volume-up-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_volume.setIcon(icon9)

        self.horizontalLayout.addWidget(self.btn_volume)

        self.btn_volume_muted = QPushButton(self.widget_3)
        self.btn_volume_muted.setObjectName(u"btn_volume_muted")
        self.btn_volume_muted.setMinimumSize(QSize(48, 32))
        self.btn_volume_muted.setMaximumSize(QSize(48, 32))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/volume-off-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_volume_muted.setIcon(icon10)

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

        self.gridLayout_3.setColumnStretch(0, 1)

        self.gridLayout_2.addWidget(self.widget_3, 1, 0, 1, 3)

        self.main_widget = QWidget(self.container)
        self.main_widget.setObjectName(u"main_widget")
        self.gridLayout_4 = QGridLayout(self.main_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.view_slot = QStackedWidget(self.main_widget)
        self.view_slot.setObjectName(u"view_slot")

        self.gridLayout_4.addWidget(self.view_slot, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.main_widget, 0, 1, 1, 1)

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
        font2 = QFont()
        font2.setPointSize(16)
        self.label.setFont(font2)
        self.label.setPixmap(QPixmap(u":/images/images/logo-compact.svg"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 24, -1, 0)
        self.btn_home = QPushButton(self.collapsed_sidebar_widget)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(64, 64))
        self.btn_home.setMaximumSize(QSize(64, 64))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon11)
        self.btn_home.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.btn_home)

        self.btn_playlist = QPushButton(self.collapsed_sidebar_widget)
        self.btn_playlist.setObjectName(u"btn_playlist")
        self.btn_playlist.setMinimumSize(QSize(64, 64))
        self.btn_playlist.setMaximumSize(QSize(64, 64))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/music-album.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_playlist.setIcon(icon12)
        self.btn_playlist.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.btn_playlist)

        self.btn_favourite = QPushButton(self.collapsed_sidebar_widget)
        self.btn_favourite.setObjectName(u"btn_favourite")
        self.btn_favourite.setMinimumSize(QSize(64, 64))
        self.btn_favourite.setMaximumSize(QSize(64, 64))
        self.btn_favourite.setIcon(icon7)
        self.btn_favourite.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.btn_favourite)

        self.btn_setting = QPushButton(self.collapsed_sidebar_widget)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setMinimumSize(QSize(64, 64))
        self.btn_setting.setMaximumSize(QSize(64, 64))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting.setIcon(icon13)
        self.btn_setting.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.btn_setting)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 309, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.collapsed_sidebar_widget, 0, 0, 1, 1)

        self.queue_widget = QWidget(self.container)
        self.queue_widget.setObjectName(u"queue_widget")
        self.queue_widget.setMinimumSize(QSize(250, 0))
        self.queue_widget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.queue_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(24, 24, 24, 0)
        self.queue_title_label = QLabel(self.queue_widget)
        self.queue_title_label.setObjectName(u"queue_title_label")
        self.queue_title_label.setMaximumSize(QSize(16777215, 48))
        self.queue_title_label.setFont(font2)
        self.queue_title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.queue_title_label.setMargin(0)

        self.verticalLayout_3.addWidget(self.queue_title_label)

        self.queue_length_info_label = QLabel(self.queue_widget)
        self.queue_length_info_label.setObjectName(u"queue_length_info_label")
        font3 = QFont()
        font3.setPointSize(9)
        self.queue_length_info_label.setFont(font3)

        self.verticalLayout_3.addWidget(self.queue_length_info_label)

        self.scrollArea = QScrollArea(self.queue_widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 202, 472))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.queue_list = QVBoxLayout()
        self.queue_list.setSpacing(16)
        self.queue_list.setObjectName(u"queue_list")
        self.queue_list.setContentsMargins(-1, 18, -1, -1)

        self.gridLayout.addLayout(self.queue_list, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.gridLayout_2.addWidget(self.queue_widget, 0, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.container)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BitBeat Music Player", None))
        self.placeholder_album_cover.setText(QCoreApplication.translate("MainWindow", u"Album", None))
        self.song_title_label.setText(QCoreApplication.translate("MainWindow", u"ReI", None))
        self.song_artist_label.setText(QCoreApplication.translate("MainWindow", u"The Oral Cigarettes", None))
        self.btn_shuffle.setText("")
        self.btn_previous.setText("")
        self.btn_play.setText("")
        self.btn_pause.setText("")
        self.btn_next.setText("")
        self.btn_favourited.setText("")
        self.btn_not_favourited.setText("")
        self.current_duration_label.setText(QCoreApplication.translate("MainWindow", u"-:-", None))
        self.total_duration_label.setText(QCoreApplication.translate("MainWindow", u"-:-", None))
        self.btn_lyrics.setText("")
        self.btn_volume.setText("")
        self.btn_volume_muted.setText("")
        self.label.setText("")
        self.btn_home.setText("")
        self.btn_playlist.setText("")
        self.btn_favourite.setText("")
        self.btn_setting.setText("")
        self.queue_title_label.setText(QCoreApplication.translate("MainWindow", u"Queue", None))
        self.queue_length_info_label.setText("")
    # retranslateUi

