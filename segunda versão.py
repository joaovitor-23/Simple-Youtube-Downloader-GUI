# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress

class Ui_TELA_inicial(object):
    def setupUi(self, TELA_inicial):
        TELA_inicial.setObjectName("TELA_inicial")
        TELA_inicial.resize(490, 204)
        self.centralwidget = QtWidgets.QWidget(TELA_inicial)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(350, 100, 101, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BOX_playlist = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BOX_playlist.setFont(font)
        self.BOX_playlist.setObjectName("BOX_playlist")
        self.horizontalLayout.addWidget(self.BOX_playlist, 0, QtCore.Qt.AlignHCenter)
        self.URL_line = QtWidgets.QLineEdit(self.centralwidget)
        self.URL_line.setGeometry(QtCore.QRect(40, 50, 411, 31))
        self.URL_line.setInputMask("")
        self.URL_line.setText("")
        self.URL_line.setObjectName("URL_line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.BTN_baixar = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_baixar.setGeometry(QtCore.QRect(210, 160, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BTN_baixar.setFont(font)
        self.BTN_baixar.setObjectName("BTN_baixar")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(39, 100, 91, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.BTN_audio = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BTN_audio.setFont(font)
        self.BTN_audio.setObjectName("BTN_audio")
        self.verticalLayout.addWidget(self.BTN_audio, 0, QtCore.Qt.AlignHCenter)
        self.BTN_video = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BTN_video.setFont(font)
        self.BTN_video.setObjectName("BTN_video")
        self.verticalLayout.addWidget(self.BTN_video, 0, QtCore.Qt.AlignHCenter)
        TELA_inicial.setCentralWidget(self.centralwidget)

        self.retranslateUi(TELA_inicial)
        QtCore.QMetaObject.connectSlotsByName(TELA_inicial)

    def retranslateUi(self, TELA_inicial):
        _translate = QtCore.QCoreApplication.translate
        TELA_inicial.setWindowTitle(_translate("TELA_inicial", "MainWindow"))
        self.BOX_playlist.setText(_translate("TELA_inicial", "Playlist"))
        self.label.setText(_translate("TELA_inicial", "URL:"))
        self.BTN_baixar.setText(_translate("TELA_inicial", "Baixar"))
        self.BTN_audio.setText(_translate("TELA_inicial", "Audio"))
        self.BTN_video.setText(_translate("TELA_inicial", "Video"))


        self.BTN_baixar.clicked.connect(self.baixar)




    def baixar(self):
        url = self.URL_line.text().strip() ## CAPTURA O TEXTO DA EDIT LINE

        if not url:
            self.mostrar_mensagem("Por favor, insira uma URL válida.")
            return

        if self.BOX_playlist.isChecked():

            if self.BTN_audio.isChecked():  ## VERIFICA SE BOTAO RADIO FOI SELECIONANDO
                self.playlist_baixar_audio(url)  ## CHAMA A FUNÇAO DE playlist AUDIO

            elif self.BTN_video.isChecked():  ## VERIFICA SE BOTAO RADIO FOI SELECIONANDO
                self.playlist_baixar_video(url)  ## CHAMA A FUNÇAO DE playlist VIDEO

            else:
                self.mostrar_mensagem("Por favor, selecione Audio ou Video.")

        elif self.BTN_audio.isChecked(): ## VERIFICA SE BOTAO RADIO FOI SELECIONANDO
            self.baixar_audio(url) ## CHAMA A FUNÇAO DE AUDIO

        elif self.BTN_video.isChecked(): ## VERIFICA SE BOTAO RADIO FOI SELECIONANDO
            self.baixar_video(url) ## CHAMA A FUNÇAO DE VIDEO

        else:
            self.mostrar_mensagem("Por favor, selecione Audio ou Video.")

    def baixar_audio(self, url):

        yt = YouTube(url, on_progress_callback=on_progress)
        ys = yt.streams.get_audio_only()
        ys.download()

        # # Aqui você implementaria a lógica para baixar o áudio

    def baixar_video(self, url):

        yt = YouTube(url, on_progress_callback=on_progress)
        ys = yt.streams.get_highest_resolution()
        ys.download()

        # # Aqui você implementaria a lógica para baixar o vídeo

    def playlist_baixar_audio(self, url):
        pl = Playlist(url)
        for video in pl.videos:

            ys = video.streams.get_audio_only()
            ys.download()

    def playlist_baixar_video(self, url):
        pl = Playlist(url)
        for video in pl.videos:
            ys = video.streams.get_highest_resolution()
            ys.download()

    def mostrar_mensagem(self, mensagem):

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(mensagem)
        msg_box.setWindowTitle("Aviso")
        msg_box.exec_()

    def mostrar_mensagem(self, mensagem):

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(mensagem)
        msg_box.setWindowTitle("Aviso")
        msg_box.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TELA_inicial = QtWidgets.QMainWindow()
    ui = Ui_TELA_inicial()
    ui.setupUi(TELA_inicial)
    TELA_inicial.show()
    sys.exit(app.exec_())
