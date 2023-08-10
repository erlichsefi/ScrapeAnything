from .dom.filters import minimize_page_data
from .dom.java_script import screen_to_table,screen_to_window_dim,get_scroll_options
from .vision.ocr import get_text_with_confidence

def enrich_base_on_vision(df,filename):
    import cv2,os
    only_filename = filename.split(".")[0]

    values = []
    for _,row in df.iterrows():
        if row['ElementType'] in ['TEXTAREA','INPUT']:
            
            img = cv2.imread(filename)
            img = img[int(float(row['top'])):int(float(row['top']))+int(float(row['height'])),int(float(row['left'])):int(float(row['left']))+int(float(row['width'])),:]
            cv2.imwrite(os.path.join(f"{only_filename}_at_{str(row['centerX'])}_{str(row['centerY'])}.png"), img)
            values.append(get_text_with_confidence(img))
        else:
            values.append("")
    df['innerText'] = values
    return df

def minimize_and_enrich_page_data(df,viewpointscroll,viewportHeight,screenshot_filename):
    df = minimize_page_data(df,viewpointscroll,viewportHeight,using_vision=True)
    df = enrich_base_on_vision(df,screenshot_filename)
    df.drop(columns=['parent_xpath','height','width','top','bottom','left','right'],inplace=True)
    return df


def get_screen_information(web_driver):
    all_elements_on_screen  = screen_to_table(web_driver)

    if all_elements_on_screen.empty:
        raise Exception("wasn't able to see anything on screen.")
    
    viewpointscroll,viewportHeight = screen_to_window_dim(web_driver)
    scroll_ratio = get_scroll_options(web_driver)
    return all_elements_on_screen,viewpointscroll,viewportHeight,scroll_ratio