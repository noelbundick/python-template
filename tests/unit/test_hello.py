from boilerplate.hello import Hello


def test_hello():
    d = Hello()
    w = d.Word()
    assert w == "world"
