import tkinter as tk
import tkinter.messagebox as msg

top=tk.Tk()
CheckVar1 = tk.StringVar()
C = tk.Checkbutton(top, text="Penceten Nek Wedok", variable=CheckVar1,
                onvalue="Mbak ", offvalue="Mas ",height=5)
C.pack()

L1 = tk.Label(top, text="Jenengmu Sopo?")
L1.pack()
E1 = tk.Entry(top, bd=9)
E1.pack()

def helloCallBack(): 
    msg.showinfo( "Sinau GUI", "Sugeng Rawuh, "
                 + CheckVar1.get() + E1.get()) 
w1=tk.Button(top, text="Opo Ikih?", command=helloCallBack)
w1.pack()
top.mainloop() 
