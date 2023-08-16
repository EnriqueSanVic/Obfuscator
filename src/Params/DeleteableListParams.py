

class DeleteableListParams:

    def __init__(self, left: int, top: int, width: int, height: int, foregroundColor: str, backgroundColor: str, fontFamily: str, haveHorizontalScroll: bool, moveVerticalScrollToEndWhenUpdateList=False, moveHorizontalScrollToEndWhenUpdateList=False):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.foregroundColor = foregroundColor
        self.backgroundColor = backgroundColor
        self.fontFamily = fontFamily
        self.haveHorizontalScroll = haveHorizontalScroll
        self.moveVerticalScrollToEndWhenUpdateList = moveVerticalScrollToEndWhenUpdateList
        self.moveHorizontalScrollToEndWhenUpdateList = moveHorizontalScrollToEndWhenUpdateList
