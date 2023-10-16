import pandas as pd
from datetime import datetime
import os
import time
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, JavascriptException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select



class Absen():
    def __init__ (self, username, password) :
        self.username = username
        self.password = password
        

    def absen(self):

        # Define executable path
        executable_path = r"A:\chromedriver-win64\chromedriver-win64\chromedriver.exe" #Windows
        service = Service(executable_path)

        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--headless=new")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False) 
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(service=service, options=options)

        driver.get("https://logbook.pajak.go.id") 
        time.sleep(10)

        username_el = driver.find_element(By.XPATH, '//*[@id="nip"]')
        password_el = driver.find_element(By.XPATH, '//*[@id="password"]')
        username_el.clear()
        username_el.send_keys(self.username)
        password_el.clear()
        password_el.send_keys(self.password)
        masuk = driver.find_element(By.XPATH, '//*[@id="m_login_signin_submit"]')
        masuk.click()
        time.sleep(10)

        presensi = driver.find_element(By.XPATH, '//*[@id="btnPresensi"]')
        presensi.click()
        
        driver.close()

def main():
    absen_instance = Absen('817932702', 'rad10headK11D@')
    # Memanggil metode absen melalui objek absen_instance
    absen_instance.absen()
    sys.exit(0)

if __name__ == "__main__":
    main()
    



