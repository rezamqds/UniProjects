from time import sleep
# St = ("Do you want to beck to menu ? y/n")
# Cou = len(St)
# for this_s in range(Cou):
#     sleep(0.2)
#     print(St[this_s])


# s2 = "I am testing"
# for word in s2.split(""):
#     sleep(0.2)
#     print (word)

i=0
text="Do you want to beck to menu ? y/n"
while i < len(text):
    sleep(0.2)
    print (text[i],end="")
    i += 1