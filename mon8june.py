#WAP to check given number is palindrom or not

'''n = int(input("enter no to reverse "))
s=0
while n>0:
    d=n%10
    s=s*10+d
    n//=10
print("sum of digits ",s)
if(s==n):
    print("palindrom")
else:
    print("not palindrom")'''


#WAP to check given number is Amstrong or not

'''n = int(input("enter no "))
s=0
t=n
while n>0:
    d=n%10
    s=s+d**3
    n//=10
print("sum of digits ",s)
if(s==t):
    print("Amstrong Number")
else:
    print("Not A Amstrong")'''
	

                #for loop   
    
 #Wap to take input from user and print n natural no in desending order in for loop   
'''n = int(input("enter a number"))
for i in range (n,0,-1):
    print(i)'''
    
    
#Wap to print fabonice series in python    
    
'''n = int(input("enter a number"))
a=0
b=1
for i in range (n):
    print(a,end=" ")
    #c=a+b
    #a=b
    #b=c
    a,b=b,a+b'''

#Wap to check given no is prime or not

'''n = int(input("enter a number"))
flag=1
for i in range (2,n):
    if n%i==0:
        flag=0
        break
if flag == 1:
    print("number is  prime")
else:
    print("number is not prime")'''
    
              #OR

'''n = int(input("enter a number"))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
else:
    print("prime")'''
    
    
'''n = input("enter a name ")
for i in n:
    print(i,end="")'''


#Repeatedly asks the user to enter a non-negative integer.
#Use typecasting to convert the input to an integer.
#If the input is invalid or negative, print "Invalid input. Please enter a non-negative integer." and ask again.
#If valid, calculate and print the factorial of the number.
#After showing the factorial, ask the user if they want to calculate another factorial (yes or no).
#If the user enters "no", stop the program. If "yes", continue. 


'''a=input("you want calculate factorial yes/no ")
while a=="yes":
    n = int(input("enter a non negative number ")) 
    f=1
    if n<0:
        print("invalid input")
    else:
        for i in range(1,n+1):
            f=f*i
        print("factorial ",f)
            
    a=input("you want calculate factorial yes/no ")

print("exit")'''