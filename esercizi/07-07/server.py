import socket, platform, os, string

SRV_ADDR = "192.168.50.105"
SVR_PORT = 5050
#socket.socket( inet ,tecnologia ->tcp)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SVR_PORT))

s.listen(1)

print("waiting for connection to "+ str(SRV_ADDR)+":"+ str(SVR_PORT) +"...")
connection, address = s.accept()

print ("client connected: ", address)

print("waiting for data...")
while 1:
    try:
        #buffer di 1024B 
        data = connction.recv(1024)

    except: continue

    a = data.decode('utf-8')
    stringa = a.split(sep="\n")

    #se client invia 1, il server fornisce i dati della macchina
    if(stringa[0] == '1'):
        tosend = platform.platform() + " " + platform.machine()
        #invio delle info
        connction.sendall(tosend.encode())
    #se client invia 2, il server fornisce i file in una determinata directory
    elif(stringa[0] == '2'):
        #necessito del nome della cartella per mostrare il contenuto
        try:
            data = connction.recv(1024)
        except:
            print ("Errore inserimento")
        try:
            ##decodifico l'imput e lo mando
            filelist = os.listdir(data.decode('utf-8'))
            tosend = ""
            for x in filelist:
                tosend += ", " + x
        except:
            tosend = "Wrong path"
        connction.sendall(tosend.encode())
    #option 3 starts data flow / ddos attack
    elif(stringa == '3'):
        packet = 0
        while 1:
            packet += 1
            data = connction.recv(1024)
            print("data nr " + packet + "recieved")
            if data.decode('utf-8') == '#': break
    #chiudo la connessione se invio 0
    elif(stringa == '0'):
        connection.close()
        #lo script si rimette in ascolto per la prossima chimata
        connection , address =  s.accept()
    else:
        print ("Errore di connessione")
