#collatz conjecture in Python

x = int(input('enter number: '))
z = x

count= 0

list1 = []

#specify how many count iterations in the while loop below 

while count < 100:
    if (x%2==0)==True:
        x/=2
        count+=1
    elif (x%2==0)!=True:
        x= (x * 3) +1
        count +=1
    list1.append(int(x))
    
print(int(x))
print('amount in series,',z, '= ', count)
print('all numbers were: ', list1)
