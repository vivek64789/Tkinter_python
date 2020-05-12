import speedtest
from tkinter import *
from tkinter import messagebox
def down():
    st = speedtest.Speedtest()
    #print(st.download())
    sp=str(st.download())
    msg = messagebox.showinfo( "Download Speed",sp[:2]+"mbps" )
def up():
    st = speedtest.Speedtest()
    #print(st.upload())
    sp=str(st.upload())
    msg = messagebox.showinfo( "Upload Speed",sp[:2]+"mbps" )

top = Tk()
B = Button(top, text = "Download Speed", command = down)
B.place(x = 50,y = 50)
B = Button(top, text = "Upload Speed", command = up)
B.place(x = 50,y = 100)
top.mainloop()


"""
down(st)
up(st)
"""
