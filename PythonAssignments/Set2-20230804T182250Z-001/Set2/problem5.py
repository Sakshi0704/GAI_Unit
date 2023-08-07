list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]



list = []

n1 = len(list1)
n2 = len(list2)
min = 0
if(n1<n2):
    min = n1
else:
    min = n2

i = 0
while(i<min):
    list.append(list1[i]+list2[i])
    i+=1

if(n1<n2):
    for item in list2:
         list.append(item)
    
elif(n1>n2):
    for item  in list1:
         list.append(item)


print(list)