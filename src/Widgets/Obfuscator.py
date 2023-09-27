import enum

from PyQt6 import QtCore
from PyQt6.QtCore import *
from src.factories.ComponentesBasicBuilds import *
from src.Params.DeleteableListParams import DeleteableListParams

from src.Contants import *
from src.ResourceRoutes import *
from src.Controllers.ObfuscatorController import ObfuscatorController
from src.Widgets.DeleteableList import DeleteableList

ubuntuMonoFontFamily: str
exoFontFamily: str


class ObfuscatorModes(enum.Enum):
    OB_MODE = 0
    DEOB_MODE = 1


class Obfuscator(QWidget):
    controller: ObfuscatorController
    mode: ObfuscatorModes = ObfuscatorModes.OB_MODE
    currentModeGUIElements: list = []
    changeModeBtn: QPushButton
    windowModeText: QLabel
    obfuscateBtn: QPushButton
    deobfuscateBtn: QPushButton
    offsetWindowPosition: QPoint | None = None
    isMousePressWindow: bool = False
    changeModeIcon: QIcon
    minimizeWindowIcon: QIcon
    closeIcon: QIcon
    closeHoverIcon: QIcon
    windowIcon: QIcon
    folderIcon: QIcon
    folderPressedIcon: QIcon
    addIcon: QIcon
    symbolIcon: QIcon
    addPressedIcon: QIcon
    shouldMinifyCode: bool = False
    shouldSaveDecoder: bool = False
    binaryStringBTitle: QLabel
    binaryStringATitle: QLabel
    binaryStringBInput: QLineEdit
    binaryStringAInput: QLineEdit
    pathsList: DeleteableList
    listReferencesTitle: QLabel
    referencesList: DeleteableList
    inputReference: QLineEdit
    decoderFilePathDisabledInput: QLineEdit

    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
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
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
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
        self.confWindowIcon()
        self.confWindowControlButtons()
        self.confChangeModeBtn()

    # Window events

    def mousePressEvent(self, event: QMouseEvent):
        self.isMousePressWindow = True
        self.offsetWindowPosition = event.pos()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.isMousePressWindow = False

    def mouseMoveEvent(self, event: QMouseEvent):

        if not self.isMousePressWindow or self.offsetWindowPosition is None:
            return

        try:
            globalPositionPoint: QPointF = event.globalPosition()
            xW = float(self.offsetWindowPosition.x())
            yW = float(self.offsetWindowPosition.y())
            xNext, yNext = int(globalPositionPoint.x() - xW), int(globalPositionPoint.y() - yW)
            self.move(QPoint(xNext, yNext))
        except Exception as ex:
            print(ex)
            pass

    def loadResources(self):
        self.windowIcon = QIcon(ICON_PATH)
        self.symbolIcon = QIcon(SYMBOL_PATH)
        self.addIcon = QIcon(ADD_ICON_PATH)
        self.folderIcon = QIcon(FOLDER_ICON_PATH)
        self.closeIcon = QIcon(CLOSE_ICON_PATH)
        self.minimizeWindowIcon = QIcon(MINIMIZE_ICON_PATH)
        self.changeModeIcon = QIcon(CHANGE_MODE_ICON_PATH)
        self.closeHoverIcon = QIcon(CLOSE_HOVER_ICON_PATH)
        self.addPressedIcon = QIcon(ADD_PRESSED_ICON_PATH)
        self.folderPressedIcon = QIcon(FOLDER_PRESSED_ICON_PATH)

        global exoFontFamily
        global ubuntuMonoFontFamily

        font_id = QFontDatabase.addApplicationFont(FONT_EXO_2_PATH)
        exoFontFamily = QFontDatabase.applicationFontFamilies(font_id)[0]

        font_id = QFontDatabase.addApplicationFont(FONT_UBUNTU_PATH)
        ubuntuMonoFontFamily = QFontDatabase.applicationFontFamilies(font_id)[0]

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
        self.confSymbolImageLabel()
        self.confDeobfuscateBtn()

    def confWindowTitle(self):

        global ubuntuMonoFontFamily

        listPathsTitle = buildLabel(
            f'  {WINDOW_TITLE}',
            10,
            backgroundColor=PRIMARY_COLOR,
            foregroundColor='white',
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
                ubuntuMonoFontFamily,
                12,
                weight=500
            )
        )
        listPathsTitle.move(0, 0)
        listPathsTitle.setParent(self)

    def confWindowIcon(self):
        label = QLabel()
        pixmap = QPixmap(SYMBOL_WHITE_MINI_PATH)
        label.setPixmap(pixmap)
        label.move(12, 5)
        label.setParent(self)

    def confWindowControlButtons(self):
        self.confMinimizeWindow()
        self.confCloseBtn()

    def confMinimizeWindow(self):
        restoreDownWindowBtn = QPushButton()
        restoreDownWindowBtn.move(WINDOW_WIDTH - 120, 0)
        restoreDownWindowBtn.setFixedSize(60, 30)

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
        closeWindowBtn.setFixedSize(60, 30)
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

        font = QFont(exoFontFamily, 11, weight=500)
        self.changeModeBtn.setFont(font)

        self.changeModeBtn.move(230, 0)
        self.changeModeBtn.setFixedSize(130, 30)

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
        self.windowModeText = buildLabel(OBFUSCATION_MODE, 9, foregroundColor='#bfbfbf')
        self.windowModeText.move(380, 7)
        self.windowModeText.setParent(self)

    def confListPathsTitle(self):
        listPathsTitle = buildLabel(FILE_PATH_LIST, 15)
        listPathsTitle.move(HORIZONTAL_PADDING + 5, TOP_PADDING)
        listPathsTitle.setParent(self)
        self.currentModeGUIElements.append(listPathsTitle)

    def confListPaths(self, width: int, height: int):
        left, top = HORIZONTAL_PADDING, TOP_PADDING + 40
        global ubuntuMonoFontFamily
        deleteableListParams = DeleteableListParams(left, top, width, height, '#ffffff', WIDGET_BACKGROUND_COLOR,
                                                    ubuntuMonoFontFamily, True,
                                                    moveVerticalScrollToEndWhenUpdateList=True,
                                                    moveHorizontalScrollToEndWhenUpdateList=True
                                                    )
        self.pathsList = DeleteableList(self, deleteableListParams)
        self.currentModeGUIElements.append(self.pathsList)

    def confAddFilesBtn(self, x: int, y: int):
        addFilesBtn = QPushButton(ADD_FILES)

        addFilesBtn.clicked.connect(self.AddFilesAction)
        addFilesBtn.move(x, y)
        addFilesBtn.setFixedSize(120, 32)

        font = QFont(exoFontFamily, 12, weight=400)
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
        listPathsTitle = buildLabel(SELECT_DECODER_FILE, 15)
        listPathsTitle.move(HORIZONTAL_PADDING + 5, 370)
        listPathsTitle.setParent(self)
        self.currentModeGUIElements.append(listPathsTitle)

    def confListReferencesTitle(self):
        self.listReferencesTitle = buildLabel(REFERENCES_LIST, 15)
        self.listReferencesTitle.move(WINDOW_WIDTH - HORIZONTAL_PADDING - 275, TOP_PADDING)
        self.listReferencesTitle.setParent(self)
        self.currentModeGUIElements.append(self.listReferencesTitle)

    def confReferencesList(self):
        left, top = WINDOW_WIDTH - HORIZONTAL_PADDING - 280, TOP_PADDING + 40
        width, height = 280, 420
        global ubuntuMonoFontFamily
        deleteableListParams = DeleteableListParams(left, top, width, height, '#ffffff', WIDGET_BACKGROUND_COLOR,
                                                    ubuntuMonoFontFamily, False,
                                                    moveVerticalScrollToEndWhenUpdateList=True,
                                                    moveHorizontalScrollToEndWhenUpdateList=True
                                                    )
        self.referencesList = DeleteableList(self, deleteableListParams)
        self.currentModeGUIElements.append(self.referencesList)

    def confInputReference(self):
        self.inputReference = buildLineEdit({
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
        self.obfuscateBtn = QPushButton(OBFUSCATE)

        self.obfuscateBtn.move(HORIZONTAL_PADDING, WINDOW_HEIGHT - BOTTOM_PADDING - 30)
        self.obfuscateBtn.setFixedSize(160, 30)

        font = QFont(exoFontFamily, 14, weight=500)
        self.obfuscateBtn.setFont(font)

        self.obfuscateBtn.setStyleSheet(
            'QPushButton{'
            'background-color: white; '
            f'color: {WIDGET_BACKGROUND_COLOR};'
            'border-top-left-radius: 7%;'
            'border-top-right-radius: 7%;'
            'border-bottom-left-radius: 7%;'
            'border-bottom-right-radius: 7%;'
            '}'

            'QPushButton:hover{'
            f'background-color: {SECONDARY_COLOR}; '
            f'color: {WIDGET_BACKGROUND_COLOR};'
            '}'

            'QPushButton:pressed{'
            'color: white;'
            '}'
        )

        self.obfuscateBtn.clicked.connect(self.controller.obfuscateAction)

        self.obfuscateBtn.setParent(self)
        self.currentModeGUIElements.append(self.obfuscateBtn)

    def confBinaryStringTitles(self):
        self.binaryStringATitle = buildLabel(STRING_A, 13)
        self.binaryStringATitle.move(120, 345 - TITLE_Y_CORRECTION)
        self.binaryStringATitle.setFixedSize(QSize(120, 30))
        self.binaryStringATitle.setParent(self)
        self.currentModeGUIElements.append(self.binaryStringATitle)

        self.binaryStringBTitle = buildLabel(STRING_B, 13)
        self.binaryStringBTitle.move(297, 345 - TITLE_Y_CORRECTION)
        self.binaryStringBTitle.setFixedSize(QSize(120, 30))
        self.binaryStringBTitle.setParent(self)
        self.currentModeGUIElements.append(self.binaryStringBTitle)

    def confBinaryStringInputs(self):
        self.binaryStringAInput = buildBinaryStringInput()
        self.binaryStringAInput.move(110, 375)
        self.binaryStringAInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.binaryStringAInput.setParent(self)
        self.currentModeGUIElements.append(self.binaryStringAInput)

        self.binaryStringBInput = buildBinaryStringInput()
        self.binaryStringBInput.move(290, 375)
        self.binaryStringBInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.binaryStringBInput.setParent(self)
        self.currentModeGUIElements.append(self.binaryStringBInput)

    def confMinCheckbox(self):
        minCheckbox = QCheckBox(MINIFY_CODE, self)
        minCheckbox.move(195, 430)
        minCheckbox.setFixedSize(145, 25)
        font = QFont(exoFontFamily, 12, weight=400)
        minCheckbox.setFont(font)
        minCheckbox.setCheckState(Qt.CheckState.Unchecked)
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
        self.shouldMinifyCode = (state != Qt.CheckState.Checked)

    def confsaveDecoderCheckbox(self):
        saveDecoderFileCheckbox = QCheckBox(SAVE_DECODER_FILE_CODE, self)
        saveDecoderFileCheckbox.move(195, 470)
        saveDecoderFileCheckbox.setFixedSize(180, 25)
        font = QFont(exoFontFamily, 12, weight=400)
        saveDecoderFileCheckbox.setFont(font)
        saveDecoderFileCheckbox.setCheckState(Qt.CheckState.Unchecked)
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
        saveDecoderFileCheckbox.stateChanged.connect(self.changStateOfShouldSaveDecoder)
        self.currentModeGUIElements.append(saveDecoderFileCheckbox)

    def changStateOfShouldSaveDecoder(self, state):
        self.shouldSaveDecoder = state != Qt.CheckState.Checked

    def confSelectDecoderFileBtn(self):
        selectDecoderFileBtn = QPushButton()
        selectDecoderFileBtn.setIcon(self.folderIcon)

        selectDecoderFileBtn.move(HORIZONTAL_PADDING, 410)
        selectDecoderFileBtn.setFixedSize(110, 31)
        selectDecoderFileBtn.setIconSize(QSize(27, 27))

        selectDecoderFileBtn.clicked.connect(self.findDecoderFileAction)
        selectDecoderFileBtn.pressed.connect(lambda: selectDecoderFileBtn.setIcon(self.folderPressedIcon))
        selectDecoderFileBtn.released.connect(lambda: selectDecoderFileBtn.setIcon(self.folderIcon))
        selectDecoderFileBtn.setObjectName('select-decoder-file-btn')
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

    def confDecoderFilePathDisabledInput(self):
        self.decoderFilePathDisabledInput = buildLineEdit({
            'top-left': 0,
            'top-right': 7,
            'bottom-left': 0,
            'bottom-right': 7,
        })

        self.decoderFilePathDisabledInput.setStyleSheet(
            f'{self.decoderFilePathDisabledInput.styleSheet()}'
            'QLineEdit{'
            f'border-color: {PRIMARY_COLOR};'
            '}'
        )

        self.decoderFilePathDisabledInput.move(HORIZONTAL_PADDING + 110, 410)
        self.decoderFilePathDisabledInput.setFixedSize(WINDOW_WIDTH - HORIZONTAL_PADDING * 2 - 110, 31)
        self.decoderFilePathDisabledInput.setDisabled(True)

        self.decoderFilePathDisabledInput.setParent(self)
        self.currentModeGUIElements.append(self.decoderFilePathDisabledInput)

    def confSymbolImageLabel(self):

        """  painter = QPainter(self)
        painter.translate(20, 100)
        painter.rotate(-90)
        painter.drawPixmap(QPoint(300,300), QPixmap(SYMBOL_PATH)) """
        pass

    def confDeobfuscateBtn(self):
        self.deobfuscateBtn = QPushButton(DEOBFUSCATE)

        self.deobfuscateBtn.move(HORIZONTAL_PADDING, WINDOW_HEIGHT - BOTTOM_PADDING - 30)
        self.deobfuscateBtn.setFixedSize(160, 30)

        font = QFont(exoFontFamily, 14, weight=500)
        self.deobfuscateBtn.setFont(font)

        self.deobfuscateBtn.setStyleSheet(
            'QPushButton{'
            'background-color: white; '
            f'color: {WIDGET_BACKGROUND_COLOR};'
            'border-top-left-radius: 7%;'
            'border-top-right-radius: 7%;'
            'border-bottom-left-radius: 7%;'
            'border-bottom-right-radius: 7%;'
            '}'

            'QPushButton:hover{'
            f'background-color: {SECONDARY_COLOR}; '
            f'color: {WIDGET_BACKGROUND_COLOR};'
            '}'

            'QPushButton:pressed{'
            'color: white;'
            '}'
        )

        self.deobfuscateBtn.clicked.connect(self.controller.deobfuscateAction)

        self.deobfuscateBtn.setParent(self)
        self.currentModeGUIElements.append(self.deobfuscateBtn)

    # Files explorer GUI system actions

    def AddFilesAction(self):
        fileNames = self.showAndGetFileNames('All files (*)')
        self.pathsList.addStringItemList(fileNames)

    def setDecoderFileAction(self):
        decoderFilePath = self.requestFilePathToUsetToSaveDecoderFile()
        if decoderFilePath is None:
            return
        self.decoderFilePathDisabledInput.setText(decoderFilePath)

    def findDecoderFileAction(self):
        path = self.showAndGetFileName('Decoder file (*.dec)')
        self.decoderFilePathDisabledInput.setText(path)

    def requestFilePathToUsetToSaveDecoderFile(self) -> str | None:

        dialog = QFileDialog()
        dialog.setFilter(dialog.filter() | QDir.Filter.Hidden)
        dialog.setWindowTitle(SAVE_DECODER_FILE)
        dialog.setDefaultSuffix('dec')
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        dialog.setNameFilters([ALLOWED_FILE_TYPES_FOR_DECODER_FILE])

        filePath = None

        if dialog.exec() == QDialog.DialogCode.Accepted:
            filePath = dialog.selectedFiles()[0]

        return filePath

    def showAndGetFileNames(self, extensionFilter: str) -> list:
        fileNames, _ = QFileDialog.getOpenFileNames(self, "Select files", "", extensionFilter)
        return fileNames

    def showAndGetFileName(self, extensionFilter: str) -> str:
        fileName, _ = QFileDialog.getOpenFileName(self, "Select file", "", extensionFilter)
        return fileName

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

    def enableDeobfuscateBtn(self, enable: bool):
        self.deobfuscateBtn.setEnabled(enable)

    def getDecoderFilePath(self) -> str:
        return self.decoderFilePathDisabledInput.text()