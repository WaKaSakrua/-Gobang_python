import tkinter as tk
import wuziqi
import WuZiQi_AI
def renren():
    page=wuziqi.qipan(15)
def  renji():
    page=WuZiQi_AI.qipan(15)
root=tk.Tk()
root.geometry("400x300")
button_login1 = tk.Button(root, text="人人对战", command=renren)
button_login1.place(x=50, y=100, width=100, height=50)
button_login2 = tk.Button(root, text="人机对战", command=renji)
button_login2.place(x=250, y=100, width=100, height=50)
root.mainloop()

