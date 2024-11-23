iceCreamDensity=10

while iceCreamDensity>0 :
    print('Drip...')
    iceCreamDensity-=1

print('The ice cream melted.')


# Corrected above code to PEP8 standard
ice_cream_density = 10 # snake_case, space around '=' op

while ice_cream_density > 0: # snake_case, space around '>' and none before ':'
    print('Drip...') # no violations
    ice_cream_density -= 1 # snake_case, space around augmented assignment op

print('The ice cream melted.') # no violations