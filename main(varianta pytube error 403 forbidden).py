from pytube import YouTube
from tkinter import *
from tkinter import messagebox,filedialog
import tkinter as tk
from yt_dlp import YoutubeDL
from urllib.request import urlopen,Request
import customtkinter

def Widgets():
    head_label=Label(root,text="YouTube Video Downloader",font=("Arial",10),bg="white",fg="black")
    head_label.grid(row=1,column=1)
    link_label=Label(root,text="Youtube url:",font=("Arial",10),bg="white",fg="black")
    link_label.grid(row=2,column=0)
    root.link_text=Entry(root,font=("Arial",10),textvariable=url,width=50)
    root.link_text.grid(row=2,column=1)
    destination_label=Label(root,text="Choose a file:",font=("Arial",10),bg="white",fg="black")
    destination_label.grid(row=3,column=0)
    root.destinationText=Entry(root,font=("Arial",10),textvariable=path,width=50)
    root.destinationText.grid(row=3,column=1)
    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="bisque",
                      relief=GROOVE)
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)

    Download_B = Button(root,
                        text="Download Video",
                        command=StartDownload,
                        width=20,
                        bg="thistle1",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Georgia, 13")
    Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)





def Browse():
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")

    path.set(download_Directory)

def StartDownload():
    Youtube_link=url.get()
    folder=path.get()
    req=Request(Youtube_link,headers={'User-Agent':'Mozilla/5.0'})
    webpage=urlopen(req).read()
    getVideo=YouTube(Youtube_link)
    videoStream=getVideo.streams.first()
    videoStream.download(folder,filename="someting")
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + folder)




root = tk.Tk()
root.geometry('550x550')
root.title('YouTube Downloader')
root.resizable(False, False)
root.config(background='PaleGreen1')

url=StringVar()
path=StringVar()
Widgets()
root.mainloop()