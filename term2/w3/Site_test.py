from time import sleep
import getpass
import pass2

def main(): 
    pass2.clear()
    print("Hello welcome to this site")
    print('Do you have an account? Y/N')
    ac=input()
    pass2.clear()
    # print(ac)
    if ac == 'y':
        while True:

        # print("yes")
            UID = input("Please Enter Your ID for login : ")
        #idsch = "reza"
        # UID ="please enter your id: "
            checkAth(UID)
            wc = input("if dont have account type 's' to signup...")
            if wc == s:
                break
            else:
                continue

    else:
        print()
        signup()
    # while True:
    #     soosk="*"*100
    #     for i in soosk:
    #         print(i)



def signup():
    pass2.clear()
    print("sign up \n")
    userFound = True

    while userFound:  
        signid = input('enter your id for signup : ')
        #check if id not exict
        cp = checkidvalid(signid)
        if cp != False:
            print("Good (",signid,") you can use this id ...")
            
            vpass = pass2.passGet()
            # print(vpass , " " , signid )
            Vlist = open('IDPASS.txt','a')
            Vlist.write(signid)
            Vlist.write("\n")
            Vlist.write(vpass)
            Vlist.write("\n")
            savingD = "Wait! Saving Data ..."
            for letter in savingD:
                print(letter)
                sleep(0.2)
            userFound = False
            # break
        else:
            print()  
            sleep(2.5)
            pass2.clear()
"""             
"""
def checkidvalid(id):
    file = open('IDPASS.txt','r')
    FullFile=file.read()
    ArrayFile=FullFile.split()
    ln = len(ArrayFile)
    for i in range(0,ln,2):
            # print("usr : ",ArrayFile[i])
            if id == ArrayFile[i] :
                print('you cannot use this id, this is taken... try another one!')
                return False

# akharin edit -- dar talash tekrar shodan user eshtebah -- ba tarif tabe ya har raveshi -- good night


def checkAth(idsch):
    crct = True
    while crct:
        file = open('IDPASS.txt','r')
        FullFile=file.read()
        ArrayFile=FullFile.split()
        userFound=False
        WrongPass=True
        #print('Array 1l :' , ArrayFile[1] , "Array :" , ArrayFile)
        countTMP = len(ArrayFile)
        for i in range(0,countTMP,2):
            #print("usr : ",ArrayFile[i])
            if idsch == ArrayFile[i] :
                userFound=True
                print("Hello" ,idsch , ' ',end='')
                psw = getpass.getpass("Please enter your pass: ")
                
                for pas in range(1,6,2):
                    #print(ArrayFile[j])
                    if psw == ArrayFile[pas]:
                        pass2.clear()
                        print("\nwelcome",ArrayFile[i])
                        sleep(2)
                        cdown=0
                        for i in range(30,0,-1):
                            cdown+=1
                            print('the app will terminate in ',i, " sec")
                            print("~"*cdown)
                            sleep(1)
                            pass2.clear()
                        input()
                        WrongPass=False
                    
                
                    
        if not userFound:        
            print("the user not found!")  
            sleep(0.2) 
            SignU=input("\n do you wanna to signup? Y/N ")
            if SignU == 'y' or 'Y':
                signup()


        if WrongPass and userFound:
            print("the password is incorrect") 

# while True:
main()
# signup()