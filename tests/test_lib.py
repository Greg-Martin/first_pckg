from math import isclose
from first_pckg.lib import try_me

def test_value1():
    assert isclose(try_me(80, 1.75), 26.12, rel_tol=0.1)
