'''Wap to count no of alphabets , digits, special 
symbols in given String and also calculate upper case
and lower case'''

'''s=input("Enter a string: ")
a=0
d=0
sp=0
u=0
l=0

for i in s:
    if i.isalpha():
        a+=1
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
    elif i.isdecimal():
        d+=1
    else:
        sp+=1

print("Alphabets =", a)
print("Digits =", d)
print("Special Symbols =", sp)
print("Uppercase Letters =", u)
print("Lowercase Letters =", l)'''

'''Wap a program to take two String from user.
If both strings are equal then convert into uppercase 
and replace 1st String with 2nd String.
if they are not equal then convert into lowercase and
join 1st String with 2nd string'''

'''s1=input("enter a 1st string ")
s2=input("enter a 2nd string ")

if s1==s2:
    a=s1=s2
    print(a.upper())

else:
    b=s1+s2
    print(b.lower())'''
    
    
'''l1=[1,2,3,-4,5]
l2=[1.2,3.4,5.6]
l3=[]
for i in l1:
    if i>0:
        l3.append(i)
        
print("l1 ",l1)
print("l3 ",l3)'''


'''l1=[1,2,3,-4,5]
n=int(input("enter a number "))
if n in l1:
    print("number is present in list")
else:
    print("not present in list ")'''