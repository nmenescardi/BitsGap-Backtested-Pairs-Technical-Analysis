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
from dotenv import load_dotenv
import time, sys, json, os

# Load Env variables:
load_dotenv()
max_number_of_pairs = int(os.getenv("MAX_NUMBER_OF_PAIRS"))
bitsgap_email = os.getenv("BITSGAP_EMAIL")
bitsgap_password = os.getenv("BITSGAP_PASSWORD")

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--kiosk")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
time.sleep(5)
 
driver.get("https://bitsgap.com/sign-in/?d=app")
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//input[@id='lemail']")))
driver.find_element_by_xpath("//input[@id='lemail']").send_keys(bitsgap_email)
driver.find_element_by_xpath("//input[@id='lpassword']").send_keys(bitsgap_password)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='strategies__list']")))
print("Month")
time.sleep(5)
d = {}
listd = []
pairs_counter = 0

driver.find_element_by_xpath("//div[@class='strategies-list__item']").click()
actions = ActionChains(driver)

for i in range(0, max_number_of_pairs):
    month = driver.find_element_by_xpath("//div[@class='strategies-list']")
    months = month.text.splitlines()

    for j in range(0, int(len(months) / 2), 2):
        if pairs_counter >= max_number_of_pairs:
            break #TODO: return

        pairs_counter = pairs_counter + 1
        print(pairs_counter)
 
        #print(months[j] + " :  " + months[j + 1])
        d[months[j]] = months[j + 1]
        dxj = {'pair': months[j], 'profit': months[j+1]}
        listd.append(dxj)

    if pairs_counter >= max_number_of_pairs:
        break #TODO: remove duplicate condition

    actions.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN)
    actions.perform()
    time.sleep(2)

print("------------final--------------------month-------------")
#print(d)
print(dict(list(d.items())[0: max_number_of_pairs]))
print(listd)

driver.quit()
sys.exit(0)

strategies = driver.find_element_by_xpath("//div[@class='strategies']")
strategies.find_element_by_xpath("//span[contains(text(),'Month')]").click()
time.sleep(2)
driver.find_elements_by_xpath("//li[@class='MuiButtonBase-root MuiListItem-root MuiMenuItem-root strategies__menu-item MuiMenuItem-gutters MuiListItem-gutters MuiListItem-button']")[1].click()
time.sleep(2)
WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='strategies__list']")))
print("Week")
time.sleep(5)
d2 = {}
listd2 = []


driver.find_element_by_xpath("//div[@class='strategies-list__item']").click()
actions = ActionChains(driver)
for i in range(0, 25):
    month = driver.find_element_by_xpath("//div[@class='strategies-list']")
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
print(dict(list(d2.items())[0: max_number_of_pairs]))
#print(listd2)


strategies.find_element_by_xpath("//span[contains(text(),'Week')]").click()

driver.find_elements_by_xpath("//li[@class='MuiButtonBase-root MuiListItem-root MuiMenuItem-root strategies__menu-item MuiMenuItem-gutters MuiListItem-gutters MuiListItem-button']")[0].click()
time.sleep(2)
WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='strategies__list']")))
print("3 days")
time.sleep(5)
d3 = {}
listd3 = []

driver.find_element_by_xpath("//div[@class='strategies-list__item']").click()
actions = ActionChains(driver)
for i in range(0, 25):
    month = driver.find_element_by_xpath("//div[@class='strategies-list']")
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
print(dict(list(d3.items())[0: max_number_of_pairs]))
#print(listd3)

driver.quit()
sys.exit(0)