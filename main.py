from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(
    "/Users/otaviomaior/Documents/chromedriver", chrome_options=options)
river.maximize_window()

driver.get("https://www.folha.uol.com.br/")

classes = ['c-main-headline__url','c-list-links__url', 'c-headline__url', 'c-list-links__url']
classeData = "c-more-options__published-date"
hrefs = []
elements = driver.find_elements_by_class_name(classes[2])

def convertStringToDate(date, formatModel):
    #passado = "2023-08-28 07:00:00"
    #"%Y-%m-%d %H:%M:%S"
    parseDate = datetime.strptime(date, formatModel)
    return parseDate

def differenceCurrentDate(past):
    today = datetime.today()
    return today - past


for el in elements:
    href = el.get_attribute('href')
    if "https://www1.folha.uol.com.br/" in href: 
        hrefs.append(href)
       

for href in hrefs:
    driver.get(href)
    pegaClasseData = driver.find_element_by_class_name('c-more-options__published-date')
    dateTime = pegaClasseData.get_attribute('datetime')
    print(dateTime)
    print(type(dateTime))

driver.close()


