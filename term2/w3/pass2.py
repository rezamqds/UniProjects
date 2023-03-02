import getpass
from time import sleep
from os import system , name

def passGet():
    while True:
        paswort = getpass.getpass("\tenter your pass : ")

        if len(paswort) <=8 :
            print("your pass is not strong enough... pass should be 8 char!")
        
        if not isUp(paswort):
            print("your pass is not strong enough... use upper case!")

        if not isNum(paswort):
            print("your pass is not strong enough... use numbers!")

        else:
            break

        sleep(2)
        clear()


    vPASS = PassSet(paswort)
    return(vPASS)


def PassSet(pasV):
    while True:
        repass = getpass.getpass("\tenter your pass again for verify : ")
        if pasV == repass:
            print("Done")
            return(pasV)
            #SSavePPASS
            break
        clear()

        print(" the pass does not match enter that again ...\n")


def isUp(paWs):
        c=0
        for _ in paWs:
            if _.isupper():
                return True
                break
            #print(c)

def isNum(PaWs):
    c=0
    for j in PaWs:
            if j.isnumeric():
                return True
                break


def clear():
        if name == 'nt':
            system('cls')
        else:
            system('clear')