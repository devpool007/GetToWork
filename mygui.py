import tkinter
from datetime import datetime as dt
from tkinter import *
import Blocksite



def onadd():
    u=(str(e1.get()))
    # z=(str(e3.get()))
    y=(str(e2.get()))
    # c=0
    d=0
    try:
        # c = int(z)
        d = int(y)
    except Exception as e:
        print("Please Enter The times correctly")
    # Blocksite.stime=c
    Blocksite.k = d
    if Blocksite.stime < Blocksite.etime: # only add if endtime is > current time
        if u not in Blocksite.website_list: # do not add more than once to the list
            Blocksite.website_list.append(u)
        else:
            print("Already There")
    else:
        print("Bad End Time")
def onremove():
    v=str(e1.get())
    try:                # only removing if there is a value
        Blocksite.website_list.remove(v)
        Blocksite.remover(v)
    except Exception as e:
        print("Not In Blocklist")
def view():
    print("Sites being Blocked:") # better view method
    for sites in Blocksite.website_list:
        print('\033[91m'+sites+'\033[0m')
def starting():
    Blocksite.start() # suggesting thread implementation so that last add/remove does not affect the current add/remove function
    window.after(5000, lambda: window.iconify()) # Destroy the widget after 5 seconds

window = tkinter.Tk()
window.configure(background="#a1dbcd")

window.title("WebsiteBlocker")


photo = tkinter.PhotoImage(file="hqdefault.PPM")
w = tkinter.Label(window, image=photo)
w.pack()


lblInst = tkinter.Label(window, text="Please Fill to continue:", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))

lblInst.pack()

l1 = tkinter.Label(window, text="URL:", fg="#383a39", bg="#a1dbcd")
e1 = tkinter.Entry(window)

l1.pack()
e1.pack()

# l3 = tkinter.Label(window, text="Start Time:", fg="#383a39", bg="#a1dbcd")
# e3 = tkinter.Entry(window)
# l3.pack()
# e3.pack()

l2 = tkinter.Label(window, text="No. of hours:", fg="#383a39", bg="#a1dbcd")
e2 = tkinter.Entry(window)
l2.pack()
e2.pack()

li = tkinter.Label(window, text="           ", fg="#383a39", bg="#a1dbcd")
li.pack()

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
