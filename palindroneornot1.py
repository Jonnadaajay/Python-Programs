a=str(input("enter a string:"))
temp=""
n=len(a)-1
while n>=0:
    temp+=a[n]
    n-=1
print(temp)    
if a==temp:
    print("palindrome")
else:
    print("not a palindrome")