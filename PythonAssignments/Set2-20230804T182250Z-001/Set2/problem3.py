s1="Ault"
s2="Kelly"

count=(len(s1)/2)
str=""
for i in s1:
    if(count==0):
        break
    str=str+i
    count-=1

str+=s2

count=0
for i in s1:
    if count<(len(s1)/2):
        count+=1
    else:
        str=str+i
        count+=1

print(str)
     