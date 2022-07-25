import main


def test_create_message():
    result = main.create_message()
    assert "This message is broken" in result


def test_single_string():
    assert main.single_string is not None, "single_string variable shouldn't be a None"
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


def test_file_sizes():
    assert main.file_sizes is not None, "file_sizes variable shouldn't be a None"
    expected = [14, 55, 84, 93, 120, 344]
    assert sorted(main.file_sizes) == expected


def test_file_names():
    assert main.file_names is not None, "file_names variable shouldn't be a None"
    expected = ['HEAD', 'config', 'index', 'logs', 'objects', 'packed-refs refs']
    assert sorted(main.file_names) == expected


def test_new_first_names():
    assert main.new_first_names is not None, "new_first_names variable shouldn't be a None"
    expected = ['Jason', 'Susan', 'Rachel', 'Dean', 'Helen', 'Carmen', 'Xavier', 'Michael' ]
    assert main.new_first_names == expected


def test_last_four_names():
    assert main.last_four_names is not None, "last_four_names variable shouldn't be a None"
    expected = ['Carmen', 'Xavier', 'Carlos', 'Michael']
    assert main.last_four_names == expected


def test_get_name():
    assert main.get_name() == "John Doe"
