from time import sleep
from random import randint

#descand sorted type
def chap (n):
    sleep(1)
    print(n)
    if n >= 1:
        chap(n-1)

#random type
def randChap(n):
    sleep(1)
    print(randint(0, n))
    if n >= 1:
        randChap(n-1)


def main():
    n=10
    chap(n)
    print("\nits random type and decrease randomly ...\n\n")
    randChap(n)

main()