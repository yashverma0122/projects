import sys
d1={}
while True:
    print('bank menu')
    print('1.open account')
    print('2.deposit money')
    print('3.withdraw money')
    print('4. display all')
    print('5.close account')
    print('6.exit')
    x=int(input('enter your choice'))
    if x==1:
        acno=int(input('enter account no'))
        l1=[]
        cname=input('enter customer name')
        actype=input('enter accont type')
        balance=int(input('enter balance'))
        l1.append(cname)
        l1.append(actype)
        l1.append(balance)
        d1[acno]=l1
    elif x ==2:
        acno=int(input('enter account no'))
        amt=int(input('enter amount to be deposited'))
        if acno in d1.keys():
            a1=d1[acno]
            a1[2]=a1[2]+amt
            d1[acno]=a1
    elif x ==3:
        pass
    elif x ==4:
        pass
    elif  x==5:
        for x in d1.keys():
            print('account no is()'.format(x))
            print('customer name is {}'.format(d1[x][0]))
            print('account type is {}'.format(d1[x][0]))
            print('account balnce  is()'.format(d1[x][0]))
            print('='*30)
    elif x==6:
         
        sys.exit(0)
   
    else:
                print('key doesnot exist')
    else:
        print('invalid choice')
            
