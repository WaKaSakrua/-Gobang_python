import tkinter as tk
from tkinter import messagebox


def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("登录成功", "欢迎，" + username)
    else:
        messagebox.showerror("登录失败", "用户名或密码错误")


root = tk.Tk()
root.title("登录窗口")

# 用户名标签和输入框
label_username = tk.Label(root, text="用户名:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

# 密码标签和输入框
label_password = tk.Label(root, text="密码:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# 登录按钮
button_login = tk.Button(root, text="登录", command=login)
button_login.pack()

root.mainloop()