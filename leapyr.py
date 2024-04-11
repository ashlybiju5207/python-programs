n=int(input('Enter the year:'))
if n%100==0 and n%400==0:
    print('This is a leap year')
elif n%4==0 and n%100!=0:
        print('This is  a leap year')
else:
      print('This is not a leap year')
