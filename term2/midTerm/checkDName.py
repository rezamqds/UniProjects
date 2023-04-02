def chkname():
    isTr = "mew"
    while isTr != "y":
        newDrug = input("--->Enter the new Drugs name: ")
        if not newDrug[0].isupper():
            newDrug = newDrug.capitalize()
    
        print("is it true ? ",newDrug)
        isTr = input(" y / n ?")
        if isTr.lower() == 'y':
            return newDrug
            sleep(1.5)
        else :
            cl3()
            print("\tyou can enter that again ...")

# chkname()