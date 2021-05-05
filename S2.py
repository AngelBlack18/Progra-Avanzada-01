#Perez Bojorquez 40138



def pedirEntrada(precio,pago):
 precio= int(input(),"Ingrese el precio del producto")
 pago= int(input(),"ingrese el pago")
 feria = pago - precio
 cents= feria
 return feria,cents,pago,precio

 

def cambio(Billete):
    if pago< precio or Billete <0: 
        print("Valor invalido")
    else:
        Bd= Billete // 200
        Bc= Billete % 200 // 100              
        Bv= Billete % 200 % 100 //20      
        Md = Billete %200 % 100 % 20 //10                                     
        Mc =Billete %200 % 100 % 20 % 10 // 5  
        Mdd = Billete %200 % 100 % 20 % 10 % 5 //2                              
        Mdu= Billete%200 % 100 % 20 % 10 % 5 % 2 // 1                 
        print("Su cambio es",feria,"pesos")
        print("Billetes de 200 ",Bd)
        print("Billetes de 100 ",Bc)
        print("Billetes de 20 ",Bv)
        print("Monedas de 10", Md)
        print("Monedas de 5 ",Mc)
        print("Monedas de 2 ",Mdd)
        print("Monedas de 1 ",Mdu)
   
print(cambio(feria))     



