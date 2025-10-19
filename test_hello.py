# test_hello.py
from hello import greet

def test_greet():
    assert "Hello" in greet()
