import main

def test_create_message():
    result = main.create_message()
    assert "This message is broken" in result

def test_single_string():
    assert "Monday" in main.single_string 
    assert "Hello students!" in main.single_string

def test_quoted_string():
    result = "Sometimes you can use a \' character to denote minutes or \" for seconds"
    assert main.quoted_string == result

def test_has_contacts():
    assert len(main.contacts) != 0, "contacts dictionary can't be empty"
    assert main.has_contacts is True

def test_numbers_string():
    assert "4" in main.numbers_string
    assert "7.3" in main.numbers_string