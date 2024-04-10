n=int(input('Entert the no:'))
rev=0
while(n!=0):
    d=n%10
    rev=rev*10+d
    n=n//10
print('The reversed digit is {}'.format(rev))


 