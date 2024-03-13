scelta=-1
while(scelta != 0):
    print("0. Esci")
    print("1. Perimetro quadrato")
    print("2. Perimetro rettangolo")
    print("3. Circonferenza cerchio")
    scelta=int(input("Che operazione vuoi eseguire: "))

    if(scelta == 0):
        print("Soddisfatto ?\nSpero di si :)")
        pass
    elif(scelta == 1):
        x = int(input("Inserisci un lato del quadrato per calcolare il perimetro: "))
        print("Il perimetro del quadreato è:", x*4)
    elif(scelta == 2):
        x = int(input("Inserisci l'altezza del rettangolo: "))
        y = int(input("Inserisci la base del rettangolo: "))
        print("Il perimetro del rettangolo è: ", x*2 + y*2)
    elif(scelta == 3):
        x = int(input("Inserisci raggio del cerchio: "))
        print("La circonfernza del cerchio è:", 2*3.14*x)
    else:
        print("Operazione sconosciuta")
