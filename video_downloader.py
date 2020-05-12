#pip install pytube3

from tkinter import *
import pytube
from tkinter import messagebox

def download():
    video_url = e1.get()
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.first()
    video.download("C:/Users/admin/Downloads")
    msg = messagebox.showinfo( "Info","Download Completed")
    e1.delete(0,END)

root=Tk()
root.geometry('300x80') 
root.iconbitmap('yt.ico')
root.wm_title('YouTube Downloader')
l1=Label(root,text="Enter Link Here")
l1.pack(side=TOP)
e1=Entry(root, width=40)
e1.pack(side=TOP)
b1=Button(root,text="Download",fg='red',command=download)
b1.pack(side=BOTTOM)
root.mainloop()
