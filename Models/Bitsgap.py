from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time, sys


class Bitsgap:
    def __init__(self, credentials, max_number_of_pairs):
        self.credentials = credentials
        self.max_number_of_pairs = max_number_of_pairs

        self.init_driver()


    def init_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        options.add_argument("--kiosk")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        time.sleep(5)


    def login(self):
        self.driver.get("https://bitsgap.com/sign-in/?d=app")
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//input[@id='lemail']")))
        self.driver.find_element_by_xpath("//input[@id='lemail']").send_keys(self.credentials.username)
        self.driver.find_element_by_xpath("//input[@id='lpassword']").send_keys(self.credentials.password)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='strategies__list']")))
        

    def get_month(self):
        #print("Month")
        time.sleep(5)
        d = {}
        listd = []
        pairs_counter = 0

        self.driver.find_element_by_xpath("//div[@class='strategies-list__item']").click()
        actions = ActionChains(self.driver)

        for i in range(0, self.max_number_of_pairs):
            month = self.driver.find_element_by_xpath("//div[@class='strategies-list']")
            months = month.text.splitlines()

            for j in range(0, int(len(months) / 2), 2):
                if pairs_counter >= self.max_number_of_pairs:
                    break #TODO: return

                pairs_counter = pairs_counter + 1
                print(pairs_counter)
        
                #print(months[j] + " :  " + months[j + 1])
                d[months[j]] = months[j + 1]
                dxj = {'pair': months[j], 'profit': months[j+1]}
                listd.append(dxj)

            if pairs_counter >= self.max_number_of_pairs:
                break #TODO: remove duplicate condition

            actions.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN)
            actions.perform()
            time.sleep(2)

        print("------------final--------------------month-------------")
        #print(d)
        print(dict(list(d.items())[0: self.max_number_of_pairs]))
        print(listd)

                
        self.driver.quit()
        sys.exit(0)
        
        
    def get_week(self):
        strategies = self.driver.find_element_by_xpath("//div[@class='strategies']")
        strategies.find_element_by_xpath("//span[contains(text(),'Month')]").click()
        time.sleep(2)
        self.driver.find_elements_by_xpath("//li[@class='MuiButtonBase-root MuiListItem-root MuiMenuItem-root strategies__menu-item MuiMenuItem-gutters MuiListItem-gutters MuiListItem-button']")[1].click()
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='strategies__list']")))
        print("Week")
        time.sleep(5)
        d2 = {}
        listd2 = []


        self.driver.find_element_by_xpath("//div[@class='strategies-list__item']").click()
        actions = ActionChains(self.driver)
        for i in range(0, 25):
            month = self.driver.find_element_by_xpath("//div[@class='strategies-list']")
            months = month.text.splitlines()
            for j in range(0, int(len(months) / 2), 2):
                # print(months[j] + " :  " + months[j + 1])
                #dxj = {'pair': months[j], 'profit': months[j+1]}
                #listd2.append(dxj)
                
                d2[months[j]] = months[j + 1]
            actions.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN)
            actions.perform()
            time.sleep(2)

        print("------------final--------------------week-------------")
        # print(d2)
        print(dict(list(d2.items())[0: self.max_number_of_pairs]))
        #print(listd2)

        
    def get_three_days(self):
        strategies = self.driver.find_element_by_xpath("//div[@class='strategies']")
        strategies.find_element_by_xpath("//span[contains(text(),'Week')]").click()

        self.driver.find_elements_by_xpath("//li[@class='MuiButtonBase-root MuiListItem-root MuiMenuItem-root strategies__menu-item MuiMenuItem-gutters MuiListItem-gutters MuiListItem-button']")[0].click()
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='strategies__list']")))
        print("3 days")
        time.sleep(5)
        d3 = {}
        listd3 = []

        self.driver.find_element_by_xpath("//div[@class='strategies-list__item']").click()
        actions = ActionChains(self.driver)
        for i in range(0, 25):
            month = self.driver.find_element_by_xpath("//div[@class='strategies-list']")
            months = month.text.splitlines()
            for j in range(0, int(len(months) / 2), 2):
                # print(months[j] + " :  " + months[j + 1])
                #dxj = {'pair': months[j], 'profit': months[j+1]}
                #listd3.append(dxj)
                d3[months[j]] = months[j + 1]
            actions.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN)
            actions.perform()
            time.sleep(2)


        print("------------final--------------------day-------------")
        # print(d3)
        print(dict(list(d3.items())[0: self.max_number_of_pairs]))
        #print(listd3)


    def cleanup(self):
        self.driver.quit()

