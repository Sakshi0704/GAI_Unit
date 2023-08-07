def longest_common_prefix(strs):
    if not strs:
        return ""
    
    shortest = min(strs, key=len)
    
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    
    return shortest



input_strings = ["flower", "flow", "flight"]
result = longest_common_prefix(input_strings)
print(result)
