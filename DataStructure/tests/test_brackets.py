from StackAndQueue.CC13 import validate_brackets


def test_valid_brackets():
    assert validate_brackets("{}") is True
    assert validate_brackets("{}(){}") is True
    assert validate_brackets("()[[Extra Characters]]") is True
    assert validate_brackets("(){}[[]]") is True
    assert validate_brackets("{}{Code}[Fellows](())") is True


def test_invalid_brackets():
    assert validate_brackets("[({}]") is False
    assert validate_brackets("(](") is False
    assert validate_brackets("{(})") is False

def test_empty_string():
    assert validate_brackets("") is True


def test_single_bracket():
    assert validate_brackets("{") is False
    assert validate_brackets("}") is False
    assert validate_brackets("[") is False
    assert validate_brackets("]") is False
    assert validate_brackets("(") is False
    assert validate_brackets(")") is False


def test_nested_brackets():
    assert validate_brackets("[{()}]") is True
    assert validate_brackets("{[()]}") is True
    assert validate_brackets("{[}]") is False
    assert validate_brackets("[{)]") is False
