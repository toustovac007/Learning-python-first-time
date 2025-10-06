import tkinter as tk


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DemoGUI")
        self.root.geometry("800x600")

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        m_tasks = tk.Menu(menubar, tearoff=False)
        m_tasks.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="Systems", menu=m_tasks)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    App().run()