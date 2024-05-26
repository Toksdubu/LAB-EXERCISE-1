#Name:Zachary Ralf Crescel Charles DG. Nudalo
#Program description: Lab Exercise 9
#Date: January 28,2023

left=1
space=8
right=1
while left<5 or space>0 or right<5:
    print(left*"*"+space*" "+right*"*")
    left=left+1
    space=space-2
    right=right+1
    continue
while left< 0 or space<= 8 or right< 0:
    print(left*"*"+space*" "+right*"*")
    left=left-1
    space=space+2
    right=right-1