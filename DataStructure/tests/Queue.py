from StackAndQueue.Queue import Queue,Node,EmptyError
import pytest

def test_enqueue(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    actual= queue.__str__()
    expect='1 -> 2 -> None'
    assert actual==expect


def test_dequeue(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    actual= queue.__str__()
    expect='2 -> None'
    assert actual==expect


def test_peek(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    actual= queue.peek()
    expect=1
    assert actual==expect

def test_isEmpty(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    actual= queue.is_empty()
    expect=False
    assert actual==expect

def test_str(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    actual= queue.__str__()
    expect='1 -> 2 -> None'
    assert actual==expect


@pytest.fixture
def queue():
    return Queue()