
###.......... W A K D Tharuk ..........

##...... Initializing variables ..........

ans1="no"
ans2=""
ans3=""
option=0
num_count=0
highest=0
lowest=0
total=0
avg=0
L=[]
T=[]

#...... Output (Display Text Area) ..........

print("\n\t\t\t\tWONDER CALCULATOR")
print("\t\t\t\t=================")
print("\n\t\t\t\t   Main Menu")
print("\n\t\t\t1. Enter Positive integer numbers\n\t\t\t2. Display Highest value\n\t\t\t3. Display Lowest value\n\t\t\t4. Display Average value\n\t\t\t5. Display even numbers\n\n\t\t\t6.Exit")
print("\nNote:- \nFirst you have to select 'option 1' and enter the numbers")

##.......... Process ..........

#...... Repetition part (While...loop) ..........

while ans1=="no":
    option=int(input("\nPlease indicate your option : "))
    
    #...... Option 1 (Enter positive integer numbers) ..........
    if option==1:
        #...... Assigning num_count how many numbers to input ..........
        num_count=int(input("\nHow many numbers do you want to input? : "))        

        #...... Check num_count <=10 ..........
        if num_count>0 and num_count<=10:
            print("\n..... Enter the numbers one by one (You must enter positive integers) .....")

            #...... Input positive integer numbers ..........
            x=0
            L=[]
            while x<num_count:
                num=int(input("\nEnter a number : "))
                if num>0:
                    #...... Display number count ..........
                    print("[",x+1,"/",num_count,"]")
                    #...... Append input numbers into the list(list as L) ..........
                    L.append(num)
                    x=x+1    
                else:
                    print("\n...Error: Invalid input [..Positive integer numbers are allowed..]...")
                    
            #...... Asking the user whether or not they want to proceed with another option ..........        
            print("\nDo you want to continue with the calculation options in the menu above? (yes / no)")
            ans2=input()
            if ans2=="no":
                print("\nDo you want to try another list of numbers? (yes / no) ")
                ans3=input()
                if ans3=="yes":
                    print("\n..... Select 'option 1' .....")
                    continue
                else:
                    print("\nDo you want to continue with this list of numbers? (yes / no) ")
                    ans2=input()
                    if ans2=="no":
                        print("\n..... Then Select 'option 6' .....")
                
            
        else:
            print("\n...Error: You can enter a maximum of 10 numbers and You can only enter positive integer number... ")
            print("\n..... Select 'option 1' .....")
    
    elif option==6:
        print("\nAre you sure want to exit? (yes / no)")
        ans1=input()
        continue
    else:
        print("...Note: First, You need to input numbers from 'Option 1'...")
        continue

    
    while ans2=="yes":
        option=int(input("\nPlease indicate your option : "))

        #...... Option 1 (Enter positive integer numbers) ..........
        if option==1:
            print("\nDo you want to try another list of numbers? (yes / no) ")
            ans3=input()
            if ans3=="yes":
                print("\n..... Select 'option 1' .....")
                break


        #...... Option 2 (Display highest value) ..........    
        elif option==2:
            highest=L[0]
            for x in L:
                if x>highest:
                    highest=x
            print("Highest value : ",highest)
        

        #...... Option 3 (Display lowest value) ..........
        elif option==3:
            lowest=L[0]
            for x in L:
                if x<lowest:
                    lowest=x
            print("Lowest value : ",lowest)


        #...... Option 4 (Display average value) ..........
        elif option==4:
            total=0
            for x in L:
                total=total+x
            avg=total/num_count    
            print("Average value : ",format(avg,".2f"))


        #...... Option 5 (Display even numbers) ..........
        elif option==5:
            T=[]
            print("Even numbers :-")
            for x in L:
                if x%2==0:
                    T.append(x)
            T.sort()            
            print(T)

        #...... Option 6 (Exit) ..........
        elif option==6:
            print("\nAre you sure want to exit? (yes / no)")
            ans1=input()
            if ans1=="no":
                print("\nDo you want to try another list of numbers? (yes / no) ")
                ans3=input()
                if ans3=="yes":
                    print("\n..... Select 'option 1' .....")
                    break
            else:
                break
                
                
        else:
            print("\n...Error: Invalid option [This option is not valid]...")

        
#.......... End of the Repetition part ..........
        
##.......... Output ..........
print("\n\t*** Thank You For Using The Calculator Software ***")


#.......... End of the Program ..........
