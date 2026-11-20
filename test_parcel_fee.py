import pytest
from parcel_fee import delivery_fee

# test valid weight bands
@pytest.mark.parametrize("weight, expected_fee", [
    (1, 500),
    (500, 500),
    (1000, 500),
    (1001, 1000),
    (10000, 1000),
    (20000, 1000)
])
def test_delivery_fee(weight, expected_fee):
    assert delivery_fee(weight) == expected_fee


# test invalid weight bands
@pytest.mark.parametrize("weight", [
    0, -1, 20001,
])
def test_delivery_fee_invalid_weight(weight):
    with pytest.raises(ValueError):
        delivery_fee(weight)


# test invalid data types
@pytest.mark.parametrize("weight", [
    "500", 5.0, True, False, None
])
def test_delivery_fee_invalid_data_type(weight):
    with pytest.raises(TypeError):
        delivery_fee(weight)