import tkinter as tk
from tkinter import messagebox, ttk
import random
from typing import List
import json
import os

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("✨ Tic Tac Toe Game ✨")
        self.window.geometry("500x650")
        self.window.resizable(False, False)
        
        # تعيين الألوان الجميلة
        self.colors = {
            'bg': '#1E1E2E',            # خلفية داكنة أنيقة
            'button': '#2A2A3E',        # لون الأزرار
            'button_hover': '#3A3A4E',  # لون الأزرار عند التحويم
            'text': '#FFFFFF',          # لون النص الأبيض
            'text_secondary': '#B4B4DB', # لون النص الثانوي
            'x_color': '#FF6B6B',       # لون X أحمر فاتح
            'o_color': '#4ECDC4',       # لون O فيروزي
            'win_color': '#95FF95',     # لون الفوز أخضر فاتح
            'reset_button': '#6C5CE7'   # لون زر إعادة التعيين بنفسجي
        }
        
        # تعيين متغيرات اللعبة
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.game_active = True
        self.scores = {"X": 0, "O": 0}
        
        # إنشاء الإطار الرئيسي
        self.main_frame = tk.Frame(self.window, bg=self.colors['bg'])
        self.main_frame.pack(expand=True, fill="both")
        
        # إنشاء عناصر الواجهة
        self.create_ui_elements()
        
        # إضافة تأثيرات التحويم للأزرار
        self.setup_button_hover_effects()
        
    def create_ui_elements(self):
        # إطار العنوان
        title_frame = tk.Frame(self.main_frame, bg=self.colors['bg'])
        title_frame.pack(pady=20)
        
        # العنوان الرئيسي مع الرموز
        title_text = "✨ Tic Tac Toe ✨"
        self.title_label = tk.Label(
            title_frame,
            text=title_text,
            font=("Helvetica", 40, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['text']
        )
        self.title_label.pack()
        
        # عنوان فرعي جميل
        subtitle_text = "Let's Play!"
        self.subtitle_label = tk.Label(
            title_frame,
            text=subtitle_text,
            font=("Helvetica", 16, "italic"),
            bg=self.colors['bg'],
            fg=self.colors['text_secondary']
        )
        self.subtitle_label.pack(pady=5)
        
        # لوحة دور اللاعب
        player_frame = tk.Frame(self.main_frame, bg=self.colors['bg'])
        player_frame.pack(pady=10)
        
        self.turn_label = tk.Label(
            player_frame,
            text=f"Player {self.current_player}'s Turn",
            font=("Helvetica", 18, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['x_color'] if self.current_player == "X" else self.colors['o_color']
        )
        self.turn_label.pack()
        
        # إطار لوحة اللعب
        self.board_frame = tk.Frame(
            self.main_frame,
            bg=self.colors['button'],
            relief="solid",
            borderwidth=2
        )
        self.board_frame.pack(pady=20)
        
        # إنشاء أزرار اللعب
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.board_frame,
                    text="",
                    font=("Helvetica", 32, "bold"),
                    width=3,
                    height=1,
                    command=lambda row=i, col=j: self.make_move(row, col),
                    bg=self.colors['button'],
                    fg=self.colors['text'],
                    relief="flat",
                    borderwidth=1,
                    cursor="hand2"
                )
                button.grid(row=i, column=j, padx=3, pady=3)
                self.buttons.append(button)
        
        # إطار النتيجة
        score_frame = tk.Frame(self.main_frame, bg=self.colors['bg'])
        score_frame.pack(pady=15)
        
        # تصميم جميل للنتيجة
        score_text = f"SCORE"
        self.score_title = tk.Label(
            score_frame,
            text=score_text,
            font=("Helvetica", 16, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['text_secondary']
        )
        self.score_title.pack()
        
        self.score_label = tk.Label(
            score_frame,
            text=f"X: {self.scores['X']}  |  O: {self.scores['O']}",
            font=("Helvetica", 24, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['text']
        )
        self.score_label.pack(pady=5)
        
        # زر إعادة التعيين
        self.reset_button = tk.Button(
            self.main_frame,
            text="New Game",
            font=("Helvetica", 14, "bold"),
            command=self.reset_game,
            bg=self.colors['reset_button'],
            fg=self.colors['text'],
            relief="flat",
            padx=30,
            pady=10,
            cursor="hand2"
        )
        self.reset_button.pack(pady=20)
        
    def setup_button_hover_effects(self):
        def on_enter(event):
            event.widget.config(bg=self.colors['button_hover'])
            
        def on_leave(event):
            if event.widget.cget('text') == "":
                event.widget.config(bg=self.colors['button'])
        
        for button in self.buttons:
            button.bind("<Enter>", on_enter)
            button.bind("<Leave>", on_leave)
            
        # تأثير التحويم لزر إعادة التعيين
        def reset_enter(event):
            self.reset_button.config(bg='#8075E5')
            
        def reset_leave(event):
            self.reset_button.config(bg=self.colors['reset_button'])
            
        self.reset_button.bind("<Enter>", reset_enter)
        self.reset_button.bind("<Leave>", reset_leave)
        
    def check_winner(self) -> bool:
        """التحقق من وجود فائز"""
        # التحقق من الصفوف
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != "":
                return True
        
        # التحقق من الأعمدة
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != "":
                return True
        
        # التحقق من القطر الرئيسي
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        
        # التحقق من القطر الثانوي
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True
        
        return False

    def make_move(self, row: int, col: int):
        """تنفيذ حركة اللاعب"""
        if not self.game_active:
            return
            
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            button = self.buttons[index]
            
            # تحديث لون وشكل الزر
            button.config(
                text=self.current_player,
                fg=self.colors['x_color'] if self.current_player == "X" else self.colors['o_color'],
                bg=self.colors['button_hover']
            )
            
            if self.check_winner():
                self.handle_win()
            elif "" not in self.board:
                self.handle_tie()
            else:
                self.switch_player()
    
    def handle_win(self):
        """معالجة حالة الفوز"""
        self.scores[self.current_player] += 1
        self.update_score()
        
        # تحديث لون الأزرار الفائزة
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # صفوف
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # أعمدة
            [0, 4, 8], [2, 4, 6]              # قطري
        ]
        
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == self.current_player:
                for i in combo:
                    self.buttons[i].config(bg=self.colors['win_color'])
                break
        
        messagebox.showinfo("🎉 Winner!", f"Player {self.current_player} wins! 🏆")
        self.game_active = False
    
    def handle_tie(self):
        messagebox.showinfo("Game Over", "It's a tie! 🤝")
        self.game_active = False
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.turn_label.config(
            text=f"Player {self.current_player}'s Turn",
            fg=self.colors['x_color'] if self.current_player == "X" else self.colors['o_color']
        )
    
    def update_score(self):
        self.score_label.config(
            text=f"X: {self.scores['X']}  |  O: {self.scores['O']}"
        )
    
    def reset_game(self):
        """إعادة تعيين اللعبة"""
        self.board = [""] * 9
        self.game_active = True
        self.current_player = "X"
        
        # إعادة تعيين الأزرار
        for button in self.buttons:
            button.config(
                text="",
                bg=self.colors['button'],
                fg=self.colors['text']
            )
        
        # تحديث نص دور اللاعب
        self.turn_label.config(
            text=f"Player {self.current_player}'s Turn",
            fg=self.colors['x_color']
        )
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run() 