from PyDictionary import PyDictionary
import warnings
from tkinter import *
from tkinter import messagebox
top = Tk()
warnings.filterwarnings("ignore")
r=0
def getdata(word):
    global r
    if r>0:
        OutputBox.delete('0.0',END)
    r=r+1
    word=word.get()
    dictionary=PyDictionary()
    try:
        OutputBox.insert(END, dictionary.meaning(word))
    except:
        msg = messagebox.showinfo( "Check Spelling Again")
    

word=StringVar()
content = Entry(top, textvariable = word,font=('calibre',10,'normal'))
content.place(x = 10,y = 50)
B = Button(top, text = "Enter", command= lambda: getdata(word))
B.place(x = 50,y = 100)
OutputBox = Text(top, width = 100, height = 10, wrap = WORD, background = "orange")
OutputBox.place(x = 20,y = 150)
top.mainloop()
