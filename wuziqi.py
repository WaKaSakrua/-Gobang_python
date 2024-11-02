import tkinter as tk
from tkinter import messagebox
class qipan():
    def __init__(self,n):
        # 定义一个空的棋盘
        self.bord=[[0 for i in range(n) ]for i in range(n)]
        self.current_player="A"
        self.n=n
        self.root=tk.Tk()
        self.root.title("五子棋")
        self.Bet=25
        self.canvas = tk.Canvas(self.root, width=n * self.Bet + 20, height=n * self.Bet + 20, bg="white")
        self.canvas.pack()
        self.show()
        #绘制两个输入框，分别接受x,y的值，并进行事件监听
        # X轴和输入框
        self.label_x = tk.Label(self.root, text="横坐标")
        self.label_x.pack()
        self.entry_x = tk.Entry(self.root)
        self.entry_x.pack()
        # Y轴和输入框
        self.label_y = tk.Label(self.root, text="纵坐标")
        self.label_y.pack()
        self.entry_y = tk.Entry(self.root)
        self.entry_y.pack()
        #确定按钮
        buttun_ensure=tk.Button(self.root,text="确定",command=self.play_move)
        buttun_ensure.pack()
        #定义一个按钮用于实现悔棋过程
        butten_huiqi=tk.Button(self.root,text="悔棋",command=self.huiqi)
        butten_huiqi.place(x=n * self.Bet-50,y=n * self.Bet+50,width=50,height=25)
        #定义一个列表，用于记录下的每一手棋子
        self.history=[]
    #定义一个函数，在按下按钮后，修改当前下棋的玩家，修改五子棋列表,并重新画图
    def play_move(self):
        x=int(self.entry_x.get())
        y=int(self.entry_y.get())
        self.entry_x.delete(0, tk.END)
        self.entry_y.delete(0, tk.END)
        #判断该位置是否有旗子
        if self.bord[x][y] ==0:
            self.bord[x][y]=self.current_player
            self.show()
            if self.check_five_in_row(self.current_player):
                messagebox.showinfo(self.current_player, f"{self.current_player}" + "你赢了")
            self.change_player()
            self.history.append([x,y])
        else:
             messagebox.showerror("输入错误",f"请玩家{self.current_player}重新输入")
    def change_player(self):
        if self.current_player == "A":
            self.current_player = "B"
        else:
            self.current_player = "A"
    def show(self):
        self.canvas.delete('all')
        # 创建Canvas 组件
        n = self.n
        Bet = 25
        canvas = self.canvas
        canvas.pack()
        # 在 Canvas 上绘制线条
        for i in range(n):
            self.canvas.create_line(20 + 0, i * self.Bet + 20, n * self.Bet - 5, i * self.Bet + 20, fill="black")
            self.canvas.create_line(i * self.Bet + 20, 0 + 20, i * self.Bet + 20, n * self.Bet - 5, fill="black")
        #画出画布上的棋子
        for i in range(n):
            for j in range(n):
                if self.bord[i][j]!=0:
                    if self.bord[i][j]=="A":
                        #获取圆心坐标,半径，画出图像
                        X=i*Bet+20
                        Y=j*Bet+20
                        r=8
                        oval=canvas.create_oval(X-r,Y+r,X+r,Y-r)
                        canvas.itemconfigure(oval, fill="red")
                    if self.bord[i][j]=="B":
                        X=i*Bet+20
                        Y=j*Bet+20
                        r=8
                        oval=canvas.create_oval(X-r,Y+r,X+r,Y-r)
                        canvas.itemconfigure(oval, fill="black")
        self.canvas.update()

    #悔棋功能
    def huiqi(self):
        print(self.history)
        if self.history!=[]:
            x,y=self.history[-1]
            del self.history[-1]
            self.bord[x][y]=0
            print(self.bord[x][y])
            self.show()
            self.change_player()
        else:
            messagebox.showerror("悔棋错误","现在已经不可以悔棋了，已经是第一步了")

    # 进行是否五子连心的判断
    def check_five_in_row(self, player):
        board=self.bord
        # 获取棋盘大小
        rows = len(board)
        cols = len(board[0]) if rows > 0 else 0
        # 检查横向是否有五子连心
        for i in range(rows):
            for j in range(cols - 4):
                if board[i][j] == player and board[i][j + 1] == player and board[i][j + 2] == player and \
                        board[i][j + 3] == player and board[i][j + 4] == player:
                    return True

                    # 检查纵向是否有五子连心
        for i in range(rows - 4):
            for j in range(cols):
                if board[i][j] == player and board[i + 1][j] == player and board[i + 2][j] == player and \
                        board[i + 3][j] == player and board[i + 4][j] == player:
                    return True

                    # 检查主对角线方向是否有五子连心
        for i in range(rows - 4):
            for j in range(cols - 4):
                if board[i][j] == player and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player and \
                        board[i + 3][j + 3] == player and board[i + 4][j + 4] == player:
                    return True

                    # 检查副对角线方向是否有五子连心
        for i in range(rows - 4):
            for j in range(4, cols):
                if board[i][j] == player and board[i + 1][j - 1] == player and board[i + 2][j - 2] == player and \
                        board[i + 3][j - 3] == player and board[i + 4][j - 4] == player:
                    return True
                    # 如果没有五子连心，则返回False
        return False