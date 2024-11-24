def extract_language(locale):
    return locale[:2]


print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

# slice was 1st instinct, but I read ISO-639-3 is using 3 letter codes

def extract_language1(locale):
    return locale.split('_')[0]

print(extract_language1('en_US.UTF-8'))
print(extract_language1('en_GB.UTF-8'))
print(extract_language1('ko_KR.UTF-16'))
