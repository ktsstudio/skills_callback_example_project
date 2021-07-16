from tasks.example_1 import Cat


def test_meow():
    assert Cat.meow() == 'meow', 'Cat must say meow'
