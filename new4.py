'''a=128512
b=128514
print(chr(a))
print(chr(b))'''

'''a = int(input("1st number "))
b = int(input("2nd number "))
c = int(input("3rd number "))

if(a>b and a>c):
    print(a,"is bigger")
elif(b>a and b>c):
    print(b,"is bigger")
else:
    print(c,"is bigger")'''
    

'''y= int(input("enter a year  "))

if(y%4==0 and y%100!=0) or (y%400 == 0) :
    print(y,"is a leap year")
else:
    print(y,"is NOT a leap year")'''
    
    
'''p=int(input("enter a price  "))

if p>5000 and p<10000:
    print("discount 5%","Final Price ", p-(p*5/100))
elif p>=10000 and p<=50000:
    print("discount 5%","Final Price ", p-(p*10/100))
elif p>=50000:
    print("discount 5%","Final Price ", p-(p*20/100))
else:
    print(" No Discount ","final price", p)'''
    
 
'''current = int(input("enter a current reading  "))
last = int(input("enter a last reading  "))

u=current - last


if u>0 and u<100 and current>last:
    print("current reading ",current)
    print("last reading ",last)
    print("units ",u)
    print("bill is ",u*2)
elif u>=100 and u<250 and current>last:
    print("current reading ",current)
    print("last reading ",last)
    print("units ",u)
    print("bill is ",u*4)
elif current>last:
    print("current reading ",current)
    print("last reading ",last)
    print("units ",u)
    print("bill is ",u*6)
else:
    print("last reading is greater than current reading !!!")'''
   

f = input("festival sell is on/off  ")
m = input("you have membership yes/no")   
c = int(input("enter a cart value  "))

if f==on:
    if m==yes:
        print("discount is 30%", c*30/100)
    else:
        print("discount is 20%", c*20/100)
else :
   if f==off and m==yes: 
       if c>5000:
           print("discount is 20%", c*20/100)
       else :
           print("discount is 20%", c*20/100)
   else:
       print("No Discount !!! ")
 
        

        
    

