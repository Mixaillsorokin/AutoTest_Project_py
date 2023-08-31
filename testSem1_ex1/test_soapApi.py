from soap_api import checkText

def test_step1(correct_word, incorrect_word):
    assert correct_word in checkText(incorrect_word),"not found"
