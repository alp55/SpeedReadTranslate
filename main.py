import sys
import time
from PyQt5 import QtWidgets, QtGui, QtCore
from googletrans import Translator

class TranslatorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_TranslatorApp()
        self.ui.setupUi(self)

        self.ui.translate_button.clicked.connect(self.translate_and_display)

    def translate_and_display(self):
        text = self.ui.input_text.toPlainText()
        font_size = self.ui.font_size_spinbox.value()
        speed_text = self.ui.speed_combo_box.currentText()
        words_per_minute = int(speed_text.split()[1])  # Dakikada kelime sayısı
        translator = Translator()
        english_words = text.split()
        word_time = 60 / words_per_minute
        for eng_word in english_words:
            tr_word = translator.translate(eng_word, src='en', dest='tr').text
            self.ui.translation_label.setText(f'{eng_word}')
            font = QtGui.QFont()
            font.setPointSize(font_size)
            self.ui.translation_label.setFont(font)
            QtWidgets.QApplication.processEvents()
              # Kelime başına süre hesaplaması
            time.sleep(word_time)
            self.ui.translation_label.setText(f'{tr_word}')
            QtWidgets.QApplication.processEvents()
            time.sleep(word_time)

class Ui_TranslatorApp(object):
    def setupUi(self, TranslatorApp):
        TranslatorApp.setObjectName("TranslatorApp")
        TranslatorApp.resize(416, 506)
        self.verticalLayout = QtWidgets.QVBoxLayout(TranslatorApp)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_text = QtWidgets.QTextEdit(TranslatorApp)
        self.input_text.setObjectName("input_text")
        self.verticalLayout.addWidget(self.input_text)
        self.translate_button = QtWidgets.QPushButton(TranslatorApp)
        self.translate_button.setObjectName("translate_button")
        self.verticalLayout.addWidget(self.translate_button)
        self.translation_label = QtWidgets.QLabel(TranslatorApp)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.translation_label.setFont(font)
        self.translation_label.setText("")
        self.translation_label.setObjectName("translation_label")
        self.verticalLayout.addWidget(self.translation_label, 0, QtCore.Qt.AlignHCenter)
        self.frame = QtWidgets.QFrame(TranslatorApp)
        self.frame.setMinimumSize(QtCore.QSize(0, 30))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.font_size_spinbox = QtWidgets.QSpinBox(self.frame)
        self.font_size_spinbox.setGeometry(QtCore.QRect(190, 0, 211, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.font_size_spinbox.sizePolicy().hasHeightForWidth())
        self.font_size_spinbox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.font_size_spinbox.setFont(font)
        self.font_size_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.font_size_spinbox.setMinimum(14)
        self.font_size_spinbox.setMaximum(72)
        self.font_size_spinbox.setObjectName("font_size_spinbox")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 5, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.frame)
        self.speed_combo_box = QtWidgets.QComboBox(TranslatorApp)
        self.speed_combo_box.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.speed_combo_box.setFrame(False)
        self.speed_combo_box.setModelColumn(0)
        self.speed_combo_box.setObjectName("speed_combo_box")
        self.speed_combo_box.addItem("")
        self.speed_combo_box.addItem("")
        self.speed_combo_box.addItem("")
        self.speed_combo_box.addItem("")
          
        self.verticalLayout.addWidget(self.speed_combo_box)

        self.retranslateUi(TranslatorApp)
        QtCore.QMetaObject.connectSlotsByName(TranslatorApp)

    def retranslateUi(self, TranslatorApp):
        _translate = QtCore.QCoreApplication.translate
        TranslatorApp.setWindowTitle(_translate("TranslatorApp", "SpeedReadTranslate"))
        self.translate_button.setText(_translate("TranslatorApp", "Çevir"))
        self.label.setText(_translate("TranslatorApp", "KELİME BOYUTU :"))
        self.speed_combo_box.setItemText(0, _translate("TranslatorApp", " Dakikada 100 kelime"))
        self.speed_combo_box.setItemText(1, _translate("TranslatorApp", " Dakikada 200 kelime"))
        self.speed_combo_box.setItemText(2, _translate("TranslatorApp", " Dakikada 300 kelime"))
        self.speed_combo_box.setItemText(3, _translate("TranslatorApp", " Dakikada 400 kelime"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = TranslatorApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
