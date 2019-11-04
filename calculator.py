#make frames using classes ,while loop and reduce liines of code.
from tkinter import *
root=Tk()
root.geometry("600x500")
root.title("calc")
root.configure(background="grey")

global scval
scval=StringVar()
scval.set("")
screen=Entry(root, textvar=scval, font="lucida 40 bold") #root specify that this screen frame is inside root
screen.pack() #add param

def click(event):
    text=event.widget.cget("text")
    if  text=="=":
        if scval.get().isdigit():
            value=int(scval.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                value="error"
                print(e)
        scval.set(value)
        screen.update()
    elif text=="C":
        scval.set("")
        screen.update()
    else:
        scval.set(scval.get()+text)
        screen.update()
f=Frame(root, bg="grey")

b=Button(f, text="9", font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f, text="8", font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f, text="7", font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root, bg="grey")

b=Button(f, text="+", font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f, text="-", font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f, text="*", font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root, bg="grey")

b=Button(f, text="/", font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f, text="=", font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f, text="C", font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()






root.mainloop()