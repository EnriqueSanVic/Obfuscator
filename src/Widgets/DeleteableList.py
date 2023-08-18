import asyncio

from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QWidget, QPushButton, QLabel, QHBoxLayout
from src.Params.DeleteableListParams import DeleteableListParams

from src.Utils import isStrEmpty

DELETE_ICON_PATH = './assets/delete.png'
ACCENT_ICON_PATH = './assets/accent_delete.png'
ACCENT_DARK_ICON_PATH = './assets/accent_dark_delete.png'

ICON_SIZE = 20

class DeleteableList(QListWidget):

    def __init__(self, parent, params: DeleteableListParams):

        super().__init__(parent)
        self.params = params
        self.deleteIcon = QIcon(DELETE_ICON_PATH)
        self.accentDeleteIcon = QIcon(ACCENT_ICON_PATH)
        self.accentDarkDeleteIcon = QIcon(ACCENT_DARK_ICON_PATH)
        self.conf()

    def conf(self):
        self.move(self.params.left, self.params.top)
        self.setFixedSize(self.params.width, self.params.height)
        self.setStyleSheet(
            'QListWidget{'
            f'background-color: {self.params.backgroundColor};'
            f'border: 2px solid {self.params.foregroundColor};'
            'border-radius: 7%;'
            '}'
        )

        model = self.model()

        if model is None:
            return

        model.rowsInserted.connect(self.afterListChange)
        model.rowsRemoved.connect(self.afterListChange)

    def addStringItemList(self, stringList: list):

        for i in stringList:
            self.addStringItem(i)

    def addStringItem(self, name: str):

        name = name.strip()

        if isStrEmpty(name):
            return

        listWidgetItem = QListWidgetItem()

        itemWidget = QWidget()

        itemWidget.setStyleSheet(f'background-color: {self.params.backgroundColor};')

        itemWidget.setLayout(self.buildListItemWidgetLayout(name, listWidgetItem))

        listWidgetItem.setSizeHint(itemWidget.sizeHint())
        listWidgetItem.setText(name)

        self.addItem(listWidgetItem)
        self.setItemWidget(listWidgetItem, itemWidget)

    def afterListChange(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.evaluateScrollMovement())

    async def evaluateScrollMovement(self):

        #await asyncio.sleep(2)

        if self.params.moveVerticalScrollToEndWhenUpdateList:
            self.moveVerticalScrollToEndWhenUpdateList()

        if self.params.moveHorizontalScrollToEndWhenUpdateList:
            self.moveHorizontalScrollToEndWhenUpdateList()

    def moveHorizontalScrollToEndWhenUpdateList(self):
        horizontalScrollbar = self.horizontalScrollBar()
        if horizontalScrollbar is None:
            return
        horizontalScrollbar.setValue(horizontalScrollbar.maximum())

    def moveVerticalScrollToEndWhenUpdateList(self):
        verticalScrollbar = self.verticalScrollBar()
        if verticalScrollbar is None:
            return
        verticalScrollbar.setValue(verticalScrollbar.maximum())

    def buildListItemWidgetLayout(self, name: str, listWidgetItem: QListWidgetItem) -> QHBoxLayout:

        deleteBtn = QPushButton(self.deleteIcon, '')
        deleteBtn.setFixedSize(ICON_SIZE, ICON_SIZE)

        deleteBtn.setStyleSheet("border: none; padding: 0px;")

        deleteBtn.enterEvent = lambda event: deleteBtn.setIcon(self.accentDeleteIcon) # type: ignore
        deleteBtn.leaveEvent = lambda event: deleteBtn.setIcon(self.deleteIcon) # type: ignore

        deleteBtn.pressed.connect(lambda: deleteBtn.setIcon(self.accentDarkDeleteIcon))
        deleteBtn.released.connect(lambda: deleteBtn.setIcon(self.deleteIcon))

        deleteBtn.clicked.connect(lambda: self.deleteListItemAction(listWidgetItem))

        label = QLabel(name)

        font = QFont(self.params.fontFamily, 13)
        label.setStyleSheet('color: white;')
        label.setFont(font)

        if not self.params.haveHorizontalScroll:
            label.setMaximumWidth(self.width() - ICON_SIZE - 47)

        layout = QHBoxLayout()
        layout.setContentsMargins(7, 7, 7, 7)

        layout.addWidget(label)
        layout.addWidget(deleteBtn)

        return layout

    def deleteListItemAction(self, itemWidget):
        item = self.item(self.row(itemWidget))
        self.takeItem(self.row(item))
        self.afterListChange()

    def getStringItems(self) -> list:
        elements = []

        for i in range(self.count()):
            item = self.item(i)
            if item is None:
                continue
            itemText = item.text()
            elements.append(itemText)

        return elements
