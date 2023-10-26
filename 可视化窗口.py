
# 初始化用户名和密码为空字符串
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

# 设置窗口大小并使其居中
window_width = 300
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width / 2) - (window_width / 2)
y_pos = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_pos)}+{int(y_pos)}")

# 设置3秒后自动关闭窗口
root.after(3000, close_window)

root.mainloop()


# 初始化用户名和密码为空字符串
username = ""
password = ""

def get_input(event=None):
    global username, password
    username = username_entry.get()
    password = password_entry.get()
    root.destroy()  # 关闭窗口

root = tk.Tk()
root.title("登录")

# 设置窗口大小并使其居中
window_width = 300
window_height = 200
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
password_entry = tk.Entry(root)
password_entry.pack(pady=10)
password_entry.bind('<Return>', get_input)

# 创建按钮来获取输入
tk.Button(root, text="提交", command=get_input).pack(pady=20)

root.mainloop()

# 输出获取到的用户名和密码
print(f"Username: {username}")
print(f"Password: {password}")
