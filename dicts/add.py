car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
}

car['year'] = '2003'

# Broken Odometer piece down here
del car['mileage']


# Print color exercise
print(car['color'])

# Calculate amount of key/value pairs
print(len(car))