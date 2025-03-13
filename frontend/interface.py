import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.ia import IA
import random

class InterfaceJogo:
    def __init__(self, master):
        self.master = master
        self.master.title("🎲 Funny Guessing Game 🎉")
        self.master.geometry('350x250')
        self.master.configure(bg='#ffe680')

        self.ia = IA()
        self.numero_secreto = random.randint(1, 100)

        self.label = tk.Label(master, text="🎯 Guess a number between 1 - 100 🎯", font=('Comic Sans MS', 12), bg='#ffe680')
        self.label.pack(pady=15)

        self.entry = tk.Entry(master, font=('Comic Sans MS', 12), justify='center')
        self.entry.pack(pady=10)

        self.btn_adivinhar = tk.Button(master, text="🤔 Guess 🤔", command=self.verificar, font=('Comic Sans MS', 10), bg='#ff6666')
        self.btn_adivinhar.pack(pady=5)

        self.btn_ia = tk.Button(master, text="🧠 AI Suggestion 🧠", command=self.sugerir, font=('Comic Sans MS', 10), bg='#66b3ff')
        self.btn_ia.pack(pady=5)

    def verificar(self):
        try:
            chute = int(self.entry.get())
            if chute == self.numero_secreto:
                messagebox.showinfo("🎉 Result 🎉", "🥳 Congratulations, you got it! 🎈")
                self.ia.registrar_tentativa(chute, True)
                self.numero_secreto = random.randint(1, 100)
            else:
                dica = "lower ⬇️" if chute > self.numero_secreto else "bigger ⬆️"
                messagebox.showinfo("🤔 Try again 🤔", f"Tip: try a number {dica}!")
                self.ia.registrar_tentativa(chute, False)
        except ValueError:
            messagebox.showerror("Error 😱", "Please, insert a valid number!")

    def sugerir(self):
        sugestao = self.ia.prever()
        messagebox.showinfo("💡 AI Suggestion 💡", f"How abaout trying number {sugestao}? 🧠")

