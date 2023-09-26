from scrape_anything.browser import action_with_js_code

import os
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))




def draw_arrow(web_driver,x,y,text=""):
    action_with_js_code(web_driver,os.path.join(CURRENT_PATH,"draw_arrow.js"),x=x,y=y,text=text)