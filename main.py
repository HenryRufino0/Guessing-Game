import tkinter as tk
from frontend.interface import InterfaceJogo

def main():
    root = tk.Tk()
    app = InterfaceJogo(root)
    root.mainloop()

if __name__ == '__main__':
    main()