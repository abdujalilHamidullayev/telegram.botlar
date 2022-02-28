from tkinter import *

oyna=Tk()
oyna.geometry("600x400")
oyna.config(bg="yellow")
oyna.resizable(0,0)
oyna.title("Mening kontaktlairim")
rasm=PhotoImage(file='book.png')
oyna.iconphoto(False,rasm)

Label(oyna,text="Malumotlar",font="arial 20 italic").pack()
name=StringVar()
number=StringVar()
Label(oyna,text="ISM",font="Algerian 15 bold").place(x=10,y=70)
name_entry=Entry(oyna,width=40,textvariable=name).place(x=100,y=75)
Label(oyna,text="Tel",font="Elephant 15 ").place(x=10,y=110)

number_entry=Entry(oyna,width=40,textvariable=number).place(x=100,y=115)

Button(oyna,text="Saqlash",font="arial 15 bold",bg="red").place(x=100,y=250)
Button(oyna,text="Korish",font="arial 15 bold",bg="blue").place(x=300,y=250)
Button(oyna,text="chiqish",font="arial 15 bold",bg="green").place(x=400,y=250)
Button(oyna,text="Tozalash",font="arial 15 bold",bg="grey").place(x=290,y=350)
Button(oyna,text="O'chirish",font="arial 15 bold",bg="pink").place(x=400,y=350)
Button(oyna,text="Taxrirlash",font="arial 15 bold",bg="white").place(x=100,y=350)
    
