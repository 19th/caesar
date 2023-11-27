import pytest

from cipher import encrypt, decrypt

def test_rot3():
    assert decrypt('ZHOFRPH WR JUDYLWB IDOOV', 3) == 'WELCOME TO GRAVITY FALLS'
