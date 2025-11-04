import tkinter as tk
from xml.etree.ElementTree import canonicalize
import random
from tkinter import simpledialog, colorchooser


try:
    from happiness.data_loader import load_data
except:
    pass

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DemoGUI")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack(fill="both", expand=True)

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        m_tasks = tk.Menu(menubar, tearoff=False)
        m_tasks.add_command(label="Exit", command=self.root.destroy)

        menubar.add_cascade(label="Systems", menu=m_tasks)

        m_colors = tk.Menu(menubar, tearoff=False)
        m_colors.add_command(label="Red", command=lambda:self.set_bg("red"))
        m_colors.add_command(label="Green", command=lambda:self.set_bg("green"))
        m_colors.add_command(label="Blue", command=lambda:self.set_bg("blue"))
        m_colors.add_command(label="White", command=lambda:self.set_bg("white"))

        menubar.add_cascade(label="Colors", menu=m_colors)

        m_grafics = tk.Menu(menubar, tearoff=False)
        m_grafics.add_command(label="Bar code", command=lambda:self.magic_bar_code(1, 20, ))
        m_grafics.add_command(label="Chessboard", command=lambda:self.chessboard(8))
        m_grafics.add_command(label="Target", command=lambda:self.set_bg("Target"))

        menubar.add_cascade(label="Grafics", menu=m_grafics)

    def _canvas_size(self) -> tuple[int, int]:
        w = self.canvas.winfo_width() or self.root.winfo_width() or 640
        h = self.canvas.winfo_height() or self.root.winfo_height() or 480
        return w, h

    def chessboard(self, size:int = 8):
        self.clear()
        self.canvas.config(background="white")
        w, h = self._canvas_size()
        cell_x = w /size
        cell_y = h /size
        for i in range(size):
            for j in range(size):
             self.canvas.create_rectangle(i*cell_x, j*cell_y, i*cell_x + cell_x, j*cell_y +cell_y, fill=f"#{random.randint(0,0xffffff):06x}")




    def magic_bar_code(self, min:int, max:int) -> None:
        self.clear()
        self.canvas.config(background="white")
        x = int(0)
        w, h = self._canvas_size()
        #Nefunguje w
        while x < w:
            width = random.randint(min, max)
            color = f"#{random.randint(0,0xffffff):06x}"
            self.canvas.create_line(x, 0, x, h, fill=color, width=width)
            x += width

    # None znamená žádný return - modernější
    def set_bg(self, color:str) -> None:
        self.canvas.config(background=color)

    def clear(self) -> None:
        self.canvas.delete("all")


    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    App().run()