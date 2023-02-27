from time import sleep

def main():
    name = input("Please Enter name that you wanna delete : ")
    textFile = open('list.txt', 'r')
    File = textFile.read()
    arFile = File.split()
    counter = len(arFile)
    # print(arFile)

    Found = False

    for this_name_c in range(counter):
        # print(arFile[this_name_c], end=' ')
        if arFile[this_name_c] == name:
            print(name ,"\n found! ill delete it ...\n and this is new list : ")
            arFile.remove(name)
            print(arFile)
            Found=True
            break

    if not Found:
        print(name ," not found!! ")
    textFile.close()

    print("Saving new file ...")
    newFile = open("NewList.txt", 'w')
    sleep(0.2)
    for i in arFile:
        print(">>>", i ,"\tadded to new file")
        newFile.write(i)
        newFile.write("\n")
        sleep(0.4)
    newFile.close()
    sleep(0.2)
    newFile = open('NewList.txt','r')
    print("\nyour new file saved! \nthis is the result : \n ")
    print(newFile.read())
main()
