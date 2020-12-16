import tkinter as tk
from tkinter import *
import os
import webbrowser
import time


def openall():
    URLs = text.get("1.0","end")            #take all text from textbox except 'EoF' & '\n'
    if (URLs[-1] == "\n"):                  
        URLs = URLs[:-1]
    amount = URLs.count("\n")               #count URL amount
    urlList = URLs.split("\n")              #split all text and make as a list that every element is one URL
    uniqueList = []                         #there is no repeated url in this list (with order)
    for url in urlList:
        if url == "" or url == "\n":
            continue
        elif url not in uniqueList:
            uniqueList.append(url)
    urlDict = {}                            #Dict for index:URL in order to execute in sequence
    count = 1                               #for dict to make index
    for url in uniqueList:                  #make dict to open urls
        if(url[0:4] != "http"):
            url = "http://" + url
        if(url[-1] == "." or url[-1] == "," or url[-1] == ")"):
            url = url[:-1]
        urlDict.update({count:url})
        count+=1
    for i in range(1,len(urlDict)+1):
        webbrowser.open_new_tab(urlDict[i])
        time.sleep(0.45)                     #wait browser in order to open in sequence
    text1.set("總共有 "+ str(amount) +" 個URL，共開啟 " + str(len(urlDict)) + " 個不重複分頁。")#print on gui to show amount
    logFilePath = "D:\\" + time.strftime("%Y") + "\\" + time.strftime("%Y%m%d") + "\\MultipleURLopener_log_" + time.strftime("%Y%m%d") + ".txt"
    if not os.path.isdir("D:\\" + time.strftime("%Y") + "\\" + time.strftime("%Y%m%d")):
        os.mkdir("D:\\" + time.strftime("%Y") + "\\" + time.strftime("%Y%m%d"))
    open(logFilePath, "a+").close()
    with open(logFilePath, mode = "a+", encoding="utf-8") as logfile: 
        logfile.write(time.strftime("%Y/%m/%d %H:%M:%S ") + str(len(urlDict)) + " " + str(urlDict) + "\n")

def cleartext():
    text1.set("總共有 0 個URL，共開啟 0 個不重複分頁。")
    text.delete("1.0","end")

if __name__=="__main__":
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
    text1.set("總共有 0 個URL，共開啟 0 個不重複分頁。")
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

