def is_empty(string):
    if string:
        return False
    return True

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

# above was first solution idea, including pythonic solution shared by LS
def is_empty(string):
    return not string

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True