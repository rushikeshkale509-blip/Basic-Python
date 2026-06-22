                #Module#
#1
'''Wap to create a game which guess random number between
1 to 100. The user has to guess the number.
The program gives hint like to high to low unti correct
guess is made and print attempts required'''

'''import random as r
a=r.randint(1,100)
attempts=0
print("guess the number between 1 to 100 ")

while True:
    n=int(input("enter number to guess "))
    attempts+=1
    
    if n>a:
        print("NO.Enter a LOW number")
    elif n<a:
        print("NO.Enter a HIGH number")
    else:
        print("Correct.you guess a right number")
        print("Attempts Required ",attempts)
        break
'''


#2
'''Wap to create 6 digit OTP number . Accept otp from
user and valided if otp is correct then print login
successfully. Only 3 attempts to be allowed'''


'''import random
otp=random.randint(100000,999999)
print(otp)
attempts=1

while attempts<=3:
    n=int(input("enter otp,only 3 attempts allowed "))
    if n==otp:
        print("login succesfully ")
        break
    else:
        print("invalid otp")
        attempts+=1
'''

#3
'''Wap to create a secure password of a  user define
length password must contain atleast one uppercase one
lowercase latter one digit and 1 special character.
remaining characters should be selected randomly and
print final password'''

import random
import string

length=int(input("enter a password length "))
lower=random.choice(string.ascii_lowercase)
upper=random.choice(string.ascii_uppercase)
digit=random.choice(string.digits)
symbol=random.choice(string.punctuation)

password=upper+lower+digit+symbol
p=random.choice(list(password)+random.choice(string.ascii_letters,k=length-4))
print(p)