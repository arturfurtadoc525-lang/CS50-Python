import pytest
from jar import Jar



def test_init():
    jar = Jar()
    assert jar.capacity == 12
    with pytest.raises(ValueError):
        jar.capacity = -1

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(6)
    jar.capacity = jar.size
    assert jar.capacity == 6
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(3)
    assert str(jar) == ""
    with pytest.raises(ValueError):
        jar.withdraw(1)
