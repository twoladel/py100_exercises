weather = (input('How\'s the weather today? '))

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrealla.")
    case 'snowy':
        print("Grab the sleds!")
    case 'windy':
        print("Let's stay inside.")
    case _:
        print("A walk might be nice.")
