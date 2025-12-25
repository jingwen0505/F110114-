import tkinter as tk
from tkinter import messagebox
import random

# ================== 主視窗 ==================
root = tk.Tk()
root.title("OOXX 人機對戰")
root.geometry("300x350")
root.resizable(False, False)

# ================== 遊戲狀態 ==================
board = [""] * 9
buttons = []
current_player = "O"
player_can_click = True

# ================== 安全訊息函式 ==================
def show_msg(title, text):
    root.after(0, lambda: messagebox.showinfo(title, text))

# ================== 勝負判斷 ==================
def check_winner():
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

# ================== AI 下棋 ==================
def ai_move():
    global player_can_click, current_player

    empty = [i for i in range(9) if board[i] == ""]
    if not empty:
        return

    i = random.choice(empty)
    board[i] = "X"
    buttons[i].config(text="X", fg="red")

    result = check_winner()
    if result == "Draw":
        show_msg("結果", "平手！")
        reset()
    elif result == "X":
        show_msg("結果", "AI 獲勝！")
        reset()
    else:
        current_player = "O"
        player_can_click = True

# ================== 玩家點擊 ==================
def on_click(i):
    global player_can_click, current_player

    if not player_can_click or board[i] != "":
        return

    board[i] = "O"
    buttons[i].config(text="O", fg="blue")

    result = check_winner()
    if result == "Draw":
        show_msg("結果", "平手！")
        reset()
        return
    elif result == "O":
        show_msg("結果", "你獲勝！")
        reset()
        return

    player_can_click = False
    current_player = "X"
    root.after(300, ai_move)

# ================== 重置遊戲 ==================
def reset():
    global board, current_player, player_can_click
    board = [""] * 9
    current_player = "O"
    player_can_click = True
    for b in buttons:
        b.config(text="")

# ================== 建立棋盤 ==================
for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 20),
        width=6,
        height=3,
        command=lambda i=i: on_click(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# 加一個測試標籤，確認視窗出現
label = tk.Label(root, text="OOXX 遊戲啟動中...", font=("Arial", 14))
label.grid(row=3, column=0, columnspan=3, pady=5)

# ================== 啟動 ==================
root.mainloop()
