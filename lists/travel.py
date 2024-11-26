destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(city, lst):
    in_list = [place for place in lst if place == city]
    if in_list:
        print(True)
    else:
        print(False)
        
contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False

