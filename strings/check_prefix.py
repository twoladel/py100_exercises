# Use the startswith method... 
def starts_with(str1, str2):
    return str1.startswith(str2)


print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

# Maybe they wanted us not to use that method so...
def starts_with(str1, str2):
    sub_len = len(str2)
    return str2 == str1[:sub_len]

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True