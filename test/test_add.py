import pytest

@pytest.fixture(params=[1,2,3])
def test_count(request):
    assert request.param != 5
