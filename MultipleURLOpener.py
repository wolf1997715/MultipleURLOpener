import tkinter as tk
from tkinter import *
import webbrowser
import time


def openall():
    URLs = text.get("1.0","end-2c")
    amount = URLs.count("\n")+1
    urlList = URLs.split("\n")
    urlDict = {}
    text1.set("總共有 "+ str(amount) +" 個URL")
    count = 1
    for url in urlList:
        if(url[0:4] != "http"):
            url = "http://" + url
        urlDict.update({count:url})
        count+=1
    for i in range(1,amount+1):
        webbrowser.open_new_tab(urlDict[i])
        time.sleep(0.3)
def cleartext():
    text1.set("總共有 0 個URL")
    text.delete("1.0","end")
    
window = tk.Tk()
window.title("URL多開器")
window.geometry("400x700+50+50")

label_1 = tk.Label(window, text = "URL: ",font = ("msjh", 12))
label_1.grid(sticky = W, padx = 20, pady = 15)

frame = tk.Frame(window)
text = tk.Text(frame, height = 40 ,width = 50)
text.grid(sticky = N+S+E+W )
frame.grid(padx = 20, pady = 5)

text1 = StringVar()
text1.set("總共有 0 個URL")
label_2 = tk.Label(window, textvariable = text1,
                   font = ("msjh", 12))
label_2.grid(sticky = W, padx = 20, pady = 10)

button1 = tk.Button(window, text = "確認", command = openall, 
                   width = 10, height = 1,
                   font = ("msjh", 12))
button2 = tk.Button(window, text = "清除", command = cleartext, 
                   width = 10, height = 1,
                   font = ("msjh", 12))
button1.grid(padx = 20, pady = 0)
button2.grid(padx = 20, pady = 5)


window.mainloop()
