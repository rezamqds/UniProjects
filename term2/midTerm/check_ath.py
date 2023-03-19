def checkAth(idsch):
    file = open('IDPASS.txt','r')
    FullFile=file.read()
    ArrayFile=FullFile.split()

    userFound=False
    WrongPass=True
    arCount = len(ArrayFile)
    for i in range(0,arCount,2):
        # print("usr : ",ArrayFile[i])
        if idsch == ArrayFile[i] :
            userFound=True
            print("Hello" ,idsch , ' ',end='')
            psw = input("Please enter your pass: ")
        
            for pas in range(1,arCount,2):
                #print(ArrayFile[j])
                if psw == ArrayFile[pas]:
                    print("welcome",ArrayFile[i])
                    WrongPass=False
                    return True
                 
    if not userFound:        
        print("the user not found!")
        return False    
    if WrongPass and userFound:
        print("the password is incorrect")
        return False