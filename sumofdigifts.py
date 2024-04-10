n=int(input('Entert the no:'))
sum=0
while(n!=0):
    d=n%10
    sum= sum+d
    n=n//10
print('The  sum of digits is {}'.format(sum))


 