# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."

n=20
i=2
flag = False
while(i<n):
    if(n%i==0):
        flag = True
        break
    i+=1

if(flag):
    print(n,"is prime")
else:
    print(n,"is not prime")