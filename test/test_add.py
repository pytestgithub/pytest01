import pytest

@pytest.fixture(params=[1,2,3])
def data(request):
    return request.params

def test_data(data):
    assert data!=4
