import re

def convert(word):
    """Take a CamelCased word and return it as un_camel_cased
    e.g. convert(myWord) returns my_word
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', word) 
        # this is counting  my=myFolder?
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    if '_' in s2:
        return s2.lower()
    return s2

# some sort of matching system should be setup, such that you can find
# it should be a rules based approach that breaks down a word.
# if the word is something like "db.model" then it should be split on the 
# period to be ["db", ".", "model"]
# the words should be split so that only WORDs are handled not spaces

def convert_with_rules(word):
    """ Words containing a certain symbol need to handled in different ways.
        Convert_with_rules does by using a set of predefined rules dictate
        how a word will be handled.

        >>> convert_with_rules('db.model')
        'db.model'
        >>> convert_with_rules('myTest=myJudge')
        'my_test=my_judge'
    """

    symbols = ['=', '+', '-', ',']
    
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
    return symbol.join([convert(w) for w in words])

def convert_line(line):
    """Break the file into lines and convert it"""
    words = line.split(' ')
    return ' '.join([convert_with_rules(word) for word in words]) + '\n'

def split_file(file_handle):
    """Break the file into a set of lines"""
    return file_handle.split('\n')

#def convert_file(file_handle):
#    """Given an open file handle, create a new converted file and save it 
#   with the extension .converted
#    appended to the filename.
#    """
#    # could just replace the old file. 
#    new_file = filename + '.converted'
#    for line in f:
#            print(convert(line))
    

