import pytest
from pytest_testrail.plugin import pytestrail
@pytestrail.case('C2')
def test_sub():
    assert True
@pytestrail.case('C3')
def test_sub_02():
    assert False