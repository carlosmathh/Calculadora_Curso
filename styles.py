import qdarkstyle
from variables import (
    PRIMARY_COLOR,
    DARKER_PRIMARY_COLOR,
    DARKEST_PRIMARY_COLOR,
    BLACK_MAIN,
    BLACK_SURFACE,
    BLACK_BUTTON,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)

qss = f"""
/* =========================
   JANELA
========================= */
QMainWindow {{
    background-color: {BLACK_MAIN};
}}

/* =========================
   DISPLAY
========================= */
QLineEdit {{
    font-size: 32px;
    font-weight: bold;
    padding: 16px;
    border-radius: 14px;
    background-color: {BLACK_SURFACE};
    color: {TEXT_PRIMARY};
    border: 2px solid {PRIMARY_COLOR};
}}

/* =========================
   INFO LABEL
========================= */
QLabel {{
    font-size: 14px;
    color: {TEXT_SECONDARY};
    padding: 6px;
}}

/* =========================
   BOTÕES PADRÃO
========================= */
QPushButton {{
    font-size: 16px;
    font-weight: bold;
    padding: 14px;
    border-radius: 14px;
    background-color: {BLACK_BUTTON};
    color: {TEXT_PRIMARY};
    border: 1px solid #333333;
}}

QPushButton:hover {{
    background-color: #2E2E2E;
}}

QPushButton:pressed {{
    background-color: #1C1C1C;
}}

/* =========================
   BOTÕES ESPECIAIS
========================= */
QPushButton[cssClass="specialButton"] {{
    background-color: {PRIMARY_COLOR};
    color: black;
    font-size: 18px;
    border-radius: 16px;
    border: none;
}}

QPushButton[cssClass="specialButton"]:hover {{
    background-color: {DARKER_PRIMARY_COLOR};
}}

QPushButton[cssClass="specialButton"]:pressed {{
    background-color: {DARKEST_PRIMARY_COLOR};
}}
"""


def setupTheme(app):
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    app.setStyleSheet(app.styleSheet() + qss)
