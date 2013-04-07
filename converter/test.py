from .app import convert, convertFile

# test the convert function
def test_convert():
    """Convert should decamelcase the word"""
    assert convert('myFolder') == 'my_folder'

def test_no_conversion_needed():
    """pass in two words, neither of which are camelcased. Test shouldn't return a change"""
    assert convert('my folder') == 'my folder'

def test_convert_with_noise():
    """test only needs to convert one word in a sentance of three words"""
    assert convert('my folder letsChange') == 'my folder lets_change'


