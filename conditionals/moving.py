speed = 0
acceleration = 24
braking_force = 25
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

# parentheses matter because once we make braking_force more than acceleration
# the expressions don't evalutate the same
is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
print(is_moving)