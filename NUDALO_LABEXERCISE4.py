#Name:Zachary Ralf Crescel Charles DG. Nudalo
#Program description: Lab Exercise 4
#Date: December 10,2022

#getting the midterm grade
print("Midterm Term Grade")
print("Class standing(70%)")
v1 = int(input('\tQuiz (over 100):'))
v2 = int(input('\tAssignment/Activity (over 100):'))
v3 = int(input('\tProject/Laboratory (over 100):'))
b1 = v1*.20
b2 = v2*.25
b3 = v3*.25
sum = b1+b2+b3
print("\tTotal Class standing score:", sum)
ME = int(input('Midterm Exam:'))
Mid = ME*.30
print("Midterm Exam Percentage: ", Mid)
MTG = round(sum+Mid, 0)
print("\nMidterm Term Grade:", MTG)
MTG_Percentage = MTG*.50
print("Midterm Term Grade Percentage:", MTG_Percentage)

#Getting the tentative final grade
print("\nTentative Final Grade")
print("Class standing(70%)")
v4 = int(input('\t''Quiz (over 100):'))
v5 = int(input('\t''Assignment/Activity (over 100):'))
v6 = int(input('\t''Project/Laboratory (over 100):'))
b4 = v4*.20
b5 = v5*.25
b6 = v6*.25
sum1 = b4+b5+b6
print("\tTotal Class standing score:", sum1)
FE = (input('Final Exam:'))
Fin = float(FE)*.30
print("Final Exam Percentage: ", Fin)
TFG = round (sum1+Fin, 0)
print("\nTentative Final Grade:", TFG)
TFG_Percentage = TFG*.50
print("Tentative Final Grade Percentage:", TFG_Percentage)

#getting the final grade 
FG= round(MTG_Percentage + TFG_Percentage, 2)
print("\nFinal grade:",FG)
if  96.5<= FG<=100:
    print("Final grade:",1.00)
elif 93.5<= FG<= 96.49:
    print("Final grade:",1.25)
elif 90.5<= FG<= 93.49:
    print("Final grade:",1.50)
elif 87.5<= FG <=90.49:
    print("Final grade:",1.75)
elif 84.5<=FG<=87.49:
    print("Final grade:",2.00)
elif 81.5<=FG<=83.49:
    print("Final grade:",2.25)
elif 78.5<=FG<=81.49:
    print("Final grade:",2.50)
elif 75.5<=FG<=78.49:
    print("Final grade:",2.75)
elif 74.5<=FG<=75.49:
    print("Final grade:",3.0)
else :
    print("Final grade:",5.00)