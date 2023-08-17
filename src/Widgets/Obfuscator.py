import enum

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from src.Contants import *
from src.ResourceRoutes import *
from src.Controllers.ObfuscatorController import ObfuscatorController
from src.Widgets.DeleteableList import DeleteableList
from src.Params.DeleteableListParams import DeleteableListParams


# Using enum class create enumerations
class ObfuscatorModes(enum.Enum):
    OB_MODE = 0
    DEOB_MODE = 1


class Obfuscator(QWidget):

    controller: ObfuscatorController = None
    mode: int = None
    currentModeGUIElements: list = []
    changeModeBtn: QPushButton = None
    windowModeText: QLabel = None
    obfuscateBtn: QPushButton = None
    offsetWindowPosition = None
    changeModeIcon: QIcon = None
    minimizeWindowIcon: QIcon = None
    closeIcon: QIcon = None
    closeHoverIcon: QIcon = None
    windowIcon: QIcon = None
    folderIcon: QIcon = None
    folderPressedIcon: QIcon = None
    addIcon: QIcon = None
    addPressedIcon: QIcon = None
    windowIcon: QIcon = None
    shouldMinifyCode: bool = False
    shouldSaveDecoder: bool = False
    binaryStringBTitle: QLabel = None
    binaryStringATitle: QLabel = None
    binaryStringBInput: QLineEdit = None
    binaryStringAInput: QLineEdit = None
    pathsList: DeleteableList = None
    listReferencesTitle: QLabel = None
    referencesList: DeleteableList = None
    ubuntuMonoFontFamily: str = None
    exoFontFamily: str = None
    inputReference: QLineEdit = None
    decoderFilePathDisabledInput: QLineEdit = None

    def __init__(self):
        super().__init__()
        self.controller = ObfuscatorController(self)
        self.mode = ObfuscatorModes.OB_MODE
        self.currentModeGUIElements = []

    def render(self):
        self.loadResources()
        self.conf()
        self.updateModeGUI()
        self.show()

    def updateModeGUI(self):

        self.removeModeGUIElements()

        if self.mode is ObfuscatorModes.OB_MODE:
            self.changeModeBtn.setText(OBFUSCATION_MODE)
            self.confObfuscateModeWidgets()
        elif self.mode is ObfuscatorModes.DEOB_MODE:
            self.changeModeBtn.setText(DEOFUSCATE_MODE)
            self.confDeobfuscateModeWidgets()

        self.showAllCurrentModeGUIElements()
        self.update()

    def showAllCurrentModeGUIElements(self):

        for child in self.currentModeGUIElements:
            child.show()

    def removeModeGUIElements(self):

        for child in self.currentModeGUIElements:
            child.deleteLater()

        self.currentModeGUIElements = []

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

        self.confWindowTitle()
        self.confWindowControlButtons()
        self.confChangeModeBtn()

    def loadResources(self):
        self.windowIcon = QIcon(ICON_PATH)
        self.addIcon = QIcon(ADD_ICON_PATH)
        self.folderIcon = QIcon(FOLDER_ICON_PATH)
        self.closeIcon = QIcon(CLOSE_ICON_PATH)
        self.minimizeWindowIcon = QIcon(MINIMIZE_ICON_PATH)
        self.changeModeIcon = QIcon(CHANGE_MODE_ICON_PATH)
        self.closeHoverIcon = QIcon(CLOSE_HOVER_ICON_PATH)
        self.addPressedIcon = QIcon(ADD_PRESSED_ICON_PATH)
        self.folderPressedIcon = QIcon(FOLDER_PRESSED_ICON_PATH)

        font_id = QFontDatabase.addApplicationFont(FONT_EXO_2_PATH)
        self.exoFontFamily = QFontDatabase.applicationFontFamilies(font_id)[0]

        font_id = QFontDatabase.addApplicationFont(FONT_UBUNTU_PATH)
        self.ubuntuMonoFontFamily = QFontDatabase.applicationFontFamilies(font_id)[0]

    def confObfuscateModeWidgets(self):
        self.confListPathsTitle()
        self.confListPaths(450, 200)
        self.confAddFilesBtn(360, 295)
        self.confListReferencesTitle()
        self.confReferencesList()
        self.confInputReference()
        self.confAddReferenceBtn()
        self.confBinaryStringTitles()
        self.confBinaryStringInputs()
        self.confMinCheckbox()
        self.confsaveDecoderCheckbox()
        self.confObfuscateBtn()

    def confDeobfuscateModeWidgets(self):
        self.confListPathsTitle()
        self.confListPaths(WINDOW_WIDTH - HORIZONTAL_PADDING * 2, 200)
        self.confAddFilesBtn(WINDOW_WIDTH - 120 - HORIZONTAL_PADDING, 295)
        self.confDecoderFilePathTitle()
        self.confSelectDecoderFileBtn()
        self.confDecoderFilePathDisabledInput()

    def confWindowTitle(self):
        listPathsTitle = self.buildLabel(
            WINDOW_TITLE,
            10,
            backgroundColor=PRIMARY_COLOR,
            foregroundColor=WIDGET_BACKGROUND_COLOR,
            paddings={
                'top': 7,
                'left': 10,
                'bottom': 6,
                'right': 10
            },
            radiusSizes={
                'top-left': 0,
                'top-right': 0,
                'bottom-left': 0,
                'bottom-right': 7
            },
            font=QFont(
                self.ubuntuMonoFontFamily,
                12,
                weight=QFont.Normal
            )
        )
        listPathsTitle.move(0, 0)
        listPathsTitle.setParent(self)

    def confWindowControlButtons(self):
        self.confMinimizeWindow()
        self.confCloseBtn()

    def confMinimizeWindow(self):
        restoreDownWindowBtn = QPushButton()
        restoreDownWindowBtn.move(WINDOW_WIDTH - 120, 0)
        restoreDownWindowBtn.setFixedSize(60, 31)

        restoreDownWindowBtn.setStyleSheet(
            'QPushButton{'
            'background-color: rgba(230, 230, 230, 0.24);'
            'border: none;'
            'border-bottom-left-radius: 7%;'
            '}'

            'QPushButton:hover{'
            f'background-color: {SECONDARY_COLOR};'
            '}'
        )

        restoreDownWindowBtn.setIcon(self.minimizeWindowIcon)
        restoreDownWindowBtn.setIconSize(QSize(12, 12))

        restoreDownWindowBtn.clicked.connect(lambda: self.showMinimized())

        restoreDownWindowBtn.setParent(self)

    def confCloseBtn(self):
        closeWindowBtn = QPushButton()
        closeWindowBtn.move(WINDOW_WIDTH - 60, 0)
        closeWindowBtn.setFixedSize(60, 31)
        closeWindowBtn.setStyleSheet(
            'QPushButton{'
            'background-color: rgba(230, 230, 230, 0.24);'
            'border: none;'
            '}'

            'QPushButton:hover{'
            f'background-color: {SECONDARY_COLOR};'
            '}'
        )
        closeWindowBtn.setIcon(self.closeIcon)
        closeWindowBtn.setIconSize(QSize(12, 12))
        closeWindowBtn.clicked.connect(lambda: exit(0))
        closeWindowBtn.setParent(self)

    def confChangeModeBtn(self):
        self.changeModeBtn = QPushButton(OBFUSCATION_MODE)

        font = QFont(self.exoFontFamily, 10, weight=QFont.Bold)
        self.changeModeBtn.setFont(font)

        self.changeModeBtn.move(230, 0)
        self.changeModeBtn.setFixedSize(130, 31)

        self.changeModeBtn.setStyleSheet(
            'QPushButton{'
            f'background-color: rgba(230, 230, 230, 0.24);'
            'color: white;'
            'border: none;'
            'border-bottom-left-radius: 7%;'
            'border-bottom-right-radius: 7%;'
            'padding-top: 2px;'
            '}'
            'QPushButton:hover{'
            f'background-color: {SECONDARY_COLOR};'
            '}'
        )

        self.changeModeBtn.clicked.connect(lambda: self.changeMode())

        self.changeModeBtn.setParent(self)

    def changeMode(self):

        if self.mode is ObfuscatorModes.OB_MODE:
            self.mode = ObfuscatorModes.DEOB_MODE
        elif self.mode is ObfuscatorModes.DEOB_MODE:
            self.mode = ObfuscatorModes.OB_MODE

        self.updateModeGUI()

    def confWindowModeText(self):
        self.windowModeText = self.buildLabel(OBFUSCATION_MODE, 9, foregroundColor='#bfbfbf')
        self.windowModeText.move(380, 7)
        self.windowModeText.setParent(self)

    def confListPathsTitle(self):
        listPathsTitle = self.buildLabel(FILE_PATH_LIST, 15)
        listPathsTitle.move(HORIZONTAL_PADDING + 5, TOP_PADDING)
        listPathsTitle.setParent(self)
        self.currentModeGUIElements.append(listPathsTitle)

    def confListPaths(self, width: int, height: int):
        left, top = HORIZONTAL_PADDING, TOP_PADDING + 40
        deleteableListParams = DeleteableListParams(left, top, width, height, '#ffffff', WIDGET_BACKGROUND_COLOR,
                                                    self.ubuntuMonoFontFamily, True,
                                                    moveVerticalScrollToEndWhenUpdateList=True,
                                                    moveHorizontalScrollToEndWhenUpdateList=True
                                                    )
        self.pathsList = DeleteableList(self, deleteableListParams)
        self.currentModeGUIElements.append(self.pathsList)

    def confAddFilesBtn(self, x:int, y:int):
        addFilesBtn = QPushButton(ADD_FILES)

        addFilesBtn.clicked.connect(self.AddFilesAction)
        addFilesBtn.move(x, y)
        addFilesBtn.setFixedSize(120, 32)

        font = QFont(self.exoFontFamily, 12, weight=QFont.Normal)
        addFilesBtn.setFont(font)

        addFilesBtn.setIcon(self.folderIcon)
        addFilesBtn.setIconSize(QSize(27, 27))

        addFilesBtn.pressed.connect(lambda: addFilesBtn.setIcon(self.folderPressedIcon))
        addFilesBtn.released.connect(lambda: addFilesBtn.setIcon(self.folderIcon))

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
        self.currentModeGUIElements.append(addFilesBtn)

    def confDecoderFilePathTitle(self):
        listPathsTitle = self.buildLabel(SELECT_DECODER_FILE, 15)
        listPathsTitle.move(HORIZONTAL_PADDING + 5, 350)
        listPathsTitle.setParent(self)
        self.currentModeGUIElements.append(listPathsTitle)

    def AddFilesAction(self):
        fileNames = self.showAndGetFileNames()
        self.pathsList.addStringItemList(fileNames)

    def confListReferencesTitle(self):
        self.listReferencesTitle = self.buildLabel(REFERENCES_LIST, 15)
        self.listReferencesTitle.move(WINDOW_WIDTH - HORIZONTAL_PADDING - 275, TOP_PADDING)
        self.listReferencesTitle.setParent(self)
        self.currentModeGUIElements.append(self.listReferencesTitle)

    def confReferencesList(self):
        left, top = WINDOW_WIDTH - HORIZONTAL_PADDING - 280, TOP_PADDING + 40
        width, height = 280, 420
        deleteableListParams = DeleteableListParams(left, top, width, height, '#ffffff', WIDGET_BACKGROUND_COLOR,
                                                    self.ubuntuMonoFontFamily, False,
                                                    moveVerticalScrollToEndWhenUpdateList=True,
                                                    moveHorizontalScrollToEndWhenUpdateList=True
                                                    )
        self.referencesList = DeleteableList(self, deleteableListParams)
        self.currentModeGUIElements.append(self.referencesList)

    def confInputReference(self):
        self.inputReference = self.buildLineEdit({
            'top-left': 7,
            'top-right': 0,
            'bottom-left': 7,
            'bottom-right': 0,
        })
        self.inputReference.move(WINDOW_WIDTH - HORIZONTAL_PADDING - 280, WINDOW_HEIGHT - BOTTOM_PADDING - 30)
        self.inputReference.setFixedSize(250, 30)
        self.inputReference.returnPressed.connect(lambda: self.insertNewVariableAction())
        self.inputReference.setParent(self)
        self.currentModeGUIElements.append(self.inputReference)

    def confAddReferenceBtn(self):
        addReferenceBtn = QPushButton()
        addReferenceBtn.setIcon(self.addIcon)

        addReferenceBtn.move(WINDOW_WIDTH - HORIZONTAL_PADDING - 30, WINDOW_HEIGHT - BOTTOM_PADDING - 30)
        addReferenceBtn.setFixedSize(30, 30)
        addReferenceBtn.setIconSize(QSize(15, 15))

        addReferenceBtn.clicked.connect(self.insertNewVariableAction)
        addReferenceBtn.pressed.connect(lambda: addReferenceBtn.setIcon(self.addPressedIcon))
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
        self.currentModeGUIElements.append(addReferenceBtn)

    def insertNewVariableAction(self):
        referenceName = self.inputReference.text()
        self.inputReference.setText('')
        self.referencesList.addStringItem(referenceName)

    def confObfuscateBtn(self):
        self.obfuscateBtn = QPushButton(START)

        self.obfuscateBtn.move(HORIZONTAL_PADDING, WINDOW_HEIGHT - BOTTOM_PADDING - 32)
        self.obfuscateBtn.setFixedSize(140, 32)

        font = QFont(self.exoFontFamily, 14, weight=QFont.Normal)
        self.obfuscateBtn.setFont(font)

        self.obfuscateBtn.setStyleSheet(
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
            'color: white;'
            '}'

            'QPushButton:pressed{'
            f'color: {PRIMARY_COLOR};'
            'background-color: white; '
            '}'
        )

        self.obfuscateBtn.clicked.connect(self.controller.obfuscateAction)

        self.obfuscateBtn.setParent(self)
        self.currentModeGUIElements.append(self.obfuscateBtn)

    def showAndGetFileNames(self) -> list:
        fileNames, _ = QFileDialog.getOpenFileNames(self, "Select files", "", "All files (*)")
        return fileNames

    def confBinaryStringTitles(self):
        self.binaryStringATitle = self.buildLabel(STRING_A, 13)
        self.binaryStringATitle.move(120, 345 - TITLE_Y_CORRECTION)
        self.binaryStringATitle.setFixedSize(QSize(120, 30))
        self.binaryStringATitle.setParent(self)
        self.currentModeGUIElements.append(self.binaryStringATitle)

        self.binaryStringBTitle = self.buildLabel(STRING_B, 13)
        self.binaryStringBTitle.move(297, 345 - TITLE_Y_CORRECTION)
        self.binaryStringBTitle.setFixedSize(QSize(120, 30))
        self.binaryStringBTitle.setParent(self)
        self.currentModeGUIElements.append(self.binaryStringBTitle)

    def confBinaryStringInputs(self):
        self.binaryStringAInput = self.buildBinaryStringInput()
        self.binaryStringAInput.move(110, 375)
        self.binaryStringAInput.setAlignment(QtCore.Qt.AlignCenter)
        self.binaryStringAInput.setParent(self)
        self.currentModeGUIElements.append(self.binaryStringAInput)

        self.binaryStringBInput = self.buildBinaryStringInput()
        self.binaryStringBInput.move(290, 375)
        self.binaryStringBInput.setAlignment(QtCore.Qt.AlignCenter)
        self.binaryStringBInput.setParent(self)
        self.currentModeGUIElements.append(self.binaryStringBInput)

    def confMinCheckbox(self):
        minCheckbox = QCheckBox(MINIFY_CODE, self)
        minCheckbox.move(195, 430)
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
        self.currentModeGUIElements.append(minCheckbox)

    def minCheckboxChange(self, state):
        self.shouldMinifyCode = state != Qt.Checked

    def confsaveDecoderCheckbox(self):
        saveDecoderFileCheckbox = QCheckBox(SAVE_DECODER_FILE_CODE, self)
        saveDecoderFileCheckbox.move(195, 470)
        saveDecoderFileCheckbox.setFixedSize(180, 25)
        font = QFont(self.exoFontFamily, 12, weight=QFont.Normal)
        saveDecoderFileCheckbox.setFont(font)
        saveDecoderFileCheckbox.setCheckState(False)
        saveDecoderFileCheckbox.setStyleSheet(
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
        saveDecoderFileCheckbox.toggle()
        saveDecoderFileCheckbox.stateChanged.connect(self.saveDecoderFile)
        self.currentModeGUIElements.append(saveDecoderFileCheckbox)

    def saveDecoderFile(self, state):
        self.shouldSaveDecoder = state != Qt.Checked

    def mousePressEvent(self, event):
        self.offsetWindowPosition = event.pos()

    def mouseMoveEvent(self, event):
        try:
            x = event.globalX()
            y = event.globalY()
            xW = self.offsetWindowPosition.x()
            yW = self.offsetWindowPosition.y()
            self.move(x - xW, y - yW)
        except:
            pass

    def requestFilePathToUser(self):

        dialog = QFileDialog()
        dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)
        dialog.setWindowTitle(SAVE_DECODER_FILE)
        dialog.setDefaultSuffix('dec')
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setNameFilters([ALLOWED_FILE_TYPES_FOR_DECODER_FILE])

        filePath = None

        if dialog.exec_() == QDialog.Accepted:
            filePath = dialog.selectedFiles()[0]

        return filePath
    
    def confSelectDecoderFileBtn(self):
        selectDecoderFileBtn = QPushButton()
        selectDecoderFileBtn.setIcon(self.folderIcon)

        selectDecoderFileBtn.move(HORIZONTAL_PADDING, 385)
        selectDecoderFileBtn.setFixedSize(110, 30)
        selectDecoderFileBtn.setIconSize(QSize(27, 27))

        selectDecoderFileBtn.clicked.connect(self.findDecoderFileAction)
        selectDecoderFileBtn.pressed.connect(lambda: selectDecoderFileBtn.setIcon(self.folderPressedIcon))
        selectDecoderFileBtn.released.connect(lambda: selectDecoderFileBtn.setIcon(self.folderIcon))

        selectDecoderFileBtn.setStyleSheet(
            'QPushButton{'
            'color: white;'
            f'background-color: {PRIMARY_COLOR};'
            'border-top-left-radius: 7%;'
            'border-top-right-radius: 0%;'
            'border-bottom-left-radius: 7%;'
            'border-bottom-right-radius: 0%;'
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

        selectDecoderFileBtn.setParent(self)
        self.currentModeGUIElements.append(selectDecoderFileBtn)

    def findDecoderFileAction(self):
        pass

    def confDecoderFilePathDisabledInput(self):
        self.decoderFilePathDisabledInput = self.buildLineEdit({
            'top-left': 0,
            'top-right': 7,
            'bottom-left': 0,
            'bottom-right': 7,
        })
        self.decoderFilePathDisabledInput.move(HORIZONTAL_PADDING + 110, 385)
        self.decoderFilePathDisabledInput.setFixedSize(WINDOW_WIDTH - HORIZONTAL_PADDING * 2 - 110, 30)
        self.decoderFilePathDisabledInput.setDisabled(True)

        self.decoderFilePathDisabledInput.setParent(self)
        self.currentModeGUIElements.append(self.decoderFilePathDisabledInput)

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

    def enableObfuscateBtn(self, enable: bool):
        self.obfuscateBtn.setEnabled(enable)
