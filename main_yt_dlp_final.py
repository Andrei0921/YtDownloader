from email.mime import audio

from pytube import YouTube
from tkinter import *
from tkinter import messagebox,filedialog
import tkinter as tk
from yt_dlp import YoutubeDL
from urllib.request import urlopen,Request
import customtkinter as ctk

def Widgets():
    head_label=ctk.CTkLabel(root,text="YouTube Video Downloader")
    head_label.grid(row=1,column=1,pady=10,padx=10)
    link_label=ctk.CTkLabel(root,text="Youtube url:")
    link_label.grid(row=2,column=0,pady=10,padx=10)
    root.link_text=ctk.CTkEntry(root,textvariable=url,width=200)
    root.link_text.grid(row=2,column=1, pady=10,padx=10)

    root.destinationText=ctk.CTkEntry(root,textvariable=path,width=200)
    root.destinationText.grid(row=3,column=1,pady=10,padx=10)
    browse_B = ctk.CTkButton(root,
                             text="Alege folder",
                             command=Browse,
                             width=10,
                             )
    browse_B.grid(row=3,
                  column=2,
                  pady=10,
                  padx=10
                  )
    method_label=ctk.CTkLabel(root,text="Alege metoda de download (default audio-video)")
    method_label.grid(row=4,column=1,pady=10,padx=10)

    radio_B1=ctk.CTkRadioButton(root,text="Audio-video",value='audio-video',variable=radio_var,
                                radiobutton_width=20,
                                radiobutton_height=20,
                                corner_radius=1,
                                border_width_unchecked = 2,
                                border_width_checked=5,
                                border_color="red",
                                hover_color="pink",
                                fg_color="green",
                                hover=True,
                                text_color="red",
                                font=("Helvetica", 12),
                                state="normal",
                                text_color_disabled="green"
                                )
    radio_B1.grid(row=5,column=0,columnspan=2,pady=5,padx=5)
    radio_B2=ctk.CTkRadioButton(root,text="Audio",value='audio',variable=radio_var,
                                radiobutton_width=20,
                                radiobutton_height=20,
                                corner_radius=1,
                                border_width_unchecked = 2,
                                border_width_checked=5,
                                border_color="red",
                                hover_color="pink",
                                fg_color="green",
                                hover=True,
                                text_color="red",
                                font=("Helvetica", 12),
                                state="normal",
                                text_color_disabled="green"
                                )
    radio_B2.grid(row=5,column=1,columnspan=2,pady=5,padx=5)
    Download_B =ctk.CTkButton(root,
                              text="Download Video",
                              command=StartDownload,
                              width=20,
                              )
    Download_B.grid(row=6,
                    column=1,
                    pady=10,
                    padx=10)

def Browse():
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")

    path.set(download_Directory)

def get_rad():
    return radio_var.get()

def StartDownload_video():
    video_link=url.get()
    download_folder=path.get()
    if not video_link:
        messagebox.showerror("Eroare", "Introduceti link-ul de la videoclip")
        return
    if not download_folder:
        messagebox.showerror("Eroare", "Selectati folder-ul in care descarcati")
        return
    try:
        ydl_opts={'outtmpl': f'{download_folder}/%(title)s.%(ext)s'}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_link])
            messagebox.showinfo("Terminat", "Descarcat cu succes")
            root.link_text.delete(0, END)
            root.destinationText.delete(0, END)
    except Exception as e:
        messagebox.showerror("Eroare", f"A aparut o eroare: {e}")
        root.link_text.delete(0, END)
        root.destinationText.delete(0, END)

def StartDownload_audio():
    video_link=url.get()
    download_folder=path.get()
    if not video_link:
        messagebox.showerror("Eroare", "Introduceti link-ul de la videoclip")
        return
    if not download_folder:
        messagebox.showerror("Eroare", "Selectati folder-ul in care descarcati")
        return
    try:
        ydl_opts={'extract_audio':True , 'format':'bestaudio','outtmpl': f'{download_folder}/%(title)s.mp3'}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_link])
            messagebox.showinfo("Terminat", "Descarcat cu succes")
            root.link_text.delete(0, END)
            root.destinationText.delete(0, END)
    except Exception as e:
        messagebox.showerror("Eroare", f"A aparut o eroare: {e}")
        root.link_text.delete(0, END)
        root.destinationText.delete(0, END)

def StartDownload():
    if get_rad()=='audio':
        StartDownload_audio()
    elif get_rad()=='audio-video':
        StartDownload_video()
    else:
        StartDownload_video()


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
root = ctk.CTk()
root.geometry('500x400')
root.title('YouTube Downloader')
root.resizable(True, True)



url=StringVar()
path=StringVar()
radio_var=StringVar(value='default')
Widgets()
root.mainloop()