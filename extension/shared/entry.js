import draw_arrow from './actions/draw_arrow.js'
import go_to_url from './actions/go_to_url.js'
import scroll_down from './actions/scroll_down.js'
import scroll_up from './actions/scroll_up.js'
import scroll_left from './actions/scroll_left.js'
import scroll_right from './actions/scroll_right.js'
import show_text from './actions/show_text.js'

function call_action(function_name,args){
    if (function_name == "draw_arrow"){
        return draw_arrow(args.text,args.x,args.y)
    }
    else if (function_name == "go_to_url"){
        return go_to_url()
    }
    else if (function_name == "scroll_down"){
        return scroll_down()
    }
    else if (function_name == "scroll_up"){
        return scroll_up()
    }
    else if (function_name == "scroll_left"){
        return scroll_left()
    }
    else if (function_name == "scroll_right"){
        return scroll_right()
    }
    else if (function_name == "show_text"){
        return show_text(args.text)
    }
    else{
        throw new Error('function '+function_name+" is not defined.");
    }

}

import get_elements from './extract/elements.js'
import get_url from './extract/get_url.js'
import getWindowSize from './extract/get_window_size.js'
import getScrollHeightInfo from './extract/scroll_height.js'
import getScrolWidthInfo from './extract/scroll_width.js'
import get_viewpoint from './extract/window.js'


async function  call_extract(function_name){
    if (function_name == "elements"){
        return get_elements()
    }
    else if (function_name == "get_url"){
        return get_url()
    }
    else if (function_name == "get_window_size"){
        return getWindowSize()
    }
    else if (function_name == "scroll_height"){
        return await getScrollHeightInfo()
    }
    else if (function_name == "scroll_width"){
        return await getScrolWidthInfo()
    }
    else if (function_name == "window"){
        return get_viewpoint()
    }
    else{
        throw new Error('function '+function_name+" is not defined.");
    }

}

export {call_action,call_extract};