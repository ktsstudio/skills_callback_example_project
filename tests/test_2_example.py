import pytest

from tasks.example_2 import Dog


class TestDog:
    @pytest.mark.skip
    def test_bark(self):
        assert Dog.bark() == 'gav', 'Dog must say gav'
