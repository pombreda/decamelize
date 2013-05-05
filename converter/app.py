import re

def convert(word):
    """Take a CamelCased word and return it as un_camel_cased
    e.g. convert(myWord) returns my_word
    """
    if word == 'True' or word == 'False':
        return word
    
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', word) 
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    
    if '_' in s2:
        return s2.lower()
    return s2


def convert_with_rules(word):
    """ Words containing a certain symbol need to handled in different ways.
    Convert_with_rules does by using a set of predefined rules dictate
    how a word will be handled.
    """

    symbols = ('=', '+', '-', ',')
    
    # these could be namespaces. Leave them alone. 
    if '.' in word: 
        return word
    
    for symbol in symbols:
        if symbol in word:
            word = convert_symbol(word, symbol)
        else:
            word = convert(word)
    return word

def convert_symbol(word, symbol):
    words = word.split(symbol)
    print(words)
    return symbol.join([convert(w) for w in words])

def convert_line(line):
    """Convert the line for the file."""
    words = line.split(' ')
    return ' '.join([convert_with_rules(word) for word in words])

#def split_file(file_handle):
#    """Break the file into a set of lines"""
#    return file_handle.split('\n')

def convert_file(filename):
    """ Given a file handle, convert the file from camel case to underscore"""
    # currently will just print out changes?
    ext = '.converted'
    with open(filename, 'r') as f:
        with open(filename + ext, 'w') as out:
            for line in f:
                out.write(convert_line(line))

