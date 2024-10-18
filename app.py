import tkinter
from tkinter import *
from tkinter import messagebox
# --------------------SETUP------------------------#
win = Tk()
win.title("Cut-Off Calculator")
win.geometry('900x500')
# --------------------TITLE------------------------#
title_name = Label(win, text="CUT OFF CALCULATOR BY PRADEEP GS", font=('times new roman', 18))
title_name.place(x=250, y=20)
# --------------------BODY------------------------#
sub_1 = tkinter.Label(win, text="Enter Your Maths Mark", font=('times new roman', 12))
sub_1.place(x=100, y=100)
sub_1_ent = Entry(win, font=('times new roman', 12))
sub_1_ent.place(x=280, y=100)

sub_2 = Label(win, text="Enter Your Physics Mark", font=('times new roman', 12))
sub_2.place(x=100, y=150)
sub_2_ent = Entry(win, font=('times new roman', 12))
sub_2_ent.place(x=280, y=150)

sub_3 = Label(win, text="Enter Your Chemistry Mark", font=('times new roman', 12))
sub_3.place(x=100, y=200)
sub_3_ent = Entry(win, font=('times new roman', 12))
sub_3_ent.place(x=280, y=200)


# --------------------CALCULATE------------------------#
def calculate():
    mat = sub_1_ent.get()
    phy = sub_2_ent.get()
    che = sub_3_ent.get()
    mat_int=int(mat)
    che_int=int(che)
    phy_int=int(phy)
    tot = mat_int + che_int / 2 + phy_int / 2
    tot_int=int(tot)
    per=tot/200
    per_int=int(per)
    messagebox.showinfo("CUT_OFF ", "YOUR CUT OFF IS : " + str(tot))
# --------------------BUTTON------------------------#
calci = tkinter.Button(win, text="CALCULATE", command=calculate,font=('arial',12))
calci.place(x=300, y=250)
mainloop()
# ---------------------END----------------------#
