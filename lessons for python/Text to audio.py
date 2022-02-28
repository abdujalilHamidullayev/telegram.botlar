from tkinter import *
oyna=Tk()
oyna.geometry("600x400")
oyna.config(bg="light blue")
oyna.resizable(0,0)
oyna.title("Text to audio")

Label(oyna,text="Matinni audioga ogirish",font='arial 25 bold',bg='light blue').pack()

name=StringVar()
Label(oyna,text="Matinni kirit:",font='arial 15 bold',bg='light blue').place(x=0,y=80)
name_entry=Entry(oyna,width=30,textvariable=name,bg='light blue').place(x=130, y=86)

def ijro_etish():
    pass
    


Button(oyna,text="ijro etish",font='arial 15 bold',bg='green',command=ijro_etish).place(x=150,y=250)

Button(oyna,text="chiqish",font='arial 15 bold',bg='red',command=chiqish).place(x=200,y=100)




