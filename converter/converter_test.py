from .app import convert, convert_with_rules, convert_line, convert_file

# test the convert function
def test_convert():
    assert convert('myFolder') == 'my_folder'

def test_convert_with_noise():
    """convert one word in a sentance of three words"""
    assert convert_line('my folder letsChange') == 'my folder lets_change'

def test_sentance_with_rules():
    assert convert_line('judgeJudy = db.Model') == 'judge_judy = db.Model'

def test_convert_with_rules_skips():
    assert convert_with_rules('db.Model') == 'db.Model'

def test_convert_with_rules_equals():
    assert convert_with_rules('model=test') == 'model=test'

def test_convert_with_rules_kwords():
    assert convert_with_rules('model=True') == 'model=True'


#def test_long_string():
#    convert_file('test_data/data.py')
#    assert True

