#Referência: https://docs.pytest.org/en/7.1.x/getting-started.html

import pytest

class TestClassDemoInstance:
    name = "Sherlon"
    age  = 28

    def test_one(self):
        assert self.name == "Sherlon"

    def test_two(self):
        assert self.age == 28
    
    def test_multiplicacao(self):
        assert 9*9 == 81