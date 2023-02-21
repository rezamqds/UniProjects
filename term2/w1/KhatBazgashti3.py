def star(n,i):
    g=' '
    s="*"
    print(n*g,s,i*g,i*s, end="")
    print()
    if n>=1:
        star(n-1,i+1)


def main():
    x = int(input("enter number: "))
    i=0
    star(x,i)


main()