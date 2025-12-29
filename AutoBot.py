from tkinter import *
from textblob import *
root=Tk()
root.title("AutoBot")
root.geometry("300x300")

def send():
    send= "You: " + e.get()
    txt.insert(END,"\n"+send)

    user=e.get().lower()

    e.delete(0,END)

txt= Text(root)
txt.grid(row=1,column=1,columnspan=2)

scrollbar=Scrollbar(txt)
scrollbar.pack(side=RIGHT,fill=Y)

e=Entry(root)
e.grid(row=2,column=0)

send= Button(root,text="Send",command=send)
txt.insert(END,"\n"+ "Autocorrector connected")
root.mainloop()