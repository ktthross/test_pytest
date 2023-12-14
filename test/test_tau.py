from test_pytest import functions

import non_existent_package

def test_tau():
    assert functions.tau() == 6.28
