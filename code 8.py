#fibonnaci series pyhton program 

n=int(input('enter the length of fibonnacci series'))
num1=0
num2=1
next_number=0
count=1
while (count<=n):
    print(next_number,end="")
    count+=1
    num1=num2
    num2=next_number
    next_number=num1+num2