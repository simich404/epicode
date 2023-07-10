import socket, platform, os, string

SRV_ADDR = "192.168.50.105"
SVR_PORT = 5050
#socket.socket( inet ,tecnologia ->tcp)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((SRV_ADDR, SVR_PORT))


print("waiting for connection to "+ str(SRV_ADDR)+":"+ str(SVR_PORT) +"...")

print("waiting for data...")
pkt = 0
while 1:
    try:
        #buffer di 1024B 
        pkt += 1
        data = connection.recvfrom(1024)
        print("sended packet nr: " + str(pkt))

    except: continue
