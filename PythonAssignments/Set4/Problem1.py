def is_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    
    return sorted(word1) == sorted(word2)





word1 = "sakshi"
word2 = "ihskas"

result = is_anagram(word1, word2)
print(result)  









#word1 = word1.replace(" ", "").lower()