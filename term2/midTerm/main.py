import check_ath, viewDrug, editDrug, checkDName
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
            print("\t\t!!!! Invalid input. Please enter Numbers !!!!")


        else:
            # add try except for each optins ==66== !!!!!
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
                            leave = input("Do you want to beck to menu? y[or Enter] / n ")
                            
                        print("taking to menu",end="")
                        for dot in range(3):
                            print('.')
                            sleep(0.2)

                    elif listChoose == 2:
                        cl3()
                        lizza = int(input("Do you want \n1.Add \n2.Replace \n3.Remove \n----> "))
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
                                    # it should be saved in the lists and then BREAKKKK -- checcked =00=
                                    editDrug.addList(newDrug)
                                    sleep(2.5)
                                    # pass
                                    break
                                else :
                                    cl3()
                                    print("\tyou can enter thar again ...")
                            
                            print("taking back to main menu ...")
                            sleep(1.6)

                        elif lizza == 2 :
                            # Replace ...
                            viewDrug.showList()
                            repDrugNum = int(input("\n--->Enter the number of drugs that you wanna replace: "))
                            repDrugName = checkDName.chkname()
                            editDrug.repList(repDrugName, repDrugNum)
                            print("Success!")
                            vw = input("Do you want to see new list? y/n ")
                            if vw == 'y':
                                cl3()
                                viewDrug.showList()
                                if input("back to menu? y/n ") == 'n' :
                                    print("ss uptime 2 sec")
                                    sleep(2)
                                    
                                sleep(1.5)

                        elif lizza == 3 :
                            # Remove
                            viewDrug.showList()
                            rmDrugNum = int(input("\n--->Enter the number of drugs that you wanna remove: "))
                            drugs = open('drugList.txt','r')
                            # lenD = len(drugs.readlines())
                            co = 0
                            for i in drugs:
                                co += 1
                                if co == rmDrugNum:
                                    surmnt = input()(f"Are you sure you wanna del {i}? y/n ")
                                    break
                            if surmnt == "y":
                                                        #use the def for del the val !!!
                                pass
                            else :
                                print("Taking back to main menu ...")
                                sleep(secs)
                                








                else:
                    sleep(1.5)
                    cl3()
                

            elif loginFlag == 2 :
                cl3()
                print("\t\tHello Customer what do you need?")
            else:
                cl3()
                print("\t\t!!!! Please enter list numbers! Try Again !!!!")
                
