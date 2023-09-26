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

    def __init__(self,viewpointscroll,viewportHeight,scroll_width,scroll_height,width,height,raw_on_screen) -> None:
        self.viewpointscroll = viewpointscroll
        self.viewportHeight = viewportHeight
        self.scroll_width = scroll_width
        self.scroll_height = scroll_height
        self.width = width
        self.height = height
        self.raw_on_screen = raw_on_screen



    
class OutGoingData:

    def __init__(self,description:str,**kwarg) -> None:
        description:str = description
        kwarg = kwarg
   