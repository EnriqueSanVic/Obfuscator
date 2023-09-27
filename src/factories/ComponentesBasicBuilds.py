from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from src.Contants import *

def buildBinaryStringInput() -> QLineEdit:
        binaryStringInput = buildLineEdit({
            'top-left': 7,
            'top-right': 7,
            'bottom-left': 7,
            'bottom-right': 7,
        })
        binaryStringInput.setFixedSize(120, 30)
        return binaryStringInput

def buildLineEdit(radiusSizes: dict | None = None) -> QLineEdit:
    lineEdit = QLineEdit()
    from src.Widgets.Obfuscator import ubuntuMonoFontFamily
    font = QFont(ubuntuMonoFontFamily, 13)
    lineEdit.setFont(font)

    if radiusSizes is None:
        lineEdit.setStyleSheet(
            'QLineEdit{'
            f'background-color: {WIDGET_BACKGROUND_COLOR};'
            'color: white;'
            'border: 2px solid white;'
            '}'
        )
    else:
        lineEdit.setStyleSheet(
            'QLineEdit{'
            f'background-color: {WIDGET_BACKGROUND_COLOR};'
            'color: white;'
            'border: 2px solid white;'
            f'border-top-left-radius: {radiusSizes.get("top-left", 0)}%;'
            f'border-top-right-radius: {radiusSizes.get("top-right", 0)}%;'
            f'border-bottom-left-radius: {radiusSizes.get("bottom-left", 0)}%;'
            f'border-bottom-right-radius: {radiusSizes.get("bottom-right", 0)}%;'
            '}'
        )

    return lineEdit

def buildLabel(text: str, fontSize: int, backgroundColor: str | None = None, foregroundColor=None,
                paddings: dict | None = None, radiusSizes: dict | None = None,
                font: QFont | None = None) -> QLabel:
    label = QLabel(text)

    styleSheet = ''

    if backgroundColor is not None:
        styleSheet += f'background-color: {backgroundColor};'

    if foregroundColor is None:
        foregroundColor = 'white'

    styleSheet += f'color: {foregroundColor};'

    if paddings is not None:
        styleSheet += f'padding-top: {paddings["top"]}px;'
        styleSheet += f'padding-bottom: {paddings["bottom"]}px;'
        styleSheet += f'padding-left: {paddings["left"]}px;'
        styleSheet += f'padding-right: {paddings["right"]}px;'

    if font is None:
        from src.Widgets.Obfuscator import exoFontFamily
        font = QFont(exoFontFamily, fontSize, weight=400)

    if radiusSizes is not None:
        styleSheet += f'border-top-left-radius: {radiusSizes.get("top-left", 0)}%;'
        styleSheet += f'border-top-right-radius: {radiusSizes.get("top-right", 0)}%;'
        styleSheet += f'border-bottom-left-radius: {radiusSizes.get("bottom-left", 0)}%;'
        styleSheet += f'border-bottom-right-radius: {radiusSizes.get("bottom-right", 0)}%;'

    label.setFont(font)

    label.setStyleSheet(styleSheet)

    return label