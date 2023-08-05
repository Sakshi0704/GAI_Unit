value="Hello"

count=0

for x in value:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        count+=1
    elif x=='A' or x=='E' or x=='I' or x=='O' or x=='U':
        count+=1

print(count)        