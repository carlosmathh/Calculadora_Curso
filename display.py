import math
from main_window import MainWindow
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout
from PySide6.QtCore import Qt, Slot, Signal
from variables import BIG_SIZE, MEDIUM_SIZE, SMALL_SIZE, TEXT_MARGING, MINIMUM_WIDTH
from utils import isNumOrDot, isEmpty, isNumber, convertToInt


class LineEdit(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"Font-size: {BIG_SIZE}px")
        self.setMinimumHeight(BIG_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(
            *[TEXT_MARGING for i in range(4)]
        )  # [TEXT_MARGING, TEXT_MARGING, TEXT_MARGING, TEXT_MARGING]

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape]
        isOperator = key in [
            KEYS.Key_Plus,
            KEYS.Key_Minus,
            KEYS.Key_Slash,
            KEYS.Key_Asterisk,
            KEYS.Key_P,
        ]

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()

        if isDelete:
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()

        if isOperator:
            if text.lower() == "p":
                text = "^"
            self.operatorPressed.emit(text)

            return event.ignore()

        # NÃO PASSSAR DAQUI SE NÃO TIVER TEXTO
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()


class Info(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"Font-size: {SMALL_SIZE}px")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)


class Buttom(QPushButton):

    def __init__(self, text: str):
        super().__init__(text)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):

    def __init__(self, display: QLineEdit, info: Info, window: MainWindow):
        super().__init__()

        self._gridMask = [
            ["C", "◀", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["NE", "0", ".", "="],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ""
        self._initialEquation = "Calcule"
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._initialEquation
        self._make_number()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _make_number(self):
        self.display.eqPressed.connect(self._equalExponentiation)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertTextLineEdit)
        self.display.operatorPressed.connect(self._configLeftOp)

        for i, row in enumerate(self._gridMask):
            for j, colunm_text in enumerate(row):
                buttom = Buttom(colunm_text)
                if not isNumOrDot(colunm_text) and not isEmpty(colunm_text):
                    buttom.setProperty("cssClass", "specialButton")
                    self._configEspecialButton(buttom)

                self.addWidget(buttom, i, j)
                slot = self._makeSlot(self._insertTextLineEdit, colunm_text)
                self._connectClicked(buttom, slot)

    def _connectClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configEspecialButton(self, button):
        text = button.text()
        if text == "C":
            self._connectClicked(button, self._clear)

        if text == "◀":
            self._connectClicked(button, self.display.backspace)

        if text == "NE":
            self._connectClicked(button, self._invertNumber)

        if text in "+-/*^":
            self._connectClicked(button, self._makeSlot(self._configLeftOp, text))

        if text == "=":
            self._connectClicked(button, self._equalExponentiation)

    @Slot()
    def _makeSlot(self, func, *args):
        @Slot(bool)
        def slot():
            func(*args)

        return slot

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isNumber(displayText):
            return

        number = convertToInt(displayText) * -1
        self.display.setText(str(number))

    @Slot()
    def _insertTextLineEdit(self, text):
        newValue = self.display.text() + text
        if not isNumber(newValue):
            # self._showInfo("Deve ser numero")
            return
        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._initialEquation
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text()
        self.display.clear()
        self.display.setFocus()

        if not isNumber(displayText) and self._left is None:
            self._showError("ATENÇÃO: Calculo sem número")
            return

        if self._left is None:
            self._left = convertToInt(displayText)
        self._op = text
        self.equation = f"{self._left} {self._op} ??"

    @Slot()
    def _equalExponentiation(self):
        displayText = self.display.text()
        if not isNumber(displayText) or self._left is None:
            self._showInfo("AVISO: Conta incompleta")
            self.display.setFocus()

            return

        self._right = convertToInt(displayText)
        self.equation = f"{self._left} {self._op} {self._right}"
        result = "error"
        try:
            if "^" in self.equation and isinstance(self._left, int | float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)

        except ZeroDivisionError:
            self._showError("ATENÇÃO: Não pode dividir por zero")

        except OverflowError:
            self._showError("ATENÇÃO: Numero muito grande para exibir")

        self.display.clear()
        self.info.setText(f"{self.equation} = {result}")
        self._left = result
        self._right = None
        self.display.setFocus()

        if result == "error":
            self._left = None

    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _makeDialog(self, text):
        messegeBox = self.window.messageBox()
        messegeBox.setText(text)
        messegeBox.setStandardButtons(messegeBox.StandardButton.Ok)
        messegeBox.button(messegeBox.StandardButton.Ok).setText("Beleza")
        return messegeBox

    def _showError(self, text):
        messegeBox = self._makeDialog(text)
        messegeBox.setIcon(messegeBox.Icon.Critical)
        messegeBox.exec()
        self.display.setFocus()

    def _showInfo(self, text):
        messegeBox = self._makeDialog(text)
        messegeBox.setIcon(messegeBox.Icon.Information)
        messegeBox.exec()
        self.display.setFocus()
