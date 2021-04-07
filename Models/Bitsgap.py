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
        #options.add_argument("--kiosk")
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
        self.__wait_for_strategy_list()
        

    def __get_pairs(self):
        results = []

        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@class='strategies-list__item']").click()
        actions = ActionChains(self.driver)

        for i in range(0, self.max_number_of_pairs):

            pairs_and_profit, pairs_range = self.__get_pairs_and_profit_list()

            for j in pairs_range:
                pair_index = j
                profit_index = j + 1

                results.append( { 
                    'pair': pairs_and_profit[ pair_index ], 
                    'profit': pairs_and_profit[ profit_index ] 
                } )

                # Remove repeated pairs
                results = list({frozenset(item.items()) : item for item in results}.values())
                if len(results) >= self.max_number_of_pairs:
                    return results

            self.__scroll_list_down()
            
        return results


    def __get_pairs_and_profit_list(self):
            pairs_and_profit__dom = self.driver.find_element_by_xpath("//div[@class='strategies-list']")
            pairs_and_profit = pairs_and_profit__dom.text.splitlines()

            pairs_amount = int( len( pairs_and_profit ) / 2 )
            pairs_range = range(0, pairs_amount, 2 )
            
            return pairs_and_profit, pairs_range


    def get_month(self):        
        monthly_pairs = self.__get_pairs()
        
        print(monthly_pairs)
        print("------------final--------------------month-------------")
                
        
    def get_week(self):
        self.__switch_list(current_text = 'Month', index = 1)
        
        weekly_pairs = self.__get_pairs()
        print(weekly_pairs)
        print("------------final--------------------Week-------------")

        
    def get_three_days(self):
        self.__switch_list(current_text = 'Week', index = 0)
                
        daily_pairs = self.__get_pairs()
        print(daily_pairs)
        print("------------final--------------------Daily-------------")


    def __switch_list(self, current_text = 'Month', index = 1):
        strategies = self.driver.find_element_by_xpath("//div[@class='strategies']")
        xpath_str = "//span[contains(text(),'{}')]".format(current_text)
        strategies.find_element_by_xpath( xpath_str ).click()
        time.sleep(2)
        self.driver.find_elements_by_xpath("//li[@class='MuiButtonBase-root MuiListItem-root MuiMenuItem-root strategies__menu-item MuiMenuItem-gutters MuiListItem-gutters MuiListItem-button']")[index].click()
        time.sleep(2)
        self.__wait_for_strategy_list()


    def __wait_for_strategy_list(self):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='strategies__list']")))


    def __scroll_list_down(self):
        self.driver.execute_script("document.querySelector('.strategies-list').scrollBy(0,100)")
        time.sleep(2)


    def cleanup(self):
        self.driver.quit()
