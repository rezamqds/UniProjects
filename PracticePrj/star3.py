s = '* '
n = ' '
i = 1
row = int(input("please choose the number of rows : "))
while row > 0:
    print(row * n,end="")
    print(i*s)
    row -= 1
    i += 1

    # like this :
 #     *
 #    * *
 #   * * *
 #  * * * *
 # * * * * *
