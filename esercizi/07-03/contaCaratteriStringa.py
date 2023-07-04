def contacaratteri(lista):
    numberToPrint = []
    for stringa in lista:
        numberToPrint.append(len(stringa))
    return numberToPrint

print("inserisci lista di stringhe, inserire '-' per interrompere \n")
strings = []
while 1:
    string = input("\n parola:")
    if string == '-':
        break
    strings.append(string)

print(contacaratteri(strings))