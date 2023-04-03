from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from src.Contants import *
from src.Controllers.ObfuscatorController import ObfuscatorController
from src.Widgets.DeleteableList import DeleteableList
from src.Params.DeleteableListParams import DeleteableListParams

ICON_PATH = './assets/icon.ico'
ADD_ICON_PATH = './assets/plus.png'
FOLDER_ICON_PATH = './assets/folder.png'

ADD_PRESSED_ICON_PATH = './assets/plus_pressed.png'
FOLDER_PRESSED_ICON_PATH = './assets/folder_pressed.png'

CLOSE_ICON_PATH = './assets/close.png'
CLOSE_HOVER_ICON_PATH = './assets/close_hover.png'


class Obfuscator(QWidget):

    def __init__(self):
        super().__init__()
        self.controller = ObfuscatorController(self)
        self.offset = None
        self.closeIcon = None
        self.closeHoverIcon = None
        self.windowIcon = None
        self.folderIconPressed = None
        self.addIconPressed = None
        self.shouldMinifyCode = False
        self.binaryStringBTitle = None
        self.folderIcon = None
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
        self.conf()
        self.confWidgets()
        self.show()

    def conf(self):

        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(self.windowIcon)

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.setObjectName('ob-container')
        self.setStyleSheet('''
                #ob-container {
                    background-color: #3c3f41;
                    border: 1px solid white;
                    border-radius: 7%;
                }
        ''')

    def loadResources(self):
        self.windowIcon = QIcon(ICON_PATH)
        self.addIcon = QIcon(ADD_ICON_PATH)
        self.folderIcon = QIcon(FOLDER_ICON_PATH)
        self.closeIcon = QIcon(CLOSE_ICON_PATH)
        self.closeHoverIcon = QIcon(CLOSE_HOVER_ICON_PATH)
        self.addIconPressed = QIcon(ADD_PRESSED_ICON_PATH)
        self.folderIconPressed = QIcon(FOLDER_PRESSED_ICON_PATH)

        font_id = QFontDatabase.addApplicationFont('./assets/exo-2.ttf')
        self.exoFontFamily = QFontDatabase.applicationFontFamilies(font_id)[0]

        font_id = QFontDatabase.addApplicationFont('./assets/ubuntu-mono.ttf')
        self.ubuntuMonoFontFamily = QFontDatabase.applicationFontFamilies(font_id)[0]

    def confWidgets(self):
        self.confWindowTitle()
        self.confWindowControlButtons()
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

    def confWindowTitle(self):
        listPathsTitle = self.buildLabel(WINDOW_TITLE, 10, backgroundColor=f'{PRIMARY_COLOR}', foregroundColor=WIDGET_BACKGROUND_COLOR,
        paddings={
            'top': 5,
            'left': 10,
            'bottom': 5,
            'right': 10
        },
        radiusSizes={
                'top-left': 0,
                'top-right': 0,
                'bottom-left': 0,
                'bottom-right': 7
        }, font=QFont(self.ubuntuMonoFontFamily, 12, weight=QFont.Light))

        listPathsTitle.move(0, 0)

        listPathsTitle.setParent(self)

    def confWindowControlButtons(self):

        closeWindowBtn = QPushButton()

        closeWindowBtn.move(WINDOW_WIDTH - 60, 0)
        closeWindowBtn.setFixedSize(60, 35)

        closeWindowBtn.setStyleSheet(
            '''
            QPushButton{
                background-color: transparent;
            }
            
            QPushButton:hover{
                background-color: rgba(230, 230, 230, 0.24);
            }
            '''
        )

        closeWindowBtn.setIcon(self.closeIcon)
        closeWindowBtn.setIconSize(QSize(15, 15))

        closeWindowBtn.clicked.connect(lambda: exit(0))
        closeWindowBtn.pressed.connect(lambda: closeWindowBtn.setIcon(self.closeHoverIcon))
        closeWindowBtn.released.connect(lambda: closeWindowBtn.setIcon(self.closeIcon))

        closeWindowBtn.setParent(self)

    def confListPathsTitle(self):
        listPathsTitle = self.buildLabel(FILE_PATH_LIST, 15)
        listPathsTitle.move(HORIZONTAL_PADDING + 5, TOP_PADDING)
        listPathsTitle.setParent(self)

    def confListPaths(self):
        left, top = HORIZONTAL_PADDING, TOP_PADDING + 40
        width, height = 450, 200
        deleteableListParams = DeleteableListParams(left, top, width, height, '#ffffff', WIDGET_BACKGROUND_COLOR,
                                                    self.ubuntuMonoFontFamily, True)
        self.pathsList = DeleteableList(self, deleteableListParams)

    def confAddFilesBtn(self):
        addFilesBtn = QPushButton(ADD_FILES)

        addFilesBtn.clicked.connect(self.AddFilesAction)
        addFilesBtn.move(360, 295)
        addFilesBtn.setFixedSize(120, 32)

        font = QFont(self.exoFontFamily, 12, weight=QFont.Normal)
        addFilesBtn.setFont(font)

        addFilesBtn.setIcon(self.folderIcon)
        addFilesBtn.setIconSize(QSize(27, 27))

        addFilesBtn.pressed.connect(lambda: addFilesBtn.setIcon(self.folderIconPressed))
        addFilesBtn.released.connect(lambda: addFilesBtn.setIcon(self.folderIcon))

        addFilesBtn.setStyleSheet(
        'QPushButton{'
            'color: white;'
            f'background-color: {PRIMARY_COLOR};'
            'text-align:center; '
            'display:flex; '
            'align-items:center; '
            'justify-content: center;'
            'border-top-left-radius: 7%;'
            'border-top-right-radius: 7%;'
            'border-bottom-left-radius: 7%;'
            'border-bottom-right-radius: 7%;'
        '}' 
        '''
        QPushButton:hover{
             background-color: #44eb97; 
        }
        '''
        'QPushButton:pressed{'
            f'color:  {PRIMARY_COLOR};'
            'background-color: white; '
        '}'
        )

        addFilesBtn.setParent(self)

    def AddFilesAction(self):
        fileNames = self.showAndGetFileNames()
        self.pathsList.addStringItemList(fileNames)

    def confListReferencesTitle(self):
        self.listReferencesTitle = self.buildLabel(REFERENCES_LIST, 15)
        self.listReferencesTitle.move(WINDOW_WIDTH - HORIZONTAL_PADDING - 275, TOP_PADDING)
        self.listReferencesTitle.setParent(self)

    def confReferencesList(self):
        left, top = WINDOW_WIDTH - HORIZONTAL_PADDING - 280, TOP_PADDING + 40
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
        self.inputReference.move(WINDOW_WIDTH - HORIZONTAL_PADDING - 280, WINDOW_HEIGHT - BOTTOM_PADDING - 30)
        self.inputReference.setFixedSize(250, 30)
        self.inputReference.setParent(self)
        self.inputReference.returnPressed.connect(lambda: self.insertNewVariableAction())

    def confAddReferenceBtn(self):
        addReferenceBtn = QPushButton()
        addReferenceBtn.setIcon(self.addIcon)

        addReferenceBtn.move(WINDOW_WIDTH - HORIZONTAL_PADDING - 30, WINDOW_HEIGHT - BOTTOM_PADDING - 30)
        addReferenceBtn.setFixedSize(30, 30)
        addReferenceBtn.setIconSize(QSize(15, 15))

        addReferenceBtn.clicked.connect(self.insertNewVariableAction)
        addReferenceBtn.pressed.connect(lambda: addReferenceBtn.setIcon(self.addIconPressed))
        addReferenceBtn.released.connect(lambda: addReferenceBtn.setIcon(self.addIcon))

        addReferenceBtn.setStyleSheet(

            'QPushButton{'
                'color: white;'
                f'background-color: {PRIMARY_COLOR};'
                'border-top-left-radius: 0%;'
                'border-top-right-radius: 7%;'
                'border-bottom-left-radius: 0%;'
                'border-bottom-right-radius: 7%;'
            '}'
            '''
            QPushButton:hover{
                 background-color: #44eb97; 
            }
            '''
            'QPushButton:pressed{'
                f'color:  {PRIMARY_COLOR};'
                'background-color: white;'
            '}'

        )

        addReferenceBtn.setParent(self)

    def insertNewVariableAction(self):
        referenceName = self.inputReference.text()
        self.inputReference.setText('')
        self.referencesList.addStringItem(referenceName)

    def confObfuscateBtn(self):
        obfuscateBtn = QPushButton(START)
        obfuscateBtn.clicked.connect(self.controller.obfuscateAction)

        obfuscateBtn.move(HORIZONTAL_PADDING, WINDOW_HEIGHT - BOTTOM_PADDING - 32)
        obfuscateBtn.setFixedSize(140, 32)

        font = QFont(self.exoFontFamily, 14, weight=QFont.Normal)
        obfuscateBtn.setFont(font)

        obfuscateBtn.setStyleSheet(
            'QPushButton{'
                'color: black;'
                'background-color: white;'
                'border-top-left-radius: 7%;'
                'border-top-right-radius: 7%;'
                'border-bottom-left-radius: 7%;'
                'border-bottom-right-radius: 7%;'
            '}'
            
            'QPushButton:hover{'
                 f'background-color: {PRIMARY_COLOR}; '
            '}'
            
            'QPushButton:pressed{'
                f'color: {PRIMARY_COLOR};'
                'background-color: white; '
            '}'
       )

        obfuscateBtn.setParent(self)

    def showAndGetFileNames(self) -> list:
        fileNames, _ = QFileDialog.getOpenFileNames(self, "Select files", "", "All files (*)")
        return fileNames

    def confBinaryStringTitles(self):
        self.binaryStringATitle = self.buildLabel(STRING_A, 12)
        self.binaryStringATitle.move(120, 345 - TITLE_Y_CORRECTION)
        self.binaryStringATitle.setMaximumSize(QSize(120, 30))
        self.binaryStringATitle.setParent(self)

        self.binaryStringBTitle = self.buildLabel(STRING_B, 12)
        self.binaryStringBTitle.move(297, 345 - TITLE_Y_CORRECTION)
        self.binaryStringBTitle.setMaximumSize(QSize(120, 30))
        self.binaryStringBTitle.setParent(self)

    def confBinaryStringInputs(self):
        self.binaryStringAInput = self.buildBinaryStringInput()
        self.binaryStringAInput.move(110, 375)
        self.binaryStringAInput.setParent(self)

        self.binaryStringBInput = self.buildBinaryStringInput()
        self.binaryStringBInput.move(290, 375)
        self.binaryStringBInput.setParent(self)

        self.binaryStringAInput.setAlignment(QtCore.Qt.AlignCenter)
        self.binaryStringBInput.setAlignment(QtCore.Qt.AlignCenter)

    def confMinCheckbox(self):
        minCheckbox = QCheckBox(MINIFY_CODE, self)
        minCheckbox.move(195, 440)
        minCheckbox.setFixedSize(145, 25)
        font = QFont(self.exoFontFamily, 12, weight=QFont.Normal)
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
            'background-color: #ff8c00'
            '}'
            'QCheckBox::indicator:unchecked {'
            'background-color: #ff8c00;'
            '}'
            'QCheckBox::indicator:checked {'
            f'background-color: {WIDGET_BACKGROUND_COLOR};'
            '}'
        )
        minCheckbox.toggle()
        minCheckbox.stateChanged.connect(self.minCheckboxChange)

    def minCheckboxChange(self, state):
        self.shouldMinifyCode = state != Qt.Checked

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)

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

    def buildLabel(self, text: str, fontSize: int, backgroundColor: str = None, foregroundColor=None, paddings: dict=None, radiusSizes: dict=None,
                   font: QFont = None) -> QLabel:
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
            font = QFont(self.exoFontFamily, fontSize, weight=QFont.Normal)

        if radiusSizes is not None:
            styleSheet += f'border-top-left-radius: {radiusSizes.get("top-left", 0)}%;'
            styleSheet += f'border-top-right-radius: {radiusSizes.get("top-right", 0)}%;'
            styleSheet += f'border-bottom-left-radius: {radiusSizes.get("bottom-left", 0)}%;'
            styleSheet += f'border-bottom-right-radius: {radiusSizes.get("bottom-right", 0)}%;'

        label.setFont(font)

        label.setStyleSheet(styleSheet)

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
