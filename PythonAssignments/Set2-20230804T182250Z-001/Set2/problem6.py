list1 = ["Hello" , "take"]
list2 = ["Dear","Sir"]

list = []


# while(i<len(list1) and j<len(list2)):
#         list.append(list1[i]+" "+list2[i])
#         i+=1
#         j+=1

for item in list1:
    for itemj in list2:
        list.append(item+" "+itemj)
    


print(list)