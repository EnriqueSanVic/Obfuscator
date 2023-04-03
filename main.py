from PyQt5.QtWidgets import QApplication
from src.Widgets.Obfuscator import Obfuscator


def main():
    app = QApplication([])
    obfuscator = Obfuscator()
    obfuscator.render()
    app.exec()


if __name__ == '__main__':
    main()
