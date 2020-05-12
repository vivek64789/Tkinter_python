#pip install pyshorteners

import pyshorteners
from tkinter import *
from tkinter import messagebox

def url_short():
    c=e1.get()
    s = pyshorteners.Shortener()
    su=s.tinyurl.short(c)
    e2.insert(0,su)

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    
root=Tk()
root.geometry('300x120') 
root.iconbitmap('yt.ico')
root.wm_title('URL Shortener')
l1=Label(root,text="Enter Link Here")
l1.pack(side=TOP)
e1=Entry(root, width=40)
e1.pack(side=TOP)
l2=Label(root,text="Get Short Link Here")
l2.pack(side=TOP)
e2=Entry(root, width=40)
e2.pack(side=TOP)
b1=Button(root,text="Generate",fg='red',command=url_short)
b1.pack(side=BOTTOM)

b2=Button(root,text="Clear",fg='red',command=clear)
b2.pack(side=BOTTOM)
root.mainloop()
