def start_browesr():
  from selenium import webdriver
  from selenium.webdriver.chrome.service import Service

  service = Service(executable_path=r'/usr/bin/chromedriver')
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--headless=new')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--lang=en')
  chrome_options.headless = True
  return webdriver.Chrome(service=service,options=chrome_options)




wd = start_browesr()
print(wd.get("https://www.google.com").page_source)