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
        self.master.title("🎲 Jogo Divertido de Adivinhação 🎉")
        self.master.geometry('350x250')
        self.master.configure(bg='#ffe680')

        self.ia = IA()
        self.numero_secreto = random.randint(1, 100)

        self.label = tk.Label(master, text="🎯 Adivinhe o número entre 1 e 100 🎯", font=('Comic Sans MS', 12), bg='#ffe680')
        self.label.pack(pady=15)

        self.entry = tk.Entry(master, font=('Comic Sans MS', 12), justify='center')
        self.entry.pack(pady=10)

        self.btn_adivinhar = tk.Button(master, text="🤔 Adivinhar 🤔", command=self.verificar, font=('Comic Sans MS', 10), bg='#ff6666')
        self.btn_adivinhar.pack(pady=5)

        self.btn_ia = tk.Button(master, text="🧠 Sugestão da IA 🧠", command=self.sugerir, font=('Comic Sans MS', 10), bg='#66b3ff')
        self.btn_ia.pack(pady=5)

    def verificar(self):
        try:
            chute = int(self.entry.get())
            if chute == self.numero_secreto:
                messagebox.showinfo("🎉 Resultado 🎉", "🥳 Parabéns, você acertou! 🎈")
                self.ia.registrar_tentativa(chute, True)
                self.numero_secreto = random.randint(1, 100)
            else:
                dica = "menor ⬇️" if chute > self.numero_secreto else "maior ⬆️"
                messagebox.showinfo("🤔 Tente novamente 🤔", f"Dica: tente um número {dica}!")
                self.ia.registrar_tentativa(chute, False)
        except ValueError:
            messagebox.showerror("Erro 😱", "Por favor, digite um número válido!")

    def sugerir(self):
        sugestao = self.ia.prever()
        messagebox.showinfo("💡 Sugestão da IA 💡", f"Que tal tentar o número {sugestao}? 🧠")

