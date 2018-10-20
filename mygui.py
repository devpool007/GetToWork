import tkinter
from tkinter import *
import Blocksite



def onadd():
    u=(str(e1.get()))
    Blocksite.website_list.append(u)
    z=(str(e3.get()))
    c = int(z)
    Blocksite.stime=c

    y=(str(e2.get()))
    d = int(y)
    Blocksite.etime=d
def onremove():
    v=str(e1.get())
    Blocksite.website_list.remove(v)
def view():
    print(Blocksite.website_list)
    print(Blocksite.stime)
    print(Blocksite.etime)
def starting():
    Blocksite.start()

window = tkinter.Tk()
window.configure(background="#a1dbcd")

window.title("WebsiteBlocker")


photo = tkinter.PhotoImage(file="hqdefault.ppm")
w = tkinter.Label(window, image=photo)
w.pack()


lblInst = tkinter.Label(window, text="Please Fill to continue:", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))

lblInst.pack()

l1 = tkinter.Label(window, text="URL:", fg="#383a39", bg="#a1dbcd")
e1 = tkinter.Entry(window)

l1.pack()
e1.pack()

l3 = tkinter.Label(window, text="Start Time:", fg="#383a39", bg="#a1dbcd")
e3 = tkinter.Entry(window)
l3.pack()
e3.pack()

l2 = tkinter.Label(window, text="End Time:", fg="#383a39", bg="#a1dbcd")
e2 = tkinter.Entry(window)
l2.pack()
e2.pack()


btn = tkinter.Button(window, text="Add", fg="#a1dbcd", bg="#383a39",command=onadd)
btn.config( height = 1, width = 12 )

btn.pack()
btn2 = tkinter.Button(window, text="Remove", fg="#a1dbcd", bg="#383a39",command=onremove)
btn2.config( height = 1, width = 12 )
btn2.pack()
btn3 = tkinter.Button(window, text="ViewSites", fg="#a1dbcd", bg="#383a39",command=view)
btn3.config( height = 1, width = 12 )
btn3.pack()
btn4 = tkinter.Button(window, text="Start", fg="#a1dbcd", bg="#383a39",command=starting)
btn4.config( height = 1, width = 12 )
btn4.pack()

window.mainloop()
