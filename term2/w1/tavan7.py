def pow(x,n):
    if n == 0 :
        return 1
    else :
        return  x * pow(x, n-1)
    
def main():
    x=5
    y=3
    print(pow(x, y))

main()