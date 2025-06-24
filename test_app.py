from app import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    # Intentional failure
    assert subtract(10, 5) == 4  # This should fail, correct value is 5
