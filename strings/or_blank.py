def is_empty_or_blank(s):
    return not s or s.isspace()


print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

# LS solution more pythonic than what I did above. Thought I was clever, lol.
def is_empty_or_blank(s):
    return not s.strip(' ') # Could also not pass an arg, defaults whitespace.

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
