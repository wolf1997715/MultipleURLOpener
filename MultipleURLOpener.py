import tkinter as tk
from tkinter import *
import os
import webbrowser
import time


def openall():
    URLs = text.get("1.0","end")            #take all text from textbox except 'EoF' & '\n'
    if (URLs[-1] == "\n"):
        URLs = URLs[:-1]
    urlList = URLs.split("\n")              #split all text and make as a list that every element is one URL
    uniqueList = []                         #there is no repeated url in this list (with order)
    while "" in urlList:
        urlList.remove("")
    for url in urlList:
        if url == "" or url == "\n":        #skip all empty
            continue
        if chkValueMutiple.get():           #if open_repeated checked
            uniqueList.append(url)
            continue
        elif url not in uniqueList:         #if open_repeated not checked
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

    if chkValueOrder.get():
        for quickurl in uniqueList:
            webbrowser.open_new_tab(quickurl)
    else:
        for i in range(1,len(urlDict)+1):
            webbrowser.open_new_tab(urlDict[i])
            time.sleep(0.45)                #wait browser in order to open in sequence

    text1.set("總共有 "+ str(len(urlList)) +" 個URL，共開啟 " + str(len(urlDict)) + " 個分頁。")#print on gui to show amount
    logFilePath = "D:\\" + time.strftime("%Y") + "\\" + time.strftime("%Y%m%d") + "\\MultipleURLopener_log_" + time.strftime("%Y%m%d") + ".txt"
    if not os.path.isdir("D:\\" + time.strftime("%Y") + "\\" + time.strftime("%Y%m%d")):
        os.mkdir("D:\\" + time.strftime("%Y") + "\\" + time.strftime("%Y%m%d"))
    open(logFilePath, "a+").close()
    with open(logFilePath, mode = "a+", encoding="utf-8") as logfile: 
        logfile.write(time.strftime("%Y/%m/%d %H:%M:%S ") + str(len(urlDict)) + " " + str(urlDict) + "\n")

def cleartext():
    text1.set("總共有 0 個URL，共開啟 0 個分頁。")
    text.delete("1.0","end")

if __name__=="__main__":
    window = tk.Tk()
    window.title("URL多開器")
    window.geometry("400x720+50+50")
    
    label_1 = tk.Label(window, text = "URL: ",font = ("msjh", 12))
    label_1.grid(sticky = W, padx = 20, pady = 15)
    
    frame = tk.Frame(window)
    text = tk.Text(frame, height = 38 ,width = 50)
    text.grid(sticky = N+S+E+W )
    frame.grid(padx = 20, pady = 5)
    
    text1 = StringVar()
    text1.set("總共有 0 個URL，共開啟 0 個分頁。")
    label_2 = tk.Label(window, textvariable = text1,
                       font = ("msjh", 12))
    label_2.grid(sticky = W, ipadx = 20, ipady = 10)

    chkValueMutiple = tk.BooleanVar() 
    chkValueMutiple.set(True)
    checkbutton = tk.Checkbutton(window, text = "開啟重複的分頁", var = chkValueMutiple, onvalue = True, offvalue = False, font = ("msjh", 12))
    checkbutton.grid(sticky = W, padx = 20)
    
    chkValueOrder = tk.BooleanVar() 
    chkValueOrder.set(False)
    checkbutton = tk.Checkbutton(window, text = "不照順序開啟(較快)", var = chkValueOrder, onvalue = True, offvalue = False, font = ("msjh", 12))
    checkbutton.grid(sticky = W, padx = 20)

    button1 = tk.Button(window, text = "確認", command = openall, 
                       width = 10, height = 1,
                       font = ("msjh", 12))
    button2 = tk.Button(window, text = "清除", command = cleartext, 
                       width = 10, height = 1,
                       font = ("msjh", 12))
    button1.grid(sticky = W, column = 0, row = 5, padx = 20, pady = 0)
    button2.grid(sticky = W, column = 0, row = 5, padx = 150, pady = 10)
    
    window.mainloop()

