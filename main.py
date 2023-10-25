from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv
import difflib
from lxml import etree
import tkinter as tk
def close_window():
    root.destroy()

root = tk.Tk()
root.title("欢迎")

# 设置窗口内容为 "欢迎使用本程序"
label1 = tk.Label(root, text="湖南大学实验室安全考试自动答题程序", font=('Arial', 16))
label1.pack(pady=10)

label2 = tk.Label(root, text="请确认使用校园网和Chrome浏览器", font=('Arial', 14))
label2.pack(pady=10)

label3 = tk.Label(root, text="Created By: JesterHey", font=('Arial', 14))
label3.pack(pady=5)

label4 = tk.Label(root, text="针对湖大物电院优化题库", font=('Arial', 14))
label4.pack(pady=10)

# 设置窗口大小并使其居中
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width / 2) - (window_width / 2)
y_pos = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_pos)}+{int(y_pos)}")

# 设置5秒后自动关闭窗口
root.after(5000, close_window)

root.mainloop()


# 初始化用户名、密码和选择为空字符串
username = ""
password = ""
choice = ""

def get_input(event=None):
    global username, password, choice
    username = username_entry.get()
    password = password_entry.get()
    choice = choice_entry.get()
    root.destroy()  # 关闭窗口

root = tk.Tk()
root.title("登录窗口")

# 设置窗口大小并使其居中
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width / 2) - (window_width / 2)
y_pos = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_pos)}+{int(y_pos)}")

# 创建用户名标签和输入框
tk.Label(root, text="学号").pack(pady=10)
username_entry = tk.Entry(root)
username_entry.pack(pady=10)
username_entry.bind('<Return>', get_input)

# 创建密码标签和输入框
tk.Label(root, text="个人门户密码").pack(pady=10)
password_entry = tk.Entry(root,show='*')
password_entry.pack(pady=10)
password_entry.bind('<Return>', get_input)

# 创建选择模式标签和输入框
tk.Label(root, text="Enter 1 (模拟考) or 2 (正式考):").pack(pady=10)
choice_entry = tk.Entry(root)
choice_entry.pack(pady=10)
choice_entry.bind('<Return>', get_input)

# 创建按钮来获取输入
tk.Button(root, text="提交", command=get_input).pack(pady=20)

root.mainloop()

opt= Options()
opt.add_experimental_option("detach", True)
def find_similar_values(value_to_search,page=0,filename='quzibase.csv',threshold=0.5): #设置匹配度阈值
    results = []

    value_to_search = value_to_search.replace('?', '\\?')
    value_to_search = value_to_search.replace('(', '\\(')
    value_to_search = value_to_search.replace(')', '\\)')


    with open(filename, 'r',encoding='utf8') as f:
        reader = csv.reader(f)

        for row in reader:
            similarity = difflib.SequenceMatcher(None, row[0], value_to_search).ratio()
            if similarity >= threshold:
                results.append(row[1])

    if results == []:
        return results
    elif page<=4:
        l1=[]
        for i in results:
            if i == '正确' or i =='错误':
                l1.append(i)
                return l1
    else:
        l1=[]
        for item in results:
            if item in 'ABCD':
                l1.append(item)
                return l1
    return results
safari = Chrome(options=opt)
url = 'https://labsafe.hnu.edu.cn/labexam/index.php'
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
choice = int(choice)
safari.find_element(By.XPATH,f'//*[@id="article"]/div[4]/div[2]/div/a[{choice}]').click()
time.sleep(1)
def clickanswer(l:list,page,index):
    if l == []:
        print('no answer')
    elif l[0] == '错误' or l[0] == 'A':
        _id = 'ti_'+ str(page*10+index) + '_0'
        safari.find_element(By.ID,_id).click()
    elif l[0] == '正确' or l[0] == 'B':
        _id = 'ti_'+ str(page*10+index) + '_1'
        safari.find_element(By.ID,_id).click()
    elif l[0] == 'C':
        _id = 'ti_'+ str(page*10+index) + '_2'
        safari.find_element(By.ID,_id).click()
    elif l[0] == 'D':
        _id = 'ti_'+ str(page*10+index) + '_3'
        safari.find_element(By.ID,_id).click()
    pass
# def findanswer(s:str,answersource):
#     s = s.split('、')[1]
#     s = s.replace('?', '\\?')
#     s = s.replace('(', '\\(')
#     s = s.replace(')', '\\)')
#     s = s + '.*?你未作答标准答案：(?P<answer>.*?)</div>'
#     pattern = re.compile(s)
#     answer = re.findall(pattern, answersource)
#     return answer
for page in range(10): #i是页码
    if page == 0:
        answerlist=[]
        page_source = safari.page_source
        htmltxt = etree.HTML(page_source)
        for tihao in range(1,11):
            qtxt = htmltxt.xpath(f'//*[@id="dati"]/div[{tihao}]/h3/text()')[0].split('、')[-1]
            answer = find_similar_values(value_to_search=qtxt,page=page)
            answerlist.append(answer)
        co=1
        while co<=10:
            clickanswer(answerlist[co-1],page,co)
            co+=1
        # <input type="radio" name="ti_91" id="ti_91_1" value="B">
        # count = 0
        # for i in answerlist:
        #     if i == []:
        #         count+=1
        # print(answerlist,end='  ')
        # print(f'有{count}个题目未匹配到答案')
        safari.find_element(By.XPATH,'//*[@id="dati"]/div[11]/input[1]').click()
        time.sleep(1)
    elif 1<=page<9:
        answerlist=[]
        page_source = safari.page_source
        htmltxt = etree.HTML(page_source)
        for tihao in range(1,11):
            qtxt = htmltxt.xpath(f'//*[@id="dati"]/div[{tihao}]/h3/text()')[0].split('、')[-1]
            answer = find_similar_values(page=page,value_to_search=qtxt)
            answerlist.append(answer)
        co = 1
        while co <= 10:
            clickanswer(answerlist[co - 1], page, co)
            co += 1
        # count = 0
        # for i in answerlist:
        #     if i == []:
        #         count+=1
        # print(answerlist,end='  ')
        # print(f'有{count}个题目未匹配到答案')
        safari.find_element(By.XPATH,'//*[@id="dati"]/div[11]/input[2]').click()
        time.sleep(1)
    else:
        answerlist = []
        page_source = safari.page_source
        htmltxt = etree.HTML(page_source)
        for tihao in range(1,11):
            qtxt = htmltxt.xpath(f'//*[@id="dati"]/div[{tihao}]/h3/text()')[0].split('、')[-1]
            answer = find_similar_values(value_to_search=qtxt,page=page)
            answerlist.append(answer)
        co = 1
        while co <= 10:
            clickanswer(answerlist[co - 1], page, co)
            co += 1
        # # <input type="radio" name="ti_91" id="ti_91_1" value="B">
        # count = 0
        # for i in answerlist:
        #     if i == []:
        #         count+=1
        # print(answerlist,end='  ')
        # print(f'有{count}个题目未匹配到答案')