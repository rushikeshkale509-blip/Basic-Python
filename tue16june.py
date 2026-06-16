#function with no arguments
'''def f1():
    return 10+20,2*3
print(f1())
a,b=f1()'''

#function with arguments
'''def f1(a,b):
    return a**b
print(f1(2,3))
a=f1(2,3)
print(a)'''

#function with multiple arguments
'''def f1(*a):
    print(sum(a))
    #print(a[2])
f1(1,2,3)
f1(10,20,30,40)
f1(35)'''

#function with positional arguments
'''def f1(x,y):
    print(x,y)
f1(y=10,x=20)
f1(10,20)'''



#function with kayword arguments
'''def f1(**kargs):
    print(kargs)
    print(len(kargs))
f1(x=10,y=30,z=20)
f1(a=1,b=2)
f1(n=100)'''


#function with call by value
'''def f5(x,y):
	print(x,y)
	x=100
	y=200
	print(x,y)
f5(10,20)
x=1
y=2
print(x,y)
x+=3
print(x,y)'''


'''def f1(x,y):
    x,y=y,x

x=10
y=20
f1(x,y)
print(x,y)'''



#function with call by refrence
'''def f1(l):
    l[0]=100
    
l=[1,2,3]
f1(l)
print(l)'''


#Wap a function that accepts a number and checks
#weather it's perfect or not

'''def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        print("its a perfect number ",n)
    else:
        print("its not a perfect number ",n)
    
n=int(input("enter a number to check "))
perfect(n)'''


#Wap a program in which function accept list having
#even numbers of elements and swap elements at 
#adjustent position
'''def f1(l):
    for i in range(0,len(l),2):
        l[i],l[i+1]=l[i+1],l[i]
    print(l)
    
l=[1,2,3,4,5,6]
if(len(l)%2==0):
    f1(l)
else:
    print("list do'nt have a even number of elements ")
'''