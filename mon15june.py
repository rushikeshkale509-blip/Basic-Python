'''t=(1,1,1,1)
s=set(t)
if len(s)==1:
    print("same elements ")
else:
    print("different elements ")'''
    
    
    
'''n=int(input("enter a number of elements "))
l1=[]
for i in range(n):
    a=input("enter a elements ")
    l1.append(a)
l2=list(set(l1))
print(l2)  '''  

                    #Dictionary

'''d={'Name':'abc','emp_id':'1234','emp_sal':'30000'}
print(d)
d['Name']='Sam'
print(d)
for i in d:
    print(i)
for (i,j) in d.items():
    print(i,j)
del d['Name']
print(d)
#del d
#print(d)
d2=dict(a='one',b='two')
print(d2)
print(d2.keys())
print(d2.values())
print(d2.items())
print(d2.get('a'))
print(d2['a'])
print(d2.popitem())
print(d2.pop('a'))
print(d2)
d2['a']='two'
print(d2)
d2['a']='one'
print(d2)
d2.clear()
print(d2)'''


'''s="python is very easy. python is programming language"
d={}
l=s.split()
for i in l:
    #print(f"{i}=",l.count(i))
    d[i]=l.count(i)
print(d)'''

s="python is very easy. python is programming language"
d={}
for i in s:
    #print(f"{i}=",l.count(i))
    d[i]=s.count(i)
print(d)