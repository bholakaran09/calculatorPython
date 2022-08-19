import tkinter as tk
from tkinter import *
import time
import datetime
win=tk.Tk()
win.geometry("440x440")
win.resizable(0,0)
win.title("Calculator")

str1=""                    #main string in which calculation occur.
str2=""                    #string in which result stores
##----------------------------------------FUNCTIONS------------------------------------------------
def cal(num):
    global str1
    str1=str1+str(num)                      #assigning values to string
    screen_var.set(str1)

def evaluate(): 
    try:
        global str1
        global str2
        str2=eval(str1)
        str2=str(str2)
        screen_var.set(str2)
    except:
        del_string()
    finally:
        print("This calculator is made by Karan Bhola")


def del_string():
    global str1
    str1=str1[0:-1]                        #deletes last element
    screen_var.set(str1)


def clear_all():
    global str1
    str1=""                                 #clears all string 
    screen_var.set(str1)

def save():
    global str1
    global str2
    now=time.strftime("%H:%M:%S")            
    today=datetime.datetime.today().strftime("%d:%m:%Y")
    file=open("calculator.txt","w")         #creating file
    file.write(str1)
    file.write("=")
    file.write(str2)                        #writting str1,str2,date and time.
    file.write("\nTime=")
    file.write(now)
    file.write("\nDate=")
    file.write(today)

##-----------------------------------------BUTTONS-----------------------------------------------


screen_var=StringVar()
screen=Entry(win,font=("Times New Roman",20),bd=15,width=50,textvariable=screen_var,justify="right")
screen.pack(side=TOP)

seven= tk.Button (win,text="7",bg="white",bd=5,height=5,width=10,command=lambda:cal(7))
seven.place(x=0,y=55)

eigth= tk.Button (win,text="8",bg="white",bd=5,height=5,width=10,command=lambda:cal(8))
eigth.place(x=86,y=55)

nine= tk.Button (win,text="9",bg="white",bd=5,height=5,width=10,command=lambda:cal(9))
nine.place(x=172,y=55)

four= tk.Button (win,text="4",bg="white",bd=5,height=5,width=10,command=lambda:cal(4))
four.place(x=0,y=148)

five= tk.Button (win,text="5",bg="white",bd=5,height=5,width=10,command=lambda:cal(5))
five.place(x=86,y=148)

six= tk.Button (win,text="6",bg="white",bd=5,height=5,width=10,command=lambda:cal(6))
six.place(x=172,y=148)

one= tk.Button (win,text="1",bg="white",bd=5,height=5,width=10,command=lambda:cal(1))
one.place(x=0,y=242)

two= tk.Button (win,text="2",bg="white",bd=5,height=5,width=10,command=lambda:cal(2))
two.place(x=86,y=242)

three= tk.Button (win,text="3",bg="white",bd=5,height=5,width=10,command=lambda:cal(3))
three.place(x=172,y=242)

zero= tk.Button (win,text="0",bg="white",bd=5,height=5,width=10,command=lambda:cal(0))
zero.place(x=86,y=334)

dot= tk.Button (win,text=".",bg="white",bd=5,height=5,width=10,command=lambda:cal("."))
dot.place(x=0,y=334)

equal= tk.Button (win,text="=",bg="#0ab6f5",bd=5,height=5,width=10,command=lambda:evaluate())
equal.place(x=172,y=334)

plus= tk.Button (win,text="+",bg="white",bd=5,height=5,width=10,command=lambda:cal("+"))
plus.place(x=258,y=334)

divide= tk.Button (win,text="/",bd=5,bg="white",height=5,width=10,command=lambda:cal("/"))
divide.place(x=258,y=55)

multiply= tk.Button (win,text="*",bg="white",bd=5,height=5,width=10,command=lambda:cal("*"))
multiply.place(x=258,y=148)

minus= tk.Button (win,text="-",bg="white",bd=5,height=5,width=10,command=lambda:cal("-"))
minus.place(x=258,y=242)

delete=tk.Button(win,text="Del",bg="white",bd=5,height=5,width=10,command=lambda:del_string())
delete.place(x=345,y=55)

clear=tk.Button(win,text="AC",bg="white",bd=5,height=5,width=10,command=lambda:clear_all())
clear.place(x=345,y=148)

save_btn=tk.Button(win,text="Save",bg="white",bd=5,height=5,width=10,command=lambda:save())
save_btn.place(x=345,y=242)

exit=tk.Button(win,text="Exit",bg="white",bd=5,height=5,width=10,command=win.destroy)
exit.place(x=345,y=334)

win.mainloop()