import random, string
from string import ascii_letters, digits, punctuation

def generaPasswordFacile():
    password = ''.join(random.choice(ascii_letters + digits) for _ in range(8))
    print(password)

def generaPasswordDifficile():
    password = ''.join(random.choice(ascii_letters + digits + punctuation) for _ in range(20))
    print(password)


print("\n\npassword alfanumerica da 8 caratteri (sicurezza media) -> 1")
print("\npassword ASCII da 20 caratteri (sicurezza alta) -> 2")
while 1:
    scelta = string = input("\ninserisci il numero per generare la password: ")

    if scelta == '1' or scelta == '2':
        break
    strings.append(string)

if scelta == '1':
    generaPasswordFacile()
else:
    generaPasswordDifficile()