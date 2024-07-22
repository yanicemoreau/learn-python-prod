import pytest

@pytest.fixture
def mylist():
    return [1,2,3]

@pytest.mark.skip
def test_a1():
    print("This is my first test")
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1
 
@pytest.mark.parametrize('a', [1, 20, 300])
@pytest.mark.parametrize('b', [1000, 2000, 3000])
def test_parametrize(a,b):
    assert a < b

def test_list(mylist):
    assert len(mylist) == 3

a : int = "abc"
