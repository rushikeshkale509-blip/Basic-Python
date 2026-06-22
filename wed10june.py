'''n = input("Enter a string ")
for i in n:
    print(i,end="")
print()

for i in range(len(n)):
    print(n[i],end="")
print()
    
i=0
while i<len(n):
    print(n[i],end="")
    i+=1'''
    
'''s=input("Enter A String To Check ")
a=s[::-1]
if s==a:
    print("Palindrome")
else: 
    print("Not Palindrome")'''
    
    
s1=input("enter a 1st string ")
s2=input("enter a 2nd string ")
s1=sorted(s1)
s2=sorted(s2)
if s1==s2:
    print("anagrams")
else:
    print("not anagrams")