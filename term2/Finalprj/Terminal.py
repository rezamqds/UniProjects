# welcome, this code is writen in  python by @rezamqds
""" a terminal managment program with oop and try except and lots of amazing feauture"""

# Import modules and libs
import pickle, time, random, Attach, check_ath
from clsClear import clear as cl3
from time import sleep

# Welcome Screen 
print("\n",time.asctime(),Attach.busLOGO)

# class Terminal
class Terminal:
    def __init__(self,place,phoneNum,):
        self.place = place
        self.phoneNumber = phoneNum

    def show(self):
        print( self.place,self.phoneNumber)

class Passenger:
    def __init__(self,name,Lname,phoneNum):
        self.__name=name
        self.__lastName=Lname
        self.phoneNumber = phoneNum
        self.price = 0
        self.Mabda = ""
        self.Maqsad = ""
    def showPas(self):
        print(f"Passenger name is : {self.__name,self.__lastName} , phone number is: {self.phoneNumber} ")

    # Buy ticket
    def getTicket(self,Mabda,Maqsad):
        self.price = random.randint(170, 250)
        self.Mabda = Mabda
        self.Maqsad = Maqsad

    def ticketReport(self):
        if self.price != 0 :
            rep = (f"[[Passenger name is : {self.__name,self.__lastName} , phone number is: {self.phoneNumber} \nMabda is {self.Mabda} and Maqsad is {self.Maqsad}\nPaidout: {self.price} $TOOMAN$ ]]")
            ticketlist = open("ticketList.txt","a")
            ticketlist.write(time.asctime())
            ticketlist.write(rep)
            ticketlist.write("\n\n")
            ticketlist.close()
            return time.asctime() , rep
        else:
            return "you should buy a ticket first!"

           
# inheritance -- Terminal and Passenger for Manager!         
# class Manager          
class Manager(Terminal,Passenger):
 	def __init__(self,name,age,sex,place,phoneNum):
 		self.__name=name
 		self.__age=age
 		self.__sex=sex
 		Terminal.__init__(place,phoneNum)
 	def changeD(self,name,age,sex):
 		self.__name=name
 		self.__age=age
 		self.__sex=sex
 	def sodoorBelit(self,mabda,maqsad):
 		Passenger.getTicket(mabda,maqsad)
 
  


# pssss =Passenger("name", "Lname", "phoneNum00")
# pssss.showPas()
# pssss.getTicket("shiraz", "tehran")
# print(pssss.ticketReport())

# reza = Passenger("name", "Lname",55251)
# reza.getTicket("Mabda", "Maqsad")

# screen adjust 
chk = False
# while not logedIn:

while True:
    try :
        inputVal = int(input("""Use the list below (use the numbers):
1. Admin
2. Passenger
0. Exit
    ----> """))

    except ValueError:
        cl3()
        print("\n\t\t!!!! Invalid input. Please enter Numbers !!!!\n")


    else:
        # add try except for each optins ==00== checked/
        if inputVal == 1 :
            cl3()
            print("\t\tHello manager!")
            UID = input("\tPlease Enter Your ID : ")
            chk = check_ath.checkAth(UID)
            # print(chk)
            # cond debug
            #chk = True
            #end debug
            if chk:
                break

        elif inputVal == 2 :
            cl3()
            print("\t\tHello Passenger") 
            pas = True
            break
            
        elif inputVal == 0 :
            cl3()
            print("\n\tHave A Good Vacation! GoodBye!\n")
            break
        else:
            cl3()
            print("\tout of range!")

while True:
    if chk:
        # manager tab
        choose = int(input("1.terminals.detail\n2.passengers.detail\n3.tickets.detail\n4.Exit "))
        cl3()
        if choose == 1 :
            print("terminals.detail")
            print("u dont have terminal make new one ...")
            plc = input("terminal place : ")
            t1 = Terminal(plc, "021-5121")
            print("terminal created succesfully ")
            gg = input("do you want another one ? y/n ")
            if gg == 'y':
                plc = input("terminal place : ")
                t2 = Terminal(plc, "021-5121")
                cl3()
                print("terminal created succesfully")
            print("Terminal Details : ")
            if gg == 'y':
                print(t1.show(),t2.show())
            else:
                print(t1.show())

        elif choose == 2 :
            filepas = open("filepas","rb")
            p1 = pickle.load(filepas)
            filepas.close()
            p1.showPas()

        elif choose == 3 :
            ticketlist = open("ticketList.txt","r")
            a = ticketlist.read()
            print(a)
        
        elif choose == 4:
            break
        else:
            print("out of range!")



    elif pas:
        #mew
        print("BUY TICKET ...")
        name = input("pls enter ur name: ")
        Lname = input("pls enter ur Last name: ")
        ph = int(input("pls enter ur phone number: "))
        pas1=Passenger(name, Lname, ph)
        cl3()

        # save data
        # pickle.dump(pas1, passenger.txt)

        filepas = open("filepas","wb")
        pickle.dump(pas1, filepas)
        filepas.close()
        #saved in file

        print("\tYour Data successfully saved!")
        Mabda = input("Enter Mabda? ")
        Maqsad = input("Enter Maqsad? ")
        pas1.getTicket(Mabda, Maqsad)
        # save data

        fileticket = open("fileticket","wb")
        pickle.dump(pas1.getTicket(Mabda, Maqsad), fileticket)
        fileticket.close()
        #saved in file
        # cl3()


        fileticket = open("fileticket","rb")
        m = pickle.load(fileticket)
        fileticket.close()
        print(m)


        print("\tTicket successfully saved, how do you want pay it?\n1.Cash 2.Card")
        pay = input("1/2 ? ")
        rep = input("Do u want to Get report of your ticket? y/n ")
        pas1.ticketReport()
        if rep == "y":
            print(pas1.ticketReport())
        
        print("\nsee u later...")
        break
