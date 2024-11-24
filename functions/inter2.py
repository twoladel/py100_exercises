def extract_language(locale):
    return locale.split('_')[0]


def extract_region(locale):
    region_index = (locale.find('_')) + 1
    return locale[region_index:region_index + 2]


def greet(code):
    match code:
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'
        

def local_greet(locale):
    lang_code = extract_language(locale)
    region = extract_region(locale)
    
    if lang_code == 'en':
        match region:
            case 'US':
                return 'Hey!'
            case 'GB':
                return 'Hello!'
            case 'AU':
                return 'Howdy!'

    return greet(lang_code)


print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!