import re

def convert(word):
    """Take a CamelCased word and return it as un_camel_cased
        e.g. convert(myWord) returns my_word
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', word)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def convert_file(filename):
    """Read the file and create a converted version with the filename 
    extension .converted"""
    # could just replace the old file. 
    new_file = filename + '.converted'

#    with(new_file, 'w') as w:
    with(filename, 'r') as f:
        for line in f:
            print(convert(line))
#                w.Write(convert(line))
    

