import check_ath, viewDrug , editDrug
from clsClear import clear as cl3
from time import sleep

cl3()
print("\t\tHello welcome to Reza`s pharmecy ")

logedIn = False
while not logedIn:

    while True:
        try :
            loginFlag = int(input("""Use the list below (use the numbers):
    1. Admin
    2. Customer
        ----> """))
    
        except ValueError:
            cl3()
            print("\t\tInvalid input. Please enter Numbers!")


        else:
            if loginFlag == 1 :
                cl3()
                print("\t\tHello manager!")
                UID = input("\tPlease Enter Your ID : ")
                chk = check_ath.checkAth(UID)

                # cond for debug :
                chk = True
                # end dg

                while chk:
                    sleep(1)
                    cl3()
                    print(" Choose Admin list :")
                    sleep(0.2)
                    print("1. view drugs\n2. edit drugs\n3. any idea?")
                    listChoose = int(input("----> "))
                    
                    if listChoose == 1:
                        cl3()            
                        print("Drugs list : ")
                        sleep(0.5)
                        viewDrug.showList()
                        leave = input("Do you want to beck to menu ? y/n ")
                        # ==00== condition in while stay or leave --  if leave nothing it takes back to menu, if stay sleep
                        # just handle the the logic
                        while leave.lower() == 'n' :
                            print("your seassion reamining 3 sec more")
                            sleep(3)
                            leave = input("Do you want to beck to menu ? y/n ")
                           
                            print("taking to menu",end="")
                            for dot in range(3):
                                sleep(.3)
                                print('.')

                    elif listChoose == 2:
                        lizza = int(input("Do you want 1.Add 2.Replace or 3.Remove ?"))
                        if lizza == 1 :
                            isTrue = False
                            while isTrue != "y":
                                newDrug = input("Please Enter the name of the drug : ")
                                if newDrug[0].isupper():
                                    print("yes upper")
                                else :
                                    newDrug = newDrug.capitalize()
                                
                                print("is it true ? ",newDrug)
                                isTrue = input(" y / n ?")
                                if Trrrr.lower() == y:
                                    # it should be saved in the lists and then BREAKKKK -- checcked =00=
                                    editDrug.addList(newDrug)
                                    # pass
                                    break
                                else :
                                    cl3()
                                    print("you can enter them again :) ...")
                            
                            print("Saved Corectly :) ...\nBack to main menu ...")
                            sleep(0.8)

                        elif lizza == 2 :
                            # Replace ...
                            print("")


                        elif lizza == 3 :
                            # Remove
                            pass








                else:
                    sleep(1.5)
                    cl3()
                

            elif loginFlag == 2 :
                cl3()
                print("\t\tHello Customer what do you need?")
            else:
                cl3()
                print("\t\tPlease enter list numbers! Try Again")
                