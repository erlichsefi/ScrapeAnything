class IncommingData:
    viewpointscroll:int
    viewportHeight:int
    scroll_width:int
    scroll_height:int

    # f"width={width},height={height}"
    width:str
    height:str

    # data from the screen
    raw_on_screen:list

    def __init__(self,url,task,viewpointscroll,viewportHeight,scroll_width,scroll_height,width,height,raw_on_screen) -> None:
        self.viewpointscroll = viewpointscroll
        self.viewportHeight = viewportHeight
        self.scroll_width = scroll_width
        self.scroll_height = scroll_height
        self.width = width
        self.height = height
        self.raw_on_screen = raw_on_screen
        self.url = url
        self.task = task


from enum import Enum
class EnabledActions(Enum):
    ClickOnCoordinates = 0
    EnterText = 1 
    GoBack = 2 
    ScrollRight = 3
    ScrollUp = 4
    ScrollDown = 5
    Refresh = 6 
    HitAKey = 7

    def filter_enabled(possible_tools):
        return list(filter(lambda x: type(x).__name__ in EnabledActions.__members__.keys(),possible_tools))

    
class OutGoingData:

    def __init__(self,description:str,**kwarg) -> None:
        #client_enum = Actions.
        description:str = description
        kwarg = kwarg
   