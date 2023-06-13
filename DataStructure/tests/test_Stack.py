from StackAndQueue.Stack import Stack,Node,EmptyError
import pytest



def test_push(stack):
    stack.push("h")
    stack.push("e")
    actual=stack.__str__()
    expect="e -> h -> None"
    assert actual==expect

def test_pop(stack):
    stack.push("h")
    stack.push("e")
    stack.pop()
    actual=stack.__str__()
    expect="h -> None"
    assert actual==expect


def test_peek(stack):
    stack.push("eman")
    stack.push("Obeidat")
    actual= stack.peek()
    expect="Obeidat"
    assert actual==expect

def test_isEmpty(stack):
    stack.push("good")
    stack.push("morning")
    stack.pop()
    actual=stack.is_empty()
    expect=False
    assert actual==expect

def test_str(stack):
    stack.push("good")
    stack.push("morning")
    actual=stack.__str__()
    expect='morning -> good -> None'
    assert actual==expect


@pytest.fixture
def stack():
    return Stack()