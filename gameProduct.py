import random

print("Hello welcome to product game :) \n")

print("you can close this by enter \"0\" \n")

while True:
	
	x = random.randint(1,10)
	y = random.randint(1,12)
	
	p= x*y
	
	print(x,"×",y," = ",end="")
	
	ans = int(input())
	
	if x*y==ans:
			print("good your awnser is correct!")
			
	else:
		print("Really!? cannot you even awnser this easy question? CA:",p)
		
		if ans == 0:
			
			print("thanks for using me , C U later")
			
			break
#by reza moghaddas