import pytest

@pytest.parametrize('a, b', [
    'spam', bytes('4:spam'),
    '' , bytes('0:'),
    'фыв' , bytes('3:фыв')
])
def test_encode_str(a, b):
    pass

@pytest.parametrize('a, b', [
    (3, 'i3e'),
    (-3, 'i-3e'),
])

def test_encode_int(a, b):
    assert bytes(b) == encode(a)
