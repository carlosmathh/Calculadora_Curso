from pathlib import Path
import sys

if getattr(sys, "frozen", False):
    ROOT_DIR = Path(sys._MEIPASS)
else:
    ROOT_DIR = Path(__file__).parent

FILES_DIR = ROOT_DIR / "files"
FILE_ICON = FILES_DIR / "img_cal_v2.ico"


# Standard Sizes
BIG_SIZE = 35
MEDIUM_SIZE = 20
SMALL_SIZE = 17
TEXT_MARGING = 2
MINIMUM_WIDTH = 400


# colors
PRIMARY_COLOR = "#F28C28"  # laranja principal
DARKER_PRIMARY_COLOR = "#D97706"
DARKEST_PRIMARY_COLOR = "#B45309"

BLACK_MAIN = "#0F0F0F"
BLACK_SURFACE = "#1A1A1A"
BLACK_BUTTON = "#242424"

TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#B5B5B5"
