from .app import convert, convert_with_rules, convert_line

# test the convert function
def test_convert():
    """Convert should decamelcase the word"""
    assert convert('myFolder') == 'my_folder'

def test_convert_with_noise():
    """test only needs to convert one word in a sentance of three words"""
    assert convert_line('my folder letsChange') == 'my folder lets_change\n'

def test_convert_with_rules_skips():
    assert convert_with_rules('db.Model') == 'db.Model'

def test_sentance_with_rules():
    assert convert_line('judgeJudy = db.Model') == 'judge_judy = db.Model\n'


