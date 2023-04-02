def addList(newD):
    newD = newD+"\n"
    drugs = open('drugList.txt','r')
    #Check if drug isnt there ...
    # print("Total Drugs : ",len(drugs.readlines()))
    isThere = False
    for this_drug in drugs:
        # print(this_drug)
        if this_drug == newD:
            print(f'---{newD}is exist in the list! , you CANNOT enter it twice!')
            isThere = True
            return False
            break
    drugs.close()
    drugs = open('drugList.txt','a')
    if not isThere :

        drugs.write(newD)
        # drugs.write("\n")
        print(f"the new Drug :{newD}Saved in the list!")
        drugs.close()
        return True
        # pass
    
# newD = 'Xtasy'
# addList(newD)




def repList(name,numbr):
    numbr -= 1
    drugs = open('drugList.txt','r')
    drugsList = (drugs.read())
    drugsList = drugsList.split()
    # print(drugsList[numbr],"\n")
    drugs.close()
    # print(drugsList[numbr])

    # for d in drugsList:
    #     print(f'k - {d}')

    drugsList[numbr] = name
    # print(drugsList)
    drugs = open('drugList.txt','w')
    # drugs.write('\n'.join(drugsList))
    for this_drug in drugsList:
        # print(this_drug)
        drugs.write(this_drug)
        drugs.write("\n")
    drugs.close()

# repList("LSD",31)
    



def remList(numbr):
    numbr -= 1
    drugs = open('drugList.txt','r')
    drugsList = drugs.read()
    drugsList = drugsList.split()
    drugs.close()
    remDrug = drugsList[numbr]
    # print(remDrug)
    drugs = open('drugList.txt','w')
    for this_drug in drugsList:
        if remDrug != this_drug :
            drugs.write(this_drug)
            drugs.write("\n")
    drugs.close()

# remList(31)

"""
def delLIst(numorname)
use this for rm or del the drug
"""


def buyDrug(numbr,tedad):
    numbr -= 1
    drugsEntit = open('drugEntity.txt').read()
    drugsEntit = drugsEntit.split()
    drugs = open('drugList.txt','r')
    drugsList = (drugs.read())
    drugsList = drugsList.split()

    print(drugsList[numbr])
    x=0
    for this_drugEntit in drugsEntit:
        if x == numbr:
            # print(this_drugEntit)
            if int(this_drugEntit) < tedad :
                print(f"There is not enough drug for u... Come back here next week!")
                if int(this_drugEntit) > 0 :
                    newDEntit = input(f"we just have {this_drugEntit} of this, do you want it? y/n --> ")
                    if newDEntit == "y":
                        print("okay")
                        tedad = this_drugEntit
                        #kam kardan tedad
                        tedadNahaei = int(this_drugEntit)-int(tedad)
                        # print(tedadNahaei)
                        drugsEntit[x] = str(tedadNahaei)
                        print("finished")
                    else :
                        print("goodbye!")
            else:
                tedadNahaei = int(this_drugEntit)-int(tedad)
                # print(tedadNahaei)
                drugsEntit[x] = str(tedadNahaei)
                print("finished")

        x += 1

    # print(drugsEntit) checked worked correctly
    drugs.close()
    newDE = open('drugEntity.txt','w')
    for i in drugsEntit:
        newDE.write(i)
        # print(i)
        newDE.write("\n")
    newDE.close()

# buyDrug(31, 14)


def EditEntityCount(numbr,newTedad):
    numbr -= 1
    drugsEntit = open('drugEntity.txt').read().split()
    drugs = open('drugList.txt','r').read().split()
    print(f"{drugs[numbr]}:{drugsEntit[numbr]} changed to {drugs[numbr]}:{newTedad}")
    newDEntit = open("drugEntity.txt",'w')
    x=0
    for i in drugsEntit :
        if x == numbr:
            newDEntit.write(str(newTedad))
            newDEntit.write("\n")
        else :
            newDEntit.write(i)
            newDEntit.write("\n")
        x += 1
    newDEntit.close
# EditEntityCount(2, 788)
