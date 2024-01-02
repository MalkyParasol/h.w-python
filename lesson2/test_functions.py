import pytest
import functions


@pytest.mark.malky
def test_find_primes():
    assert functions.find_primes(5) == {1, 2, 3}
    assert functions.find_primes(7) == {1, 2, 3}
    assert functions.find_primes(-12) == set()


@pytest.mark.parametrize("mylist,res", [([4, 3, 8, 1], [1, 3, 4, 8]),
                                        ([4, 45, 8, 1], [1, 4, 8, 45])])
def test_sorted_list(mylist, res):
    assert functions.sort_list(list) == res


