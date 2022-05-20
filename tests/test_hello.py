from boilerplate import Hello


def test_hello():
    hello = Hello()
    message = hello.greet()
    assert message == "Hello, world from computer!"


def test_hello_friend():
    hello = Hello()
    message = hello.greet("friend")
    assert message == "Hello, friend from computer!"
