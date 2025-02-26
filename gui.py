import tkinter as tk
from tkinter import filedialog
import os
from cover import coverMigrate


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("275x110")
        self.root.title("网易云mp3封面位置转移")

        self.label_path = tk.Label(self.root, text="目录:")
        self.label_path.place(x=5, y=5, width=35, height=20)

        self.edt_path = tk.Entry(self.root)
        self.edt_path.place(x=45, y=5, width=150, height=20)

        self.btn_path = tk.Button(self.root, text="选择路径...", command=self.chooseDir)
        self.btn_path.place(x=200, y=5, width=65, height=20)

        self.check_copy_selected = tk.IntVar()
        self.check_copy = tk.Checkbutton(self.root, text="另存新文件", variable=self.check_copy_selected)
        self.check_copy.place(x=5, y=30, width=80, height=20)
        self.check_copy_selected.set(1)

        self.check_keep_selected = tk.IntVar()
        self.check_keep = tk.Checkbutton(self.root, text="保留碟片图像", variable=self.check_keep_selected)
        self.check_keep.place(x=90, y=30, width=100, height=20)
        self.check_keep_selected.set(1)

        self.label_handling = tk.Label(self.root, text="")
        self.label_handling.place(x=5, y=55, width=250, height=20)

        self.btn_exec = tk.Button(self.root, text="开始执行", command=self.execute)
        self.btn_exec.place(x=5, y=80, width=65, height=20)

        self.btn_exit = tk.Button(self.root, text="退出", command=self.exit)
        self.btn_exit.place(x=200, y=80, width=65, height=20)

    def chooseDir(self):
        directory = filedialog.askdirectory()
        print(directory)
        self.edt_path.delete(0, tk.END)
        self.edt_path.insert(0, directory)

    def mainLoop(self):
        self.root.mainloop()

    def exit(self):
        self.root.quit()

    def execute(self):
        path = self.edt_path.get()
        if path=="" or not os.path.exists(path):
            self.label_handling.config(text="目录非法，请重新选择")
            return
        coverMigrate(path,
                     save_new_file=bool(self.check_copy_selected.get()),
                     keep_disc_img=bool(self.check_keep_selected.get()),
                     label=self.label_handling
                     )
        self.label_handling.config(text="已完成")
