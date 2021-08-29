import os
import platform
import tkinter as tk
from pytube import YouTube
from tkinter import ttk
from tkinter import filedialog

Folder_Name = ""

def commandSOShell():
    sistema= platform.system()

    if sistema== "Windows":
        return "clear"
    else:
        return "clear"

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if len(url)>1:
        ytdError.config(text="")
        yt = YouTube(url)

        if choice == choices[0]:
            select = yt.streams.get_highest_resolution()

        elif choice == choices[1]:
            select = yt.streams.filter(progressive=True, file_extension='mp4').first()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")


    #download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")



root = tk.Tk()
os.system(commandSOShell())
root.title("YouTube Downloader")
root.geometry("400x450") #set window
root.columnconfigure(0,weight=1)#set all content in center.

#Ytd Link Label
ytdLabel = tk.Label(root,text="Enter the URL of the Video",font=("jost",15))
ytdLabel.grid()

#Entry Box
ytdEntryVar = tk.StringVar()
ytdEntry = tk.Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error Msg
ytdError = tk.Label(root,text="Error Msg",fg="red",font=("jost",10))
ytdError.grid()

#Asking save file label
saveLabel = tk.Label(root,text="Save the Video File",font=("jost",15,"bold"))
saveLabel.grid()

#btn of save file
saveEntry = tk.Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

#Error Msg location
locationError = tk.Label(root,text="Error Msg of Path",fg="red",font=("jost",10))
locationError.grid()

#Download Quality
ytdQuality = tk.Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

#combobox
choices = ["High quality", "Low quality", "Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#donwload btn
downloadbtn = tk.Button(root,text="Donwload",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

#developer Label
developerlabel = tk.Label(root,text="Diego Martínez Sánchez",font=("jost",15))
developerlabel.grid()
root.mainloop()