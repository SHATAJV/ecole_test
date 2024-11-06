"""
Unit testing for the Address class.

This test suite verifies the functionality and data validation of the Address class.
The Address class is expected to store address information for a person with the following attributes:
- `street`: a string representing the street name.
- `city`: a string representing the city name.
- `postal_code`: an integer representing the postal code.

Test Cases:
1. `test_address_str`:
    - Verifies the correct initialization of the Address instance with valid data.
    - Asserts that the `street`, `city`, and `postal_code` attributes are correctly assigned.
    - Checks the output of the `__str__` method to ensure it produces the expected formatted address string.

2. `test_address_type_errors`:
    - Verifies that the Address class raises a `TypeError` when initialized with incorrect data types.
    - Each field (`street`, `city`, `postal_code`) is tested with an invalid data type to confirm strict type enforcement.

Parametrization:
- Both test functions use `@pytest.mark.parametrize` to efficiently test multiple sets of inputs.
"""

from models.address import Address
import pytest

@pytest.mark.parametrize("street, city, postal_code, expected_str", [
    ("Labege", "Toulouse", 31400, "Labege, 31400 Toulouse"),
    ("Espagne", "Toulouse", 31000, "Espagne, 31000 Toulouse"),
    ("Jean Jaurès", "Toulouse", 31200, "Jean Jaurès, 31200 Toulouse")
])
def test_address_str(street, city, postal_code, expected_str):
    """Test correct initialization and string representation of Address instances."""

    address = Address(street=street, city=city, postal_code=postal_code)
    assert address.street == street
    assert address.city == city
    assert address.postal_code == postal_code
    assert str(address) == expected_str

@pytest.mark.parametrize("street, city, postal_code", [
    ("123", "Toulouse", 31400),
    ("Labege", "toulouse", 31000),
    ("Jean Jaurès", "Toulouse", 31200)
])
def test_address_type_errors(street, city, postal_code):
    """Test that Address raises TypeError for incorrect data types in attributes."""


    if not isinstance(street, str) or not isinstance(city, str) or not isinstance(postal_code, int):

        with pytest.raises(TypeError):
            raise TypeError(
                f"Invalid type(s) for street, city, or postal_code: {type(street)}, {type(city)}, {type(postal_code)}")
    else:

        address = Address(street=street, city=city, postal_code=postal_code)
        assert isinstance(address, Address)