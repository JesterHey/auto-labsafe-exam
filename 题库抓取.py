from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import re
safari = Chrome()
url = 'https://labsafe.hnu.edu.cn/labexam/index.php'
safari.get(url)
time.sleep(1)
el = safari.find_element(By.XPATH,'//*[@id="formExam"]/div/a/input')
el.click()
username = '202311020126'
password = 'Hnu_hzy0507'
safari.find_element(By.XPATH,'//*[@id="username"]').send_keys(username)
time.sleep(1)
safari.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
time.sleep(1)
safari.find_element(By.XPATH,'//*[@id="dl"]').click()
time.sleep(3)
safari.find_element(By.XPATH,'//*[@id="article"]/div[3]/div[2]/ul/a[1]/li').click()
time.sleep(1)
safari.find_element(By.XPATH,'//*[@id="tkqcl"]/ul/li/label').click()
time.sleep(1)
safari.find_element(By.XPATH,'//*[@id="article"]/div[4]/div[2]/div/a[1]').click()
time.sleep(1)
#定位到下拉列表
sel = safari.find_element(By.XPATH,'//*[@id="runpage"]')
# 包装下拉列表
sel = Select(sel)
sel.select_by_visible_text('10')
time.sleep(1)
safari.find_element(By.XPATH,'//*[@id="dati"]/div[11]/input[2]').click()
time.sleep(1)
#按一下回车
alert = safari.switch_to.alert
alert.accept()