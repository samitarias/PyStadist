import random
def media(X):
    return sum(X)/len(X)

def opc():
    aux=True
    while aux:
            aux=input("Desea escribir una lista o que se genere aleatoriamente? Digite 1 para aleatorio o 2 para lista de numeros \n 1. Aleatorio\n 2. Lista de numeros\n 3. Para salir\n")
            if aux =="1":
                X=[random.randint(1,21) for i in range(20)]
                mu=media(X)
                print(f'La media de {len(X)} numeros  es {mu} ')
            elif aux=="2":
                lista=[]
                limite=int(input("Digite limite de la lista: "))
                for i in range(limite):
                    numero=int(input("Digite numero: "))
                    lista.append(numero)
                    longi=media(lista)
                print("La media es:",longi)
            elif aux=="3":
                break
            elif aux !="":
                print("Debe digitar una opción")


    
if __name__=='__main__':
    opc()
