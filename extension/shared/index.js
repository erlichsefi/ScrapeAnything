import draw_arrow from './actions/draw_arrow.js'
import go_to_url from './actions/go_to_url.js'
import scroll_down from './actions/scroll_down.js'
import scroll_up from './shared/actions/scroll_up.js'
import scroll_left from './actions/scroll_left.js'
import scroll_right from './actions/scroll_right.js'
import show_text from './actions/show_text.js'

function call_action(function_name,...args){
    if (function_name == "draw_arrow"){
        return draw_arrow(...args)
    }
    else if (function_name == "go_to_url"){
        return go_to_url(...args)
    }
    else if (function_name == "scroll_down"){
        return scroll_down(...args)
    }
    else if (function_name == "scroll_up"){
        return scroll_up(...args)
    }
    else if (function_name == "scroll_left"){
        return scroll_left(...args)
    }
    else if (function_name == "scroll_right"){
        return scroll_right(...args)
    }
    else if (function_name == "scroll_right"){
        return show_text(...args)
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



function call_extract(function_name,...args){
    if (function_name == "elements"){
        return get_elements(...args)
    }
    else if (function_name == "get_url"){
        return get_url(...args)
    }
    else if (function_name == "get_window_size"){
        return getWindowSize(...args)
    }
    else if (function_name == "scroll_height"){
        return getScrollHeightInfo(...args)
    }
    else if (function_name == "scroll_width"){
        return getScrolWidthInfo(...args)
    }
    else if (function_name == "window"){
        return get_viewpoint(...args)
    }
    else{
        throw new Error('function '+function_name+" is not defined.");
    }

}