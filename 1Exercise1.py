N = int(input("Your number: "))
sum = 0
sum1 = 0
count = 0
for i in range(1,N+1):
    if(i % 2) != 0:
        sum=sum + i
    else:
        count = count + 1
        sum1=sum1 + i

sum1=sum1/count 
print ('The sum of odd numbers: ', sum)
print ('The average of even numbers:', sum1)