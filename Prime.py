n=int(input('Enter the no:'))
f=0
if n==1:
    print(n,'is not a prime number')

else:
    for i in range(2,n):
        if (n%i)==0:
            f=1
            break

    if (f==1):
        print('The given no  {} is not prime '.format(n))
    else:
        print('The given no {} is  prime'.format(n))