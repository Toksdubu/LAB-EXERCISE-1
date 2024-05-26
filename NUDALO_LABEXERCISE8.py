#Name:Zachary Ralf Crescel Charles DG. Nudalo
#Program description: Lab Exercise 8
#Date: January 28,2022

n=5
for a in range(n):
    for b in range(n-a-1):
        print(' ',end='')
    for c in range(a+1):
        print('*', end='')
    print()
for a in range(n-1):
    for b in range(a+1):
        print(' ',end='')
    for c in range(n-a-1):
        print('*', end='')
    print()