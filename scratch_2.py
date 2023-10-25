# -*- codeing = utf-8 -*-
# @Time : 2020/10/24
# @Author : loadding...
# @File : lab_safety.py
# @Software : jupyter

from lxml import etree
import requests
from selenium import webdriver
import re


def getQuestionBank():
    #     url="http://aqks.neu.edu.cn/redir.php?catalog_id=6&cmd=dajuan_chakan&huihuabh=69338&mode=test"
    url = "http://aqks.neu.edu.cn/"
    response = requests.get(url)
    page_source = response.text
    # print(page_source)
    tree = etree.HTML(page_source)
    arr = tree.xpath('//*[@class="shiti"]/strong')
    # print(arr)


def search_answer(answer_source, question):
    # 匹配判断题答案
    # s=question+'</strong>（分值1.0）<br/>你未作答标准答案：(.{2,4}?)</div>'

    # 查了好久，终于知道为什么有的答案搜索不到了，比如某些问题里带有?，而?在正则里是有含义的，需要转义
    question = question.replace('?', '\\?')
    question = question.replace('(', '\\(')
    question = question.replace(')', '\\)')
    # .*?非贪婪模式匹配，匹配判断题、选择题

    s = question + '.*?你未作答标准答案：(?P<answer>.*?)</div>'
    # s='灾初起阶段是扑救火灾()的阶段。.*?你未作答标准答案：(.{1,2}?)</div>'
    # print(s)
    pattern = re.compile(s)
    # 获取答案
    answer = re.findall(pattern, answer_source)
    # 返回搜索到的答案列表，注意可能为空列表
    # print(answer)
    return answer


if __name__ == '__main__':

    while (1):
        # 登录网站
        print(
            "****************************欢迎来到实验室安全考试系统，本程序是自动答题脚本，祝您玩的愉快！！！*************************")
        username = input('请输入学号：')
        password = input('请输入密码：')
        # 实例化出一个Firefox浏览器
        dr = webdriver.Chrome()
        dr.get("http://aqks.neu.edu.cn/")
        dr.find_element_by_id('u1').send_keys(username)
        dr.find_element_by_id('password').send_keys(password)
        # 点击提交登录
        dr.find_element_by_xpath('//*[@id="web_login"]/div/form/div[3]/input').click()
        if dr.current_url == 'http://aqks.neu.edu.cn/':
            print("用户名或密码错误！请重新登录！！！")
        else:
            break

    # 点击导航栏安全考试
    dr.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[3]/a').click()
    while (1):
        type = input('模拟考试/开始考试（输入1或2）：')
        if type == '1':
            # 点击模拟考试
            dr.find_element_by_xpath('//*[@id="article"]/div[4]/div[2]/div/a[1]').click()
            break
        elif type == '2':
            # 点击开始考试
            dr.find_element_by_xpath('//*[@id="article"]/div[4]/div[2]/div/a[2]').click()
            break
        else:
            print("输入错误，请重输！！！")

    # 提取问题，定位的是第一个元素不是一个列表，改用其他方法
    # question=dr.find_element_by_class_name('shiti').text[2:-4]

    # 获取答案
    url = "http://aqks.neu.edu.cn/redir.php?catalog_id=6&cmd=dajuan_chakan&huihuabh=69338&mode=test"
    response = requests.get(url)
    response.encoding = 'gbk'  # 网页是gbk编码
    answer_source = response.text
    # 去掉所有的空白符，包括换行符和空格、制表符
    answer_source = re.sub('\s', '', answer_source)
    # print(answer_source)
    # 共有10页，每页10题
    page = 0
    while (page < 10):
        # 获取当前页面源码（答题页）
        page_source = dr.page_source
        tree = etree.HTML(page_source)
        question_list = tree.xpath('//h3')
        for i in range(10):
            question = question_list[i]
            # 因为最大题号是100，再加上符号，所以从4开始截取
            question = question.xpath('string(.)')[4:]
            # 有的问题也会带有空格，先处理掉
            question = re.sub('\s', '', question)
            # 搜索答案
            answer = search_answer(answer_source, question)
            # print(answer)
            if (len(answer) == 0):
                print("第" + str(10 * page + i + 1) + "题未搜索到答案!")
                print("问题是：" + question)
                continue
            answer = answer[0]
            # 拼接按钮元素的id
            id = 'ti_' + str(10 * page + i + 1)
            if answer == '错误' or answer == 'A':
                id = id + '_0'
            elif answer == '正确' or answer == 'B':
                id = id + '_1'
            elif answer == 'C':
                id = id + '_2'
            elif answer == 'D':
                id = id + '_3'
            else:
                print("搜索答案失败！！！")
                continue
            dr.find_element_by_id(id).click()
        if page == 0:
            # 第一页时，点击下一页是input[1],其它页面是input[2]
            path = '//*[@id="dati"]/div[11]/input[1]'
        else:
            path = '//*[@id="dati"]/div[11]/input[2]'
        dr.find_element_by_xpath(path).click()
        page = page + 1
    # 答题页面共有10页
    for i in range(10):
        pass