import random
random_number = random.randint(0, 1)

if random_number == 1:
    print('Yes!')
else:
    print('No')

# course solution
if random_number: # 1 is truthy and 0 is falsy so no need for '=='
    print('Yes!')
else:
    print('No')

# Part 2 exercise - ternary
print('Yes!' if random_number else 'No')