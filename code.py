import math

name=str(input()) #Here enter the name of the person
agent=int(input()) #Here enter count of the available agents at the moment
others=str(input()) #Here enter the all others' names 

others=others.split(" ")
others.append(name)
others.sort()

index=others.index(name)
place=index+1
line=math.ceil(place/agent)
time=line*20

print(time)
