
from tkinter import *
import tkinter as tk
from tkinter import ttk
import awesometkinter as atk
import requests
import json
from creds import URL
import time
from tkinter import scrolledtext

root = atk.tk.Tk()

content = atk.Frame3d(root)
frame = atk.Frame3d(content, relief=RIDGE, borderwidth=5)


def balanceD(frame):
    ballabel = Bar(frame, text='Balance: ', relief=RAISED)
    ballabel1 = Bar(frame, text='insert balance')
    ballabel.grid(column=0, row=0, sticky='news', padx=1, pady=0)
    ballabel1.grid(column=1, row=0, sticky='news')

def miningD(frame):
    mdiflabel = Label(frame, text='Mining Diff: ', relief=RAISED)
    mdiflabel1 = Label(frame, text="1")
    mdiflabel1.grid(column=1, row=1, sticky=E)
    mdiflabel.grid(column=0, row=1, sticky=W+E+S+N, padx=1, pady=0)

def stakingD(frame):
    sdiflabel = Label(frame, text='Staking Diff: ', relief=RAISED)
    sdiflabel1 = Label(frame, text="1")
    sdiflabel1.grid(column=1, row=2, sticky=E)
    sdiflabel.grid(column=0, row=2, sticky=W+E+S+N, padx=1, pady=0)

def addressList(frame):
    tink = open('address', 'a+')
#    address = requests.get(URL + 'address')
#    addy = address.json
    tink.write(str("111111"))



#balance = requests.get(URL + 'balance')
#bal = balance.text

namelbl = ttk.Label(content, text="SAT3COiN")
name = ttk.Entry(content)

one = atk.Button3d(content, text="One", command=lambda:[balanceD(frame)])
two = atk.Button3d(content, text="Two", command=lambda:[addylist(frame)])
three = atk.Button3d(content, text="Three", command=frame.destroy)

ok = atk.Button3d(content, text="Okay")
exit = atk.Button3d(content, text="exit", command=root.destroy)

content.grid(column=0, row=0, columnspan=3, rowspan=4, stick="w")

frame.grid(column=0, row=0, columnspan=3, rowspan=5)

namelbl.grid(column=3, row=0, columnspan=2)
name.grid(column=3, row=1, columnspan=2)

one.grid(column=0, row=5)
two.grid(column=1, row=5)
three.grid(column=2, row=5, sticky='news')

ok.grid(column=3, row=5)
addressList(frame)
balanceD(frame)
stakingD(frame)
miningD(frame)
ttk.Label(frame,
          text = "Wallet Widget",
          font = ("Times New Roman", 15),
          background = 'green',
          foreground = "white").grid(column = 0,
                                     row = 0)

# Creating scrolled text
# area widget
text_area = scrolledtext.ScrolledText(frame,
                                      wrap = tk.WORD,
                                      width = 40,
                                      height = 10,
                                      font = ("Times New Roman",
                                              18))

text_area.grid(column = 0, row=6, pady = 10, padx = 10)


exit.grid(column=8, row=7)

root.mainloop()
