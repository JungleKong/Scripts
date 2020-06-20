import requests
from selenium import webdriver
import time

url = 'http://one.hrbeu.edu.cn/'
username = "2016071705"
password = "asyouare"

path = r"F:\chromedriver.exe"
# option = webdriver.ChromeOptions()
# option.add_argument('disable-infobars')
my_driver = webdriver.Chrome(executable_path=path)
my_driver.get(url)

my_driver.find_element_by_id("username").send_keys(username)
my_driver.find_element_by_id("password").send_keys(password)
my_driver.find_element_by_name('submit').click()
# print(my_driver.page_source)

for i in range(400):
    js = 'window.scrollTo(0,{});'.format(5*i)
    my_driver.execute_script(js)

my_driver.find_element_by_link_text("平安行动").click()

time.sleep(3)

windows_all = my_driver.window_handles
my_driver.switch_to.window(windows_all[2])

for i in range(300):
    js = 'window.scrollTo(0,{});'.format(5*i)
    my_driver.execute_script(js)

my_driver.find_element_by_id('V1_CTRL82').click()

my_driver.find_element_by_link_text("确认填报").click()
time.sleep(1)
my_driver.find_element_by_xpath('//button[@class="dialog_button default fr"]').click()


# my_driver.find_element_by_class_name("infoplus_checkLabel").click()
# my_driver.find_element_by_class_name("command_button_content").click()
