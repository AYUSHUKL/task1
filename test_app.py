from app import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    # This test is intentionally wrong to trigger a failure
    assert subtract(10, 5) == 4  # Should be 5, but we write 4
