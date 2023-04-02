from time import sleep

def showList(prv):
    drugs = open('drugList.txt','r')
    dCount = 1
    if prv:
        drugsEntit = open('drugEntity.txt').read()
        drugsEntit = drugsEntit.split()
        x=0
        # print(drugsEntit)
        for this_drug in drugs:
            sleep(0.5)
            if dCount < 10 :
                print(dCount,"  •",this_drug,"\t↳ Count : ",drugsEntit[x])
            else:    
                print(dCount," •",this_drug,"\t↳ Count : ",drugsEntit[x])
            dCount += 1
            x += 1
    else:
        for this_drug in drugs:
            sleep(0.18)
            if dCount < 10 :
                print(dCount,"  •",this_drug,end="")
            else:    
                print(dCount," •",this_drug,end="")
            dCount += 1



# showList(True)
