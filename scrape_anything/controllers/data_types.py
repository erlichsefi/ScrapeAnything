class IncommingData:
    viewpointscroll:int
    viewportHeight:int
    scroll_ratio:int

    # f"width={width},height={height}"
    width:str
    height:str

    # data from the screen
    raw_on_screen:list

    def __init__(self,viewpointscroll,viewportHeight,scroll_ratio,width,height,raw_on_screen) -> None:
        self.viewpointscroll = viewpointscroll
        self.viewportHeight = viewportHeight
        self.scroll_ratio = scroll_ratio
        self.width = width
        self.height = height
        self.raw_on_screen = raw_on_screen



    
class OutGoingData:

    def __init__(self,description:str,**kwarg) -> None:
        description:str = description
        kwarg = kwarg
   