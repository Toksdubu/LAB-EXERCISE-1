#Name:Zachary Ralf Crescel Charles DG. Nudalo
#Program description: Lab Exercise 3
#Date: December 10,2022

n=float(input("Ritcher scale number:"))
if n<5.0:
    print("Little or no damage")
elif 5.0<=n<5.5:
    print("Some damage")
elif 5.5<=n<6.5:
    print("Serious damage:walls may crack or fall")
elif 6.5<=n<7.5:
    print("Disaster: house or building may collapse")
else :
    print("Catastrophe:most buildings destroyed")