from scrape_anything.browser import action_with_js_code

import os
CURRENT_PATH = os.path.join(os.getcwd(),"shared","actions")


def draw_arrow(web_driver,x,y,text=""):
    action_with_js_code(web_driver,os.path.join(CURRENT_PATH,"draw_arrow.js"),x=x,y=y,text=text)

def scroll_up(web_driver):
    action_with_js_code(web_driver,os.path.join(CURRENT_PATH,"scroll_up.js"))

def scroll_down(web_driver):
    action_with_js_code(web_driver,os.path.join(CURRENT_PATH,"scroll_down.js"))

def scroll_right(web_driver):
    action_with_js_code(web_driver,os.path.join(CURRENT_PATH,"scroll_right.js"))

def scroll_left(web_driver):
    action_with_js_code(web_driver,os.path.join(CURRENT_PATH,"scroll_left.js"))

def go_to_url(web_driver,url):
    action_with_js_code(web_driver,os.path.join(CURRENT_PATH,"go_to_url.js"),url=f"Go to {url}")

def refresh(web_driver):
    action_with_js_code(web_driver,os.path.join(CURRENT_PATH,"show_text.js"),text="refresh the page")

def go_back_a_page(web_driver):
    action_with_js_code(web_driver,os.path.join(CURRENT_PATH,"show_text.js"),text="you should go back a page")

def hit_a_key(web_driver,key):
    action_with_js_code(web_driver,os.path.join(CURRENT_PATH,"show_text.js"),text=f"you should hit {key}")
