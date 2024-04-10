n=int(input('Enter the no:'))
t=n
sum=0
d=0
while(n!=0):
    d=n%10
    sum=sum+d**3
    n=n//10
if sum==t:
    print('The no is armstrong')
else:
    print('The no is not armstrong')