import check_ath, viewDrug, editDrug, checkDName
from os import system as littleSkiny
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
            print("\n\t\t!!!! Invalid input. Please enter Numbers !!!!\n")


        else:
            # add try except for each optins ==00== checked/
            if loginFlag == 1 :
                cl3()
                print("\t\tHello manager!")
                UID = input("\tPlease Enter Your ID : ")
                chk = check_ath.checkAth(UID)

                # cond for debug :
                # chk = True
                # end dg
                errShown = False

                while chk:
                    sleep(1)
                    cl3()
                    print(" Choose Admin list :")
                    sleep(0.2)
                    print("1. view drugs\n2. edit drugs\n3. ExitAdmin")  #if freetime: option for change admin pass
                    try :
                        listChoose = int(input("----> "))
                    except ValueError:
                        errShown = True
                        print("\t\t!!!!Please enter Numbers !!!!")
                        sleep(1)
                        cl3()

                    # else:
                    if listChoose == 1:
                        cl3()            
                        print("Drugs list : ")
                        sleep(0.5)
                        viewDrug.showList(True)
                        leave = input("Do you want to beck to menu ? y/n ")
                        # ==00== condition in while stay or leave --  if leave nothing it takes back to menu, if stay sleep
                        # just handle the the logic
                        while leave.lower() == 'n' :
                            print("your seassion reamining 3 sec more")
                            sleep(3)
                            leave = input("Do you want to beck to menu? y[or Enter] / n ")
                            
                        print("taking to menu",end="")
                        for dot in range(3):
                            print('.')
                            sleep(0.2)

                    elif listChoose == 2:
                        cl3()
                        lizza = int(input("\Edit drugs :\n~~~~ \n0.\BackMenu/ \n1.Add \n2.Replace \n3.Remove \n4.EditEntityCount\n~~~~ \n----> "))
                        if lizza == 1 :
                            # Add ...
                            isTrue = False
                            while isTrue != "y":
                                newDrug = input("Please Enter the name of the drug : ")
                                if not newDrug[0].isupper():
                                #     pass
                                #     # print("yes upper")
                                # else :
                                    # captalize the drug name !!
                                    newDrug = newDrug.capitalize()
                                
                                print("is it true ? ",newDrug)
                                isTrue = input(" y / n ?")
                                cl3()
                                if isTrue.lower() == 'y':
                                    # it should be saved in the lists and then BREAKKKK -- checcked =00= /
                                    editDrug.addList(newDrug)
                                    sleep(2.5)
                                    # pass
                                    break
                                else :
                                    cl3()
                                    print("\tyou can enter thar again ...")
                            
                            vw = input("Do you want to see new list? y/n ")
                            if vw == 'y':
                                cl3()
                                viewDrug.showList(True)
                                if input("back to menu? y/n ") == 'n' :
                                    print("ss uptime 2 sec")
                                    sleep(2)
                                    
                                sleep(1.5)

                            else :
                                print("Taking back to main menu ...")
                                sleep(2)

                        elif lizza == 2 :
                            # Replace ...
                            viewDrug.showList(True)
                            repDrugNum = int(input("\n--->Enter the number of drugs that you wanna replace: "))
                            repDrugName = checkDName.chkname()
                            editDrug.repList(repDrugName, repDrugNum)
                            print("Success! , Replaced!")
                            vw = input("Do you want to see new list? y/n ")
                            if vw == 'y':
                                cl3()
                                viewDrug.showList(True)
                                if input("back to menu? y/n ") == 'n' :
                                    print("ss uptime 2 sec")
                                    sleep(2)
                                    
                                sleep(1.5)

                        elif lizza == 3 :
                            # Remove
                            viewDrug.showList(True)
                            rmDrugNum = int(input("\n--->Enter the number of drugs that you wanna remove: "))
                            drugs = open('drugList.txt','r')
                            # lenD = len(drugs.readlines())
                            co = 0
                            for i in drugs:
                                co += 1
                                if co == rmDrugNum:
                                    surmnt = input(f"Are you sure you wanna del {i}? y/n ")
                                    break
                            if surmnt == "y":
                                                        #use the def for del the val !!!
                                editDrug.remList(rmDrugNum)
                                print("Success! , Removed!")
                            vw = input("Do you want to see new list? y/n ")
                            if vw == 'y':
                                cl3()
                                viewDrug.showList(True)
                                if input("back to menu? y/n ") == 'n' :
                                    print("ss uptime 2 sec")
                                    sleep(2)
                                    
                                sleep(1.5)

                            else :
                                print("Taking back to main menu ...")
                                sleep(2)
                            drugs.close()


                        elif lizza == 0 :
                            print("back to main menu ...")

                        elif lizza == 4 :
                            # EditEntityCount
                            viewDrug.showList(True)
                            try:
                                numbr = int(input("Please enter the number of drug: "))
                                newTedad = int(input("please eneter the new entitiy count: "))
                            except ValueError:
                                print("NUMBERS!")
                            else :
                                editDrug.EditEntityCount(numbr, str(newTedad))
                            sleep(2)

                        else :
                            print(f"{lizza} is not in the range ! ")
                            sleep(1)
                

                    elif listChoose == 3:
                        # 3 exitAdmin
                        print("Safly close files and logout ADMIN!")
                        sleep(1)
                        chk = False

                    elif not errShown :
                        print('choose options in list range !')
                        sleep(1)

                else:
                    sleep(1.5)
                    cl3()

            elif loginFlag == 2 :
                while True:
                    cl3()
                    print("\t\tHello Customer what do you need?")
                    print("1. view drugs\n2. buy drugs\n3. Exit")
                    try:
                        listChoose = int(input("----> "))

                    except ValueError:
                        print("     Use numbers !!!")
                        sleep(1)
                        cl3()

                    else:
                        if listChoose == 1 :
                            cl3()            
                            print("Drugs list : ")
                            sleep(0.5)
                            viewDrug.showList(False)
                            leave = input("Do you want to beck to menu ? y/n ")
                            while leave.lower() == 'n' :
                                print("your seassion reamining 3 sec more")
                                sleep(3)
                                leave = input("Do you want to beck to menu? y[or Enter] / n ")
                        elif listChoose == 2 :
                                                                            # buy drug
                                
                            print("Choose the drug num")
                            sleep(1)

                            viewDrug.showList(False)
                            try:
                                buyDrug = int(input("Drug num: "))
                            except ValueError:
                                print("enter NUMBERS!")
                                sleep(secs)
                            
                            else:

                                try:
                                    cntit = int(input('how many do you want ? '))
                                    sleep(0.2)
                                    cl3()
                                except ValueError:
                                    # cl3()
                                    print("we said how many? NUMBER is the awnser!")
                                    sleep(1)
                                else:
                                    if cntit > 5 :
                                        print('you are not allowd to pick more than 5 !')
                                        print('max=5 , now is in your cart')
                                        # kam kardan tedad daroo
                                        editDrug.buyDrug(buyDrug, 5)
                                    elif cntit < 1:
                                        print("\t\tit looks like you are not OKAY! cannot buy less than one item")
                                        print('taking back to the main menu ...')
                                        sleep(0.8)
                                        break

                                    else:
                                        # kam kardan tedad daroo                00000000
                                        editDrug.buyDrug(buyDrug, cntit)
                                        print('Here u are!\n')
                                        # sleep(1)
                                        

                                try :
                                    payWay = input("How would you pay?\n1.card\n2.cash\n--> ")
                                
                                except ValueError:
                                    print("JUST NUMBERS!")
                                
                                else:
                                    if payWay == 1:
                                        pass
                                    else :
                                        print("after epidemic you just can use your card ... ")
                                        sleep(1.5)
                                    littleSkiny("start "+"rule3char.txt")


                        elif listChoose == 3 :
                            # exit
                            cl3()
                            print("Exit ...")
                            sleep(1)
                            cl3()
                            break
                        else:
                            print("     Use the list range !!!")
                            sleep(1.6)
                            cl3()
            else:
                cl3()
                print("\n\t\t!!!! Please enter list numbers! Try Again !!!!\n")
                
