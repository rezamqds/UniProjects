def addList(newD):
    drugs = open('drugList.txt','a')
    drugs.write(newD)
    drugs.write("\n")
    #Check if drug isnt there ...


# cond = 'y'
# while cond == 'y':
#     d = input("drug name ?")
#     addList(d)
#     cond = input("continiue? ")