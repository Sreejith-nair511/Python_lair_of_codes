#multi varibale console 

number=int(input('enter the number'))#number defining
temp=number#temperoray number setup 
my_list=[]#list formation 

while temp!=0:
    my_list.append(temp%10)
    temp=temp//10

freq={}
for item in my_list:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1
    for key,value in freq.items():
        print(f'digit{key}occurs {value}times')



