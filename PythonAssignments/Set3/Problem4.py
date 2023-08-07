def is_palindrome(word):
    cleaned_word = ''.join(c.lower() for c in word if c.isalnum())
    return cleaned_word == cleaned_word[::-1]

# Test the function with the given input
input_word = "madam"
if is_palindrome(input_word):
    print(f"The word {input_word} is a palindrome.")
else:
    print(f"The word {input_word} is not a palindrome.")