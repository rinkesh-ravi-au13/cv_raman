#question :- Take integer inputs from user until he/she presses q ( Ask to press q to quit after
#every integer input ). Print average and product of all numbers .

i=0
a=100
n=0
while i <= a:
    print('Enter the input')
    user_input=str(input())
    if user_input!='q':
        n=n+int(user_input)
        print('Enter to continue or q to quit')
        i=i+1
    else:
        print('You have chosen to quit')
        break
avg=n/i
print("total time the user entered the value is : %d " %i)
print("Average : %d" %avg)
print("product of all the number : %d" %n)