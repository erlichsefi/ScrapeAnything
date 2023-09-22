

def start_browesr(dockerized=True,headless=False,selenium_host="host.docker.internal"):
  from selenium import webdriver
  from selenium.webdriver.chrome.service import Service

  
  chrome_options = webdriver.ChromeOptions()
  
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--lang=en')
  if headless:
    chrome_options.headless = True
    chrome_options.add_argument('--headless')
  if dockerized:
    return webdriver.Remote(f"http://{selenium_host}:4444/wd/hub",options=chrome_options)
  
  service = Service(executable_path=r'/usr/bin/chromedriver')
  return webdriver.Chrome(service=service,options=chrome_options)

def load_script(filepath):
  with open(filepath, 'r', encoding='utf-8') as f:
      return "".join(f.readlines())

def run_js_code(wd,filepath):
  script = f"""
  var consoleLogs = [];
  var originalLog = console.log;
  console.log = function(message) {{
      consoleLogs.push(message);
      originalLog.apply(console, arguments);
  }};

  {load_script(filepath)}

  return consoleLogs;
  """
  return wd.execute_script(script)


def web_driver_to_image(wd,file_name):
  full_path = f"{file_name}.png"
  wd.save_screenshot(full_path)
  return full_path


def web_driver_to_html(wd,file_name):
  # Get the page source HTML
  html_content = wd.page_source
  full_path = f"{file_name}.html"
  # Save the HTML content to a file
  with open(full_path, 'w', encoding='utf-8') as f:
      f.write(html_content)
  return full_path


def draw_on_screen(webdriver,filename,x,y,**kwarg):
  from PIL import Image, ImageDraw,ImageFont
  # Perform mouse click at X and Y coordinates
  # Open the screenshot image using Pillow
  final_fname = f"{filename}_click_location"
  final_fname = web_driver_to_image(webdriver,final_fname)
  image = Image.open(final_fname)

  # Create a drawing context on the image
  draw = ImageDraw.Draw(image)

  # Define the size of the marker
  marker_size = 10

  # Draw a marker at the specified coordinates
  draw.rectangle([(x - marker_size, y - marker_size), (x + marker_size, y + marker_size)], outline="red")

  if "text" in kwarg:
    text_x = x  # X coordinate for the text (centered with the rectangle)
    text_y = y - marker_size - 20  # Y coordinate above the rectangle
    draw.text((text_x, text_y), kwarg['text'], fill="black")


  # Save the marked screenshot

  image.save(final_fname)
  return filename


def get_screen_size(webdriver):
  window_size = webdriver.get_window_size()
  width = window_size["width"]
  height = window_size["height"]
  return width,height

from selenium.webdriver.support.ui import WebDriverWait

def wait_for_page_load(wdriver):
    wait = WebDriverWait(wdriver, 60)

    def page_loaded(driver):
        return driver.execute_script("return document.readyState") == "complete"

    wait.until(page_loaded)