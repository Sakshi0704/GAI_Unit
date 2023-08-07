# user_input = input("Enter something :  ")

# print("You entered : ",user_input)


print("Enter n numerber to get fibonnaci numbers : ")
n = int(input())
a = 1
b = 0
list = []
while(n>0):
    list.append(b)
    c = a+b
    a =  b
    b = c
    n-=1

print(list)

# # 0 1 1 2 3
# a = 1
# b = 0
# c = a+b=1

# 0 
# a = b = 0
# b = c = 1

# c = 0+1 = 1

# 0 1 
# a = b = 1
# b = c = 1


