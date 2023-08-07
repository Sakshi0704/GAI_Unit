

str1 = "PyNaTive"

lowerStr = ""
upperStr = ""

for item in str1:
     if(item.islower()):
          lowerStr+=item
     else:
        upperStr+=item

print(lowerStr+upperStr)
            