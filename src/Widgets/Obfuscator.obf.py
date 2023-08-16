from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.Contants import *
from src.ResourceRoutes import *
from src.Controllers.ObfuscatorController import ObfuscatorController
from src.Widgets.DeleteableList import DeleteableList
from src.Params.DeleteableListParams import DeleteableListParams
class Obfuscator(QWidget):
    def __init__(self):
        super().__init__()
        self.lIIIII = ObfuscatorController(self)
        self.Illlll = None
        self.lIIlll = None
        self.IIIIII = None
        self.IIllII = None
        self.lIIlII = None
        self.IllIIl = None
        self.lIIIll = None
        self.IlIIIl = None
        self.IllIlI = None
        self.IlIIll = False
        self.IIllIl = None
        self.lIIIlI = None
        self.IIlllI = None
        self.IIllll = None
        self.IlIIII = None
        self.lIIlIl = None
        self.IIlIII = None
        self.lIIllI = None
        self.IllIll = None
        self.IIIllI = None
        self.IllllI = None
        self.lIIIll = None
        self.IlllII = None
    def render(self):
        self.loadResources()
        self.conf()
        self.confWidgets()
        self.show()
    def conf(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(self.lIIIll)
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
        self.lIIIll = QIcon(ICON_PATH)
        self.lIIllI = QIcon(ADD_ICON_PATH)
        self.lIIIlI = QIcon(FOLDER_ICON_PATH)
        self.lIIlII = QIcon(CLOSE_ICON_PATH)
        self.IIllII = QIcon(MINIMIZE_ICON_PATH)
        self.IllIIl = QIcon(CLOSE_HOVER_ICON_PATH)
        self.IllIlI = QIcon(ADD_PRESSED_ICON_PATH)
        self.IlIIIl = QIcon(FOLDER_PRESSED_ICON_PATH)
        font_id = QFontDatabase.addApplicationFont(FONT_EXO_2_PATH)
        self.IllllI = QFontDatabase.applicationFontFamilies(font_id)[0]
        font_id = QFontDatabase.addApplicationFont(FONT_UBUNTU_PATH)
        self.IIIllI = QFontDatabase.applicationFontFamilies(font_id)[0]
    def confWidgets(self):
        self.IlIllI()
        self.IIIIIl()
        self.IIlIll()
        self.IlllIl()
        self.IlIlIl()
        self.IIIIlI()
        self.IIlIlI()
        self.IIlIIl()
        self.IIIlll()
        self.IIIlII()
        self.IIIIll()
        self.IlIlII()
        self.IlIIlI()
    def IlIllI(self):
        IllIII = self.buildLabel(WINDOW_TITLE, 10, backgroundColor=f'{PRIMARY_COLOR}',
                                         foregroundColor=WIDGET_BACKGROUND_COLOR,
                                         paddings={
                                             'top': 7,
                                             'left': 10,
                                             'bottom': 6,
                                             'right': 10
                                         }, radiusSizes={
                                             'top-left': 0,
                                             'top-right': 0,
                                             'bottom-left': 0,
                                             'bottom-right': 7
                                         }, font=QFont(self.IIIllI, 12, weight=QFont.Light))
        IllIII.move(0, 0)
        IllIII.setParent(self)
    def IIIIIl(self):
        self.confMinimizeWindow()
        self.confCloseBtn()
    def confMinimizeWindow(self):
        IIIlIl = QPushButton()
        IIIlIl.move(WINDOW_WIDTH - 120, 0)
        IIIlIl.setFixedSize(60, 35)
        IIIlIl.setStyleSheet(
            'QPushButton{'
                'background-color: rgba(230, 230, 230, 0.24);'
                'border: none;'
                'border-bottom-left-radius: 7%;'
            '}'
            
            'QPushButton:hover{'
                f'background-color: {SECONDARY_COLOR};'
            '}'
        )
        IIIlIl.setIcon(self.IIllII)
        IIIlIl.setIconSize(QSize(15, 15))
        IIIlIl.clicked.connect(lambda: self.showMinimized())
        IIIlIl.setParent(self)
    def confCloseBtn(self):
        IlIlll = QPushButton()
        IlIlll.move(WINDOW_WIDTH - 60, 0)
        IlIlll.setFixedSize(60, 35)
        IlIlll.setStyleSheet(
             'QPushButton{'
                'background-color: rgba(230, 230, 230, 0.24);'
                'border: none;'
            '}'
            
            'QPushButton:hover{'
                f'background-color: {SECONDARY_COLOR};'
            '}'
        )
        IlIlll.setIcon(self.lIIlII)
        IlIlll.setIconSize(QSize(15, 15))
        IlIlll.clicked.connect(lambda: exit(0))
        IlIlll.setParent(self)
    def IIlIll(self):
        IllIII = self.buildLabel(FILE_PATH_LIST, 15)
        IllIII.move(HORIZONTAL_PADDING + 5, TOP_PADDING)
        IllIII.setParent(self)
    def IlllIl(self):
        left, top = HORIZONTAL_PADDING, TOP_PADDING + 40
        width, height = 450, 200
        deleteableListParams = DeleteableListParams(left, top, width, height, '#ffffff', WIDGET_BACKGROUND_COLOR,
                                                    self.IIIllI, True)
        self.lIIlIl = DeleteableList(self, deleteableListParams)
    def IlIlIl(self):
        addFilesBtn = QPushButton(ADD_FILES)
        addFilesBtn.clicked.connect(self.AddFilesAction)
        addFilesBtn.move(360, 295)
        addFilesBtn.setFixedSize(120, 32)
        font = QFont(self.IllllI, 12, weight=QFont.Normal)
        addFilesBtn.setFont(font)
        addFilesBtn.setIcon(self.lIIIlI)
        addFilesBtn.setIconSize(QSize(27, 27))
        addFilesBtn.pressed.connect(lambda: addFilesBtn.setIcon(self.IlIIIl))
        addFilesBtn.released.connect(lambda: addFilesBtn.setIcon(self.lIIIlI))
        addFilesBtn.setStyleSheet(
            'QPushButton{'
            'color: white;'
            f'background-color: {PRIMARY_COLOR};'
            'text-align:center; '
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
        self.lIIlIl.addStringItemList(fileNames)
    def IIIIlI(self):
        self.IIlIII = self.buildLabel(REFERENCES_LIST, 15)
        self.IIlIII.move(WINDOW_WIDTH - HORIZONTAL_PADDING - 275, TOP_PADDING)
        self.IIlIII.setParent(self)
    def IIlIlI(self):
        left, top = WINDOW_WIDTH - HORIZONTAL_PADDING - 280, TOP_PADDING + 40
        width, height = 280, 420
        deleteableListParams = DeleteableListParams(left, top, width, height, '#ffffff', WIDGET_BACKGROUND_COLOR,
                                                    self.IIIllI, False)
        self.IllIll = DeleteableList(self, deleteableListParams)
    def IIlIIl(self):
        self.IlllII = self.buildLineEdit({
            'top-left': 7,
            'top-right': 0,
            'bottom-left': 7,
            'bottom-right': 0,
        })
        self.IlllII.move(WINDOW_WIDTH - HORIZONTAL_PADDING - 280, WINDOW_HEIGHT - BOTTOM_PADDING - 30)
        self.IlllII.setFixedSize(250, 30)
        self.IlllII.setParent(self)
        self.IlllII.returnPressed.connect(lambda: self.insertNewVariableAction())
    def IIIlll(self):
        addReferenceBtn = QPushButton()
        addReferenceBtn.setIcon(self.lIIllI)
        addReferenceBtn.move(WINDOW_WIDTH - HORIZONTAL_PADDING - 30, WINDOW_HEIGHT - BOTTOM_PADDING - 30)
        addReferenceBtn.setFixedSize(30, 30)
        addReferenceBtn.setIconSize(QSize(15, 15))
        addReferenceBtn.clicked.connect(self.insertNewVariableAction)
        addReferenceBtn.pressed.connect(lambda: addReferenceBtn.setIcon(self.IllIlI))
        addReferenceBtn.released.connect(lambda: addReferenceBtn.setIcon(self.lIIllI))
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
        referenceName = self.IlllII.text()
        self.IlllII.setText('')
        self.IllIll.addStringItem(referenceName)
    def IlIIlI(self):
        self.Illlll = QPushButton(START)
        self.Illlll.move(HORIZONTAL_PADDING, WINDOW_HEIGHT - BOTTOM_PADDING - 32)
        self.Illlll.setFixedSize(140, 32)
        font = QFont(self.IllllI, 14, weight=QFont.Normal)
        self.Illlll.setFont(font)
        self.Illlll.setStyleSheet(
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
        self.Illlll.clicked.connect(self.lIIIII.obfuscateAction)
        self.Illlll.setParent(self)
    def showAndGetFileNames(self) -> list:
        fileNames, _ = QFileDialog.getOpenFileNames(self, "Select files", "", "All files (*)")
        return fileNames
    def IIIlII(self):
        self.IIlllI = self.buildLabel(STRING_A, 12)
        self.IIlllI.move(120, 345 - TITLE_Y_CORRECTION)
        self.IIlllI.setMaximumSize(QSize(120, 30))
        self.IIlllI.setParent(self)
        self.IIllIl = self.buildLabel(STRING_B, 12)
        self.IIllIl.move(297, 345 - TITLE_Y_CORRECTION)
        self.IIllIl.setMaximumSize(QSize(120, 30))
        self.IIllIl.setParent(self)
    def IIIIll(self):
        self.IlIIII = self.buildBinaryStringInput()
        self.IlIIII.move(110, 375)
        self.IlIIII.setParent(self)
        self.IIllll = self.buildBinaryStringInput()
        self.IIllll.move(290, 375)
        self.IIllll.setParent(self)
        self.IlIIII.setAlignment(QtCore.Qt.AlignCenter)
        self.IIllll.setAlignment(QtCore.Qt.AlignCenter)
    def IlIlII(self):
        minCheckbox = QCheckBox(MINIFY_CODE, self)
        minCheckbox.move(195, 440)
        minCheckbox.setFixedSize(145, 25)
        font = QFont(self.IllllI, 12, weight=QFont.Normal)
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
            f'background-color: {SECONDARY_COLOR};'
            '}'
            'QCheckBox::indicator:unchecked {'
            f'background-color: {SECONDARY_COLOR};'
            '}'
            'QCheckBox::indicator:checked {'
            f'background-color: {WIDGET_BACKGROUND_COLOR};'
            '}'
        )
        minCheckbox.toggle()
        minCheckbox.stateChanged.connect(self.minCheckboxChange)
    def minCheckboxChange(self, state):
        self.IlIIll = state != Qt.Checked
    def mousePressEvent(self, event):
        self.lIIlll = event.pos()
    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.lIIlll.x()
        y_w = self.lIIlll.y()
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
        font = QFont(self.IIIllI, 14)
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
    def buildLabel(self, text: str, fontSize: int, backgroundColor: str = None, foregroundColor=None,
                   paddings: dict = None, radiusSizes: dict = None,
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
            font = QFont(self.IllllI, fontSize, weight=QFont.Normal)
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
        return self.lIIlIl.getStringItems()
    def getReferences(self) -> list:
        return self.IllIll.getStringItems()
    def getStringA(self) -> str:
        return self.IlIIII.text()
    def getStringB(self) -> str:
        return self.IIllll.text()
    def getShouldMinifyCode(self) -> bool:
        return self.IlIIll
    def enableObfuscateBtn(self, enable: bool):
        self.Illlll.setEnabled(enable)
