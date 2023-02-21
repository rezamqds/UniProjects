def zarb(x,y):
    if x==0:
        return 0
    else :
        return y + zarb(x-1, y)


def main():
    x=int(input("x: "))
    y=int(input("y: "))
    print(zarb(x, y))

main()