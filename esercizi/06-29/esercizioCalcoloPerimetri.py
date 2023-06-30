import math
import os 

def perimetroquadrato(lato): 
    print(lato*4)
    return

def perinetrocerchio(raggio): 
    print(2*math.pi*raggio)

def perimetroRettangolo(base, altezza): 
    print(base*altezza)

def perimetrofriangolo(lato): 
    print(lato*3)

def perimetroPentagono (lato): 
    print(lato*5)

game = True
while game:
    choice = input("DL quale figura si vuole calcolare il perimetro? \n a) quadrato \n b) cerchio \n c) rettangolo \n d) triangolo equilatero \n e) pentagono  \n")

    repeat = True
    while repeat:
        lato = input("\ninserisci il valore del lato: ")
        try:
            lato = float(lato)
            repeat = False
        except: 
            print("\nreinserisci il valore, solo numeri ammessi (anche con virgola)\n")

    if choice == 'c':
        altezza = input("Intnsertsct il valore del'altezza: ")
        try:
            altezza = float(altezza)
            repeat = False
        except: 
            print("\nreinserisci il valore, solo numeri ammessi (anche con virgola)\n")

    print("Il perimetro e': ")

    match choice: 
        case 'a':
            perimetroquadrato(lato)
        case 'b':
            perimetroCerchto(lato)
        case 'c':
            perimetroRettangolo(lato, altezza)
        case 'd':
            perimetroTriangolo(lato)
        case 'e':
            perimetroPentagono(lato)
        case _:
            print("errore dt input")
    gameContinue = input("\n s per ricominciare, qualsiasi altro carattere per chiudere: ")
    game = gameContinue == 's' or gameContinue == 'S'
    os.system('cls')

input("\n\nciauuu :)")
