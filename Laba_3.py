#!/urs/bin/python3
#-*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from Encoding import *


# Класс отвечающий за стартовое окно
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("qt_login.ui", self)
        self.login()

    def login(self):
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_btn.clicked.connect(lambda: self.personal_ac())
        self.registr_btn.clicked.connect(lambda: self.registr())

    def personal_ac(self):
        username = self.line_username.text().strip()
        password = self.line_password.text()
        if check_login(username, password):
            self.line_username.setText('')
            self.line_password.setText('')
            widget.addWidget(account_window)
            widget.setFixedWidth(850)
            widget.setFixedHeight(700)
            widget.setCurrentWidget(account_window)
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка\t\t\t\t\t")
            error.setText("Введен неверный логин или пароль.")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

    def registr(self):
        self.line_username.setText('')
        self.line_password.setText('')
        widget.setCurrentWidget(new_ac_window)

# Класс отвечающий за окно регистрации
class Registration(QMainWindow):
    def __init__(self):
        super(Registration, self).__init__()
        loadUi("qt_registration.ui", self)
        self.registration()

    def registration(self):
        self.new_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.replay_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_create.clicked.connect(lambda: self.login_window(True))
        self.back_btn.clicked.connect(lambda: self.login_window(False))


    def login_window(self, flag):
        if flag:
            username = self.new_username.text().strip()
            password = self.new_password.text()
            replay_password = self.replay_password.text()
            if password != replay_password:
                error = QMessageBox()
                error.setWindowTitle("Ошибка\t\t\t\t\t")
                error.setText("Пароли не совпадают!")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()
                return False
            registr = check_registr(username, password)
            if registr ==True:
                flag = False
            else:
                error = QMessageBox()
                error.setWindowTitle("Ошибка\t\t\t\t\t")
                error.setText("Введены неверный данные!")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.setDetailedText(" Требования к паролю:\n"
                                      "1) Пароль может состоять из: \n"
                                      "- Латинского алфавита (a-z; A-Z)\n"
                                      "- знаков препинания ('.', '!', '?', ',', '_')\n"
                                      "- цифр (0-9)\n"
                                      "2) Длина пароля должна быть не менее 8 и не более 30\n"
                                      "Требования к логину: \n"
                                      " Длина логина должна быть не менее 2 и не более 50\n\n"
                                      "Примечание: Если все требования выполняются, но программа выдает ошибку. Это значит,"
                                      " что пользователь с таким логином или паролем уже существует.")
                error.exec_()
        if not flag:
            self.new_username.setText('')
            self.new_password.setText('')
            self.replay_password.setText('')
            return widget.setCurrentWidget(login_window)

# Класс отвечающий за личный кабинет
class Personal_account(QMainWindow):
    def __init__(self):
        super(Personal_account, self).__init__()
        loadUi("qt_personal_ac.ui", self)
        self.encrypt_btn.clicked.connect(lambda: self.encryption())
        self.dencrypt_btn.clicked.connect(lambda: self.dencryption())
        self.exit_btn.clicked.connect(lambda: self.exit())

        self.encrypt_text.setAcceptRichText(False)
        self.dencrypt_text.setAcceptRichText(False)
        self.encrypt_text.setPlaceholderText("Введите текст (ТОЛЬКО АНГЛИЙСКИЙ ЯЗЫК И ЦИФРЫ), который надо зашифровать")
        self.dencrypt_text.setPlaceholderText("Введите текст (ТОЛЬКО ЦИФРЫ), который надо расшифровать")

    def exit(self):
        error = QMessageBox()
        error.setWindowTitle("Предупреждение\t\t\t\t\t")
        error.setText("Вы уверены что хотите выйти из лчного кабинета?")
        error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        error.buttonClicked.connect(self.click_btn)
        error.exec_()

    def click_btn(self, btn):
        if btn.text() == 'OK':
            self.encrypt_text.setText("")
            self.dencrypt_text.setText("")
            widget.removeWidget(account_window)
            widget.setFixedWidth(560)
            widget.setFixedHeight(350)
            widget.setCurrentWidget(login_window)

    def encryption(self):
        enc_text = self.encrypt_text.toPlainText()

        if enc_text != 0:
            cyphred = []  # тут будет хранится зашифрованный текст
            gost = Crypt(key, blocks)
            s = []

            # Читаем текст из поля ввода и шифруем каждую букву
            for byte in str(enc_text):
                s.append(ord(byte))
            for x in s:
                cyphred.append(gost.encrypt(x))

            with open('enc.txt', 'r+', encoding='utf8') as file:
                print(*cyphred, file=file)
                print("Файл зашифрован")
        else:
            self.error_text()


    def error_text(self):
        error = QMessageBox()
        error.setWindowTitle("Ошибка\t\t\t\t\t")

        error.setText("Введен неверный текст.")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.setDetailedText(
                              "Текст не должен быть пустым\n"
                              )
        error.exec_()

    def dencryption(self):
        denc_text = self.dencrypt_text.toPlainText()

        if denc_text != 0:
            decyphred = []  # тут будет хранится зашифрованный текст
            gost = Crypt(key, blocks)
            s = denc_text
            # Читаем текст из поля ввода и расшифровываем каждую букву
            for x in s.split():
                #  расшифровываем текст из файла и добавляем его в список
                decyphred.append(gost.decrypt(int(x)))
            try:
                with open("denc.txt", 'wb') as file:
                    # объеденяем расшифрованные символы в строку и записываем в файл
                    file.write(bytes(decyphred))
                print("Файл расшифрован")
            except:
                print(f"Не удалось открыть файл ")
                return
        else:
            self.error_text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login()
    new_ac_window = Registration()
    account_window = Personal_account()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(login_window)
    widget.addWidget(new_ac_window)
    widget.show()
    sys.exit(app.exec_())