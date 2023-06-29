import pyttsx3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "Database\chromedriver.exe"
driver = webdriver.Chrome(Path, options=chrome_options)
driver.maximize_window()

web = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(web)
ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')

def say(text):
    length = len(str(text))

    if length == 0:
        pass
    else:
        print(f"\n JARVIS: {text} \n")
        data = str(text)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()

        if length >= 30:
            sleep(4)
        elif length >= 40:
            sleep(6)
        elif length >= 55:
            sleep(8)
        elif length >= 70:
            sleep(10)
        elif length >= 100:
            sleep(13)
        elif length >= 120:
            sleep(14)
        else:
            sleep(2)

say("Hello")
