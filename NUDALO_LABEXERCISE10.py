#Name:Zachary Ralf Crescel Charles DG. Nudalo
#Program description: Lab Exercise 10
#Date: February 17,2023


while True: 
    print("Welcome to the list of Lab Exercises")
    print("The list of the Lab Exercises:")
    print("\t1.Tree poem\n\t2.Average Calculator\n\t3.Ritcher Scale\n\t4.Grade Scale pt.1\n\t5.Grade Scale pt.2\n\t6.Grade Scale pt.3\n\t7.Program A(Left Diamond pattern)\n\t8.Program B(Right Diamond pattern)\n\t9.Program C(Butterfly Pattern)")
    def labexercise1():
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\bI\n\t\t\t\t\t\t\t\t\t\t\t\tThink\n\t\t\t\t\t\t\t\t\t\t\t\t\b\b\bThat I shall\n\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\bNever see a poem\n\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\bAs lovely as a tree,\n\t\t\t\t\t\t\t\t\t\t\t\bA tree whose hungry mouth\n\t\t\t\t\t\t\t\t\t\t\t\b\b\bIs pressed against the earth's\n\t\t\t\t\t\t\t\t\t\t\t\b\b\b\bSweet flowing breast, a tree that\n\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\bLooks at God all day, and lifts it's\n\t\t\t\t\t\t\t\t\t\tLeafy arams to pray. A tree that may in\n\t\t\t\t\t\t\t\t\t\t\bSummer wear, a nest of robin in her hair;\n\t\t\t\t\t\t\t\t\t\t\b\b\bUpon whose bosom snow has lain; who intimately\n\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\bLives with rain'\n\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\bPoems are made by\n\t\t\t\t\t\t\t\t\t\t\t\t\b\b\bFools like Me\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\bBut\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\bOnly\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b God\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\bCan\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b Make\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\bA\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\bTree\n\t\t\t\t\t\t\t\t\t\t\t\t\b\b\bJOYCE KILMER")
    def labexercise2():
        First_Grade= float(input('First Grade:'))
        Second_Grade= float(input('Second Grade:'))
        Third_Grade= float(input('Third Grade:'))
        Fourth_Grade= float(input('Fourth Grade:'))
        sum= First_Grade + Second_Grade + Third_Grade + Fourth_Grade
        ave=sum / 4
        print(ave)
    def labexercise3():
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
    def labexercise4():
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
    def labexercise5():
        while True:
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

            ask=input("\nwould you like to re enter your grade?""yes or no?:")
            if ask.lower()=="yes":
                continue
            else:
                print("\nthank you for submitting your grade.")
                print("\nHave a nice day!")
            break
    def labexercise6():
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
    def labexercise7():
        n=5
        for a in range(n):
            for b in range(a):
                print ("*",end="")
            print("")
        for a in range(n,0,-1):
            for b in range(0,a):
                print ("*",end="")
            print("")
    def labexercise8():
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
    def labexercise9():
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

    #User Pickings
    userpicks=0
    userpicks=float(input('Choose an Exercise(1-9):'))
    if userpicks==1:
        labexercise1()
    elif userpicks==2:
        labexercise2()
    elif userpicks==3:
        labexercise3()
    elif userpicks==4:
        labexercise4()
    elif userpicks==5:
        labexercise5() 
    elif userpicks==6:
        labexercise6()
    elif userpicks==7:
        labexercise7()
    elif userpicks==8:
        labexercise8()
    elif userpicks==9:
        labexercise9()
    else:
        print('wrong input')
        continue
    
    #Askings the user to try again
    ask=input("\nwould you like to try again?""yes or no?:")
    if ask.lower()=="yes":
        continue
    elif ask.lower()=="no":
        print("\nthank you for using this program.\nHave a nice day!")
        break
    else:
        print("wrong input please try again...")
        continue
    

