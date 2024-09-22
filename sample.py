from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

window=Tk()
window.geometry("650x400")
window.title("denomination calculator")
window.configure(bg="blue")

upload=Image.open("app_img.jpg")
upload=upload.resize((300,300))
img=ImageTk.PhotoImage(upload)
label=Label(window,image=img,bg="blue")
label.place(x=180,y=20)

label1=Label(text="welcome to denomination computer",fg="black",bg="white",height="5",width="40")
label1.place(x=190,y=300)

def msg():
    msgbox1=messagebox.showinfo("Alert","Do you want to calculate denomination count?")
    if msgbox1=="ok":
        topwin()

btn=Button(text="enter",command=msg,bg="yellow",fg="black")
btn.pack()

def topwin():
    top=Toplevel()
    top.configure(bg="white")
    top.geometry("500x500")
    top.title("window")


    label=Label(top,text="enter the total amount")
    entry=Entry(top)
    label1=Label(top,text="here are the number of notes")

    l1=Label(top,text="2000",bg="yellow")
    l2=Label(top,text="100",bg="yellow")
    l3=Label(top,text="100",bg="yellow")

    e1=Entry(top)
    e2=Entry(top)
    e3=Entry(top)
    def calculator():
       try:
        global amount
        amount=int(Entry.get())
        note2000=amount//2000
        amount%=2000
        note500=amount//500
        amount%=500
        note100=amount//100

        l1.delete(0,END)
        l2.delete(0,END)
        l3.delete(0,END)

        l1.insert(END,str(note2000))
        l2.insert(END,str(note500))
        l3.insert(END,str(note100))

       except ValueError:
        messagebox.showerror("Alert","please enter an valid amount")
    btn=Button(window,command=calculator,text="calculate",bg="yellow",fg="black")
    l1.place(x=180,y=300)
    l2.place(x=180,y=330)
    l3.place(x=180,y=360)

    label.place(x=230,y=300)
    label1.place(x=140,y=170)
    btn.place(x=240,y=120)
    entry.place(x=200,y=80)

    top.mainloop()

window.mainloop()