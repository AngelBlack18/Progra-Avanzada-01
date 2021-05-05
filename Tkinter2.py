from tkinter import *

root= Tk()

label1= Label(root,text="Ingresa el precio del producto")

label2= Label(root,text="Ingresa tu pago")

entrada1= Entry(root)
entrada2= Entry(root)
entrada1.get()
entrada2.get()


def comando(entrada1, entrada2):
 print("hola el resultado es", entrada1-entrada2)

label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)

entrada1.grid(row=0,column=1,)
entrada2.grid(row=1,column=1)

c= Button(root,text="Ingresar",bg="green",fg="white" ,command=comando)
c.grid(columnspan=2)

root.mainloop()