from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import src.Contants as Constants
from src.Controllers.ObfuscatorController import ObfuscatorController
from src.Widgets.DeleteableList import DeleteableList
from src.Params.DeleteableListParams import DeleteableListParams


ICON_PATH = './assets/icon.ico'

ADD_ICON_PATH = './assets/plus.png'
FOLDER_ICON_PATH = './assets/folder.png'

ADD_PRESSED_ICON_PATH = './assets/plus_pressed.png'
FOLDER_PRESSED_ICON_PATH = './assets/folder_pressed.png'

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 540

HORIZONTAL_PADDIND = 20
VERTICAL_PADDIND = 20

TITLE_Y_CORRECTION = 3

WIDGET_BACKGROUND_COLOR = '#2b2b2b'


class Obfuscator(QWidget):

    def __init__(self):
        super().__init__()
        self.folderIconPressed = None
        self.addIconPressed = None
        self.shouldMinifyCode = False
        self.binaryStringBTitle = None
        self.folderIcon = None
        self.controller = ObfuscatorController(self)
        self.binaryStringATitle = None
        self.binaryStringBInput = None
        self.binaryStringAInput = None
        self.pathsList = None
        self.listReferencesTitle = None
        self.addIcon = None
        self.referencesList = None
        self.ubuntuMonoFontFamily = None
        self.exoFontFamily = None
        self.windowIcon = None
        self.inputReference = None

    def render(self):
        self.loadResources()
        self.confWindow()
        self.confWidgets()
        self.show()

    def confWindow(self):
        self.setWindowTitle(Constants.WINDOW_TITLE)
        self.setWindowIcon(self.windowIcon)
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet("background-color: #3c3f41;")

    def loadResources(self):
        self.windowIcon = QIcon(ICON_PATH)
        self.addIcon = QIcon(ADD_ICON_PATH)
        self.folderIcon = QIcon(FOLDER_ICON_PATH)
        self.addIconPressed = QIcon(ADD_PRESSED_ICON_PATH)
        self.folderIconPressed = QIcon(FOLDER_PRESSED_ICON_PATH)

        font_id = QFontDatabase.addApplicationFont('./assets/exo-2.ttf')
        self.exoFontFamily = QFontDatabase.applicationFontFamilies(font_id)[0]

        font_id = QFontDatabase.addApplicationFont('./assets/ubuntu-mono.ttf')
        self.ubuntuMonoFontFamily = QFontDatabase.applicationFontFamilies(font_id)[0]

    def confWidgets(self):
        self.confListPathsTitle()
        self.confListPaths()
        self.confAddFilesBtn()
        self.confListReferencesTitle()
        self.confReferencesList()
        self.confInputReference()
        self.confAddReferenceBtn()
        self.confBinaryStringTitles()
        self.confBinaryStringInputs()
        self.confMinCheckbox()
        self.confObfuscateBtn()

    def confListPathsTitle(self):
        listPathsTitle = self.buildLabel(Constants.FILE_PATH_LIST, 15)
        listPathsTitle.move(HORIZONTAL_PADDIND + 5, VERTICAL_PADDIND - TITLE_Y_CORRECTION)
        listPathsTitle.setParent(self)

    def confListPaths(self):
        left, top = HORIZONTAL_PADDIND, VERTICAL_PADDIND + 33
        width, height = 450, 200
        deleteableListParams = DeleteableListParams(left, top, width, height, '#ffffff', WIDGET_BACKGROUND_COLOR,
                                                    self.ubuntuMonoFontFamily, True)
        self.pathsList = DeleteableList(self, deleteableListParams)

    def confAddFilesBtn(self):
        addFilesBtn = QPushButton(Constants.ADD_FILES)

        addFilesBtn.clicked.connect(self.AddFilesAction)
        addFilesBtn.move(350, 265)
        addFilesBtn.setFixedSize(120, 32)

        font = QFont(self.exoFontFamily, 12)
        font.setWeight(QFont.Bold)
        addFilesBtn.setFont(font)

        addFilesBtn.setIcon(self.folderIcon)
        addFilesBtn.setIconSize(QSize(27, 27))

        addFilesBtn.pressed.connect(lambda: addFilesBtn.setIcon(self.folderIconPressed))
        addFilesBtn.released.connect(lambda: addFilesBtn.setIcon(self.folderIcon))

        addFilesBtn.setStyleSheet('''
        QPushButton{
            color: white;
            background-color: #4ac788; 
            text-align:center; 
            display:flex; 
            align-items:center; 
            justify-content: center;
            border-top-left-radius: 7%;
            border-top-right-radius: 7%;
            border-bottom-left-radius: 7%;
            border-bottom-right-radius: 7%;
        }
        
        QPushButton:hover{
             background-color: #44eb97; 
        }
        
        QPushButton:pressed{
            color:  #4ac788;
            background-color: white; 
        }
        ''')

        addFilesBtn.setParent(self)

    def AddFilesAction(self):
        fileNames = self.showAndGetFileNames()
        self.pathsList.addStringItemList(fileNames)

    def confListReferencesTitle(self):
        self.listReferencesTitle = self.buildLabel(Constants.REFERENCES_LIST, 15)
        self.listReferencesTitle.move(WINDOW_WIDTH - HORIZONTAL_PADDIND - 275, VERTICAL_PADDIND - TITLE_Y_CORRECTION)
        self.listReferencesTitle.setParent(self)

    def confReferencesList(self):
        left, top = WINDOW_WIDTH - HORIZONTAL_PADDIND - 280, VERTICAL_PADDIND + 33
        width, height = 280, 420
        deleteableListParams = DeleteableListParams(left, top, width, height, '#ffffff', WIDGET_BACKGROUND_COLOR,
                                                    self.ubuntuMonoFontFamily, False)
        self.referencesList = DeleteableList(self, deleteableListParams)

    def confInputReference(self):
        self.inputReference = self.buildLineEdit({
            'top-left': 7,
            'top-right': 0,
            'bottom-left': 7,
            'bottom-right': 0,
        })
        self.inputReference.move(WINDOW_WIDTH - HORIZONTAL_PADDIND - 280, WINDOW_HEIGHT - VERTICAL_PADDIND - 30)
        self.inputReference.setFixedSize(250, 30)
        self.inputReference.setParent(self)
        self.inputReference.returnPressed.connect(lambda: self.insertNewVariableAction())

    def confAddReferenceBtn(self):
        addReferenceBtn = QPushButton()
        addReferenceBtn.setIcon(self.addIcon)
        addReferenceBtn.clicked.connect(self.insertNewVariableAction)

        addReferenceBtn.move(WINDOW_WIDTH - HORIZONTAL_PADDIND - 30, WINDOW_HEIGHT - VERTICAL_PADDIND - 30)
        addReferenceBtn.setFixedSize(30, 30)
        addReferenceBtn.setIconSize(QSize(15, 15))

        addReferenceBtn.pressed.connect(lambda: addReferenceBtn.setIcon(self.addIconPressed))
        addReferenceBtn.released.connect(lambda: addReferenceBtn.setIcon(self.addIcon))

        addReferenceBtn.setStyleSheet(
            '''
            QPushButton{
                color: white;
                background-color: #4ac788;
                border-top-left-radius: 0%;
                border-top-right-radius: 7%;
                border-bottom-left-radius: 0%;
                border-bottom-right-radius: 7%;
            }
            
            QPushButton:hover{
                 background-color: #44eb97; 
            }
            
            QPushButton:pressed{
                color:  #4ac788;
                background-color: white; 
            }
            '''
        )

        addReferenceBtn.setParent(self)

    def insertNewVariableAction(self):
        referenceName = self.inputReference.text()
        self.inputReference.setText('')
        self.referencesList.addStringItem(referenceName)

    def confObfuscateBtn(self):
        obfuscateBtn = QPushButton(Constants.START)
        obfuscateBtn.clicked.connect(self.controller.obfuscateAction)

        obfuscateBtn.move(HORIZONTAL_PADDIND, WINDOW_HEIGHT - VERTICAL_PADDIND - 32)
        obfuscateBtn.setFixedSize(140, 32)

        font = QFont(self.exoFontFamily, 14)
        font.setWeight(QFont.Bold)
        obfuscateBtn.setFont(font)

        obfuscateBtn.setStyleSheet('''
            QPushButton{
                color: black;
                background-color: white;
                border-top-left-radius: 7%;
                border-top-right-radius: 7%;
                border-bottom-left-radius: 7%;
                border-bottom-right-radius: 7%;
            }
            
            QPushButton:hover{
                 background-color: #4ac788; 
            }
            
            QPushButton:pressed{
                color: #4ac788;
                background-color: white; 
            }
        ''')

        obfuscateBtn.setParent(self)

    def showAndGetFileNames(self) -> list:
        fileNames, _ = QFileDialog.getOpenFileNames(self, "Select files", "", "All files (*)")
        return fileNames

    def confBinaryStringTitles(self):
        self.binaryStringATitle = self.buildLabel(Constants.STRING_A, 12)
        self.binaryStringATitle.move(95, 314 - TITLE_Y_CORRECTION)
        self.binaryStringATitle.setMaximumSize(QSize(120, 30))
        self.binaryStringATitle.setParent(self)

        self.binaryStringBTitle = self.buildLabel(Constants.STRING_B, 12)
        self.binaryStringBTitle.move(277, 314 - TITLE_Y_CORRECTION)
        self.binaryStringBTitle.setMaximumSize(QSize(120, 30))
        self.binaryStringBTitle.setParent(self)

    def confBinaryStringInputs(self):
        self.binaryStringAInput = self.buildBinaryStringInput()
        self.binaryStringAInput.move(90, 340)
        self.binaryStringAInput.setParent(self)

        self.binaryStringBInput = self.buildBinaryStringInput()
        self.binaryStringBInput.move(270, 340)
        self.binaryStringBInput.setParent(self)

        self.binaryStringAInput.setAlignment(QtCore.Qt.AlignCenter)
        self.binaryStringBInput.setAlignment(QtCore.Qt.AlignCenter)

    def confMinCheckbox(self):
        minCheckbox = QCheckBox(Constants.MINIFY_CODE, self)
        minCheckbox.move(180, 415)
        minCheckbox.setFixedSize(145, 25)
        font = QFont(self.exoFontFamily, 11)
        font.setWeight(QFont.Bold)
        minCheckbox.setFont(font)
        minCheckbox.setCheckState(False)
        minCheckbox.setStyleSheet(
            'QCheckBox{'
                'color: white;'
            '}'
            'QCheckBox::indicator {'
                'width: 15px;'
                'height: 15px;'
                'border: 2px solid white;'
                'border-radius: 7%;'
                'background-color: #fc9619;'
            '}'
            'QCheckBox::indicator:unchecked {'
                'background-color: #fc9619;'
            '}'
            'QCheckBox::indicator:checked {'
                f'background-color: {WIDGET_BACKGROUND_COLOR};'
            '}'
        )
        minCheckbox.toggle()
        minCheckbox.stateChanged.connect(self.minCheckboxChange)

    def minCheckboxChange(self, state):
        self.shouldMinifyCode = state != Qt.Checked

    # BUILD FUNCTIONS

    def buildBinaryStringInput(self) -> QLineEdit:
        binaryStringInput = self.buildLineEdit({
            'top-left': 7,
            'top-right': 7,
            'bottom-left': 7,
            'bottom-right': 7,
        })
        binaryStringInput.setFixedSize(120, 30)
        return binaryStringInput

    def buildLineEdit(self, radiusSizes: dict = None) -> QLineEdit:
        lineEdit = QLineEdit()
        font = QFont(self.ubuntuMonoFontFamily, 14)
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

    def buildLabel(self, text: str, fontSize: int) -> QLabel:
        label = QLabel(text)
        font = QFont(self.exoFontFamily, fontSize)
        font.setWeight(QFont.Bold)
        label.setFont(font)
        label.setStyleSheet('color: white;')

        return label

    # GETTERS AND SETTERS

    def getFilePaths(self) -> list:
        return self.pathsList.getStringItems()

    def getReferences(self) -> list:
        return self.referencesList.getStringItems()

    def getStringA(self) -> str:
        return self.binaryStringAInput.text()

    def getStringB(self) -> str:
        return self.binaryStringBInput.text()

    def getShouldMinifyCode(self) -> bool:
        return self.shouldMinifyCode
