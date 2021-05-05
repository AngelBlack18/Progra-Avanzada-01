from tkinter import *

root = Tk()



#etiqueta= Label(root,text ="pelada",bg="purple")
#etiqueta.pack()  

topFrame= Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

def comando1():
 print("Rojo")
 
def comando2():
 print("Azul")
 
def comando3():
 print("Naraja")
 
def comando4():
 print("Verde")


boton1 = Button(topFrame,text="Rojo [1]",bg="red",fg="white",command=comando1)
boton2 = Button(topFrame,text="Azul [2]",bg="blue",fg="white",command=comando2)
boton3 = Button(topFrame,text="Naranja [3]",bg="orange",fg="white",command=comando3)
boton4 = Button(topFrame,text="Verde [4]",bg="green",fg="white",command=comando4)

boton1.pack(side=LEFT)
boton2.pack(side=LEFT)
boton3.pack(side=LEFT)
boton4.pack(side=LEFT)



root.mainloop()



