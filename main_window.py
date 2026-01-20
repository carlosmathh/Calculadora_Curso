from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox


class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setWindowTitle("Calculadora Carlos Prog")

        self.centra_widget = QWidget()

        self.vLayout = QVBoxLayout()
        self.centra_widget.setLayout(self.vLayout)

        self.setCentralWidget(self.centra_widget)

        # ultimas coisa

    def adjustFixedsize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
        # self.adjustFixedsize()

    def addToGridLayout(self, grid):
        self.vLayout.addWidget(grid)

    def messageBox(self):
        return QMessageBox(self)
