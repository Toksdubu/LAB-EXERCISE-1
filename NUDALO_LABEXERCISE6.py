#Name:Zachary Ralf Crescel Charles DG. Nudalo
#Program description: Lab Exercise 6
#Date: January 28,2022

while True:
    #getting the midterm grade
    print("Midterm Term Grade")
    print("Class standing(70%)")

    #quiz
    quizsum =0
    answer=0
    quizno=1
    aoq=int(input('\n'"how many quiz:"))

    while aoq>0: 
        print('\t''quiz',quizno)
        Input=int(input('\t'"enter your quiz: "))  
        Items=int(input('\tenter items: '))    
        quizno=quizno+1
        aoq=aoq-1
        quizsum+=Input
        answer+=Items
        continue
    quizave=quizsum/answer
    qf=quizave*100
    print('total score in quiz:',quizsum,"/",answer)
    print('total average in quiz:',qf)


    #activities
    actsum=0
    ans=0
    noofactivites=1
    aoa=int(input('\n'"how many Assignment/Activity:"))

    while aoa>0: 
        print('\t''Assignment/Activity',noofactivites)
        Input=int(input('\t''enter your Assignment/Activity: ')) 
        Items1=int(input('\tenter items: ')) 
        noofactivites=noofactivites+1
        aoa=aoa-1
        actsum+=Input
        ans+=Items1
        continue
    actave=actsum/ans
    af=actave*100
    print('total score in Assignment/Activity:',actsum,"/",ans)
    print("total average in Assignment/Activity:",af)

    #laboratory
    labsum =0
    answer2=0
    quizno2=1
    aol=int(input('\n'"how many Project/Laboratory:"))

    while aol>0: 
        print('\t''Project/Laboratory',quizno2)
        Input=int(input('\t''enter your Project/Laboratory: ')) 
        Items2=int(input('\t''enter items:'))
        quizno2=quizno2+1
        aol=aol-1
        labsum+=Input
        answer2+=Items2
        continue
    labave=labsum/answer2
    lf=labave*100
    print('total score in Project/Laboratory:',labsum,"/",answer2)
    print('total average in Project/Laboratory',lf)

    tq = qf*.20
    ta = af*.25
    tl = lf*.25
    sum = tq+ta+tl
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
    #final quiz
    quizfinalsum =0
    answer3=0
    quizno3=1
    aoqf=int(input("\nhow many quiz:"))

    while aoqf>0: 
        print('\tquiz',quizno3)
        Input=int(input('\tenter your quiz: ')) 
        Items4=int(input('\tenter items: '))
        quizno3=quizno3+1
        aoqf=aoqf-1
        quizfinalsum+=Input
        answer3+=Items4
        continue
    quizfinalave=quizfinalsum/answer3
    qf1=quizfinalave*100
    print('total score in quiz:',quizfinalsum,"/",answer3)
    print('total average in quiz:',qf1)

    #final activities
    actfinalsum=0
    answer4=0
    quizno4=1
    aoaf=int(input("\nhow many Assignment/Activity:"))

    while aoaf>0: 
        print('\tAssignment/Activity',quizno4)
        Input=int(input('\tenter your Assignment/Activity: ')) 
        Items5=int(input('\tenter items: '))
        quizno4=quizno4+1
        aoaf=aoaf-1
        actfinalsum+=Input
        answer4+=Items5
        continue
    actfinalave=actfinalsum/answer4
    af1=actfinalave*100
    print('total score in Assignment/Activity:',actfinalsum,"/",answer4)
    print('total average in Assignment/Activity:',af1)


    #final laboratory
    labfinalsum =0
    answer5=0
    quizno5=1
    aolf=int(input("\nhow many Project/Laboratory:"))

    while aolf>0: 
        print('\tProject/Laboratory',quizno5)
        Input=int(input('\tenter your Project/Laboratory: ')) 
        Items6=int(input('\tenter items: '))
        quizno5=quizno5+1
        aolf=aolf-1
        labfinalsum+=Input
        answer5+=Items6
        continue
    labfinalave=labfinalsum/answer5
    lf1=labfinalave*100
    print('total score in Project/Laboratory:',labfinalsum,"/",answer5)
    print('total average in Project/Laboratory:',lf1)

    tqf = qf1*.20
    taf = af1*.25
    tlf = lf1*.25
    sum1= tqf+taf+tlf
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

    ask=input("\nwould you like to re enter your grade?""yes or no?:")
    if ask.lower()=="yes":
        continue
    else:
        print("\nthank you for submitting your grade.")
        print("\nHave a nice day!")
    break