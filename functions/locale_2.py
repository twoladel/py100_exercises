def extract_region(locale):
    region_index = (locale.find('_')) + 1
    return locale[region_index:region_index + 2]

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR