def main():  
    idsch = input("Please Enter Your ID : ")
    #idsch = "reza"
    # UID ="please enter your id: "
    checkAth(idsch)

def checkAth(idsch):
    file = open('IDPASS.txt','r')
    FullFile=file.read()
    ArrayFile=FullFile.split()
    userFound=False
    WrongPass=True
    #print('Array 1l :' , ArrayFile[1] , "Array :" , ArrayFile)
    for i in range(0,6,2):
        #print("usr : ",ArrayFile[i])
        if idsch == ArrayFile[i] :
            userFound=True
            print("Hello" ,idsch , ' ',end='')
            psw = input("Please enter your pass: ")
        
            for pas in range(1,6,2):
                #print(ArrayFile[j])
                if psw == ArrayFile[pas]:
                    print("welcome",ArrayFile[i])
                    WrongPass=False
            
                   
    if not userFound:        
        print("the user not found!")    
    if WrongPass and userFound:
        print("the password is incorrect")            

    

main()
