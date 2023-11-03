from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
from lxml import etree
import csv
# 可以设置无头浏览器
# opt= Options()
# opt.add_experimental_option("detach", True)
# opt.add_argument('--headless')
username = input('请输入学号')
password = input('请输入密码')
for _ in range(5):
    url = 'https://labsafe.hnu.edu.cn/labexam/index.php'
    safari = Chrome()
    safari.get(url)
    time.sleep(1)
    el = safari.find_element(By.XPATH,'//*[@id="formExam"]/div/a/input')
    el.click()
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
    #按一下回车提交答案
    alert = safari.switch_to.alert
    alert.accept()
    safari.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[3]/ul/li[1]/a').click()
    #获得答案源代码
    pagetxt = etree.HTML(safari.page_source)
    for i in range(3,101):
        quiztxt = pagetxt.xpath(f'/html/body/div[2]/div[2]/div[2]/div[{i}]/strong/text()')
        answertxt = pagetxt.xpath(f'/html/body/div[2]/div[2]/div[2]/div[{i}]/text()')[-1]
        answertxt=list(str(answertxt).strip())
        tureanswer=''
        if answertxt[-1].isupper() == True:
            tureanswer = answertxt[-1]
        else:
            tureanswer = ''.join(answertxt[::-1][0:2:][::-1])
        if quiztxt == []:
            continue
        else:
            quiztxt = quiztxt[0]
        with open('quizbase.csv', mode='a+') as quz:
            csvwriter=csv.writer(quz)
            csvwriter.writerow([quiztxt,tureanswer])
    safari.close()
