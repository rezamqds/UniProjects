from time import sleep

def showList():
    drugs = open('drugList.txt','r')
    dCount = 1
    for this_drug in drugs:
        sleep(0.18)
        if dCount < 10 :
            print(dCount,"  •",this_drug,end="")
        else:    
            print(dCount," •",this_drug,end="")
        dCount +=1
