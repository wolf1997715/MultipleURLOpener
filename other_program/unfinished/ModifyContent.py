import re
import csv
import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.withdraw()

filePath = filedialog.askopenfile(initialdir = "shell:MyComputerFolder",title = "選擇CSV檔案",filetypes = (("CSV (逗號分隔)","*.csv"),("全部檔案","*.*"))).name

with open(filePath,encoding = "ANSI", newline="",mode = "w+") as csvfile:
    columns = csv.DictReader(csvfile)
    for element in columns:
        element["content"] = re.sub(r"Result_(\d+)\.csv,", " ",element["content"])
        
