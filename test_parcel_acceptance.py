import pytest
from parcel_acceptance import is_parcel_accepted

# test valid acceptances of parcels
@pytest.mark.parametrize("weight, length, expected", [
    (1, 1, True),
    (500, 100, True),
    (20000, 200, True)
])
def test_is_parcel_accepted(weight, length, expected):
    result = is_parcel_accepted(weight, length)
    assert result == expected
    assert type(result) is bool


# test invalid acceptances of parcels
@pytest.mark.parametrize("weight, length, expected", [
    (0, 100, False),
    (10000, 0, False),
    (0, 0, False),
    (20001, 100, False),
    (10000, 201, False),
    (20001, 201, False),
])
def test_is_parcel_invalid(weight, length, expected):
    result = is_parcel_accepted(weight, length)
    assert result == expected
    assert type(result) is bool


# test negative measurements
@pytest.mark.parametrize("weight, length", [
    (-1, 100),
    (10000, -1),
    (-1, -1)
])
def test_is_parcel_negative(weight, length):
    with pytest.raises(ValueError):
        is_parcel_accepted(weight, length)


# test invalid data types
@pytest.mark.parametrize("weight, length", [
    ("100", 100),
    (100, "100"),
    (5.0, 100),
    (100, 5.0),
    (True, 100),
    (100, False),
    (None, 100),
    (100, None),
])
def test_is_parcel_invalid_type(weight, length):
    with pytest.raises(TypeError):
        is_parcel_accepted(weight, length)