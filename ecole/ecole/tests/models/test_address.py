
from models.address import Address
import pytest


@pytest.mark.parametrize(
    "street, city, postal_code, expected_str",
    [
        ("Labege", "Toulouse", 31400, "Labege, 31400 Toulouse"),
        ("Espagne", "Toulouse", 31000, "Espagne, 31000 Toulouse"),
        ("Jean Jaurès", "Toulouse", 31200, "Jean Jaurès, 31200 Toulouse"),
    ],
)
def test_address_str(street, city, postal_code, expected_str):


    address = Address(street=street, city=city, postal_code=postal_code)
    assert address.street == street
    assert address.city == city
    assert address.postal_code == postal_code
    assert str(address) == expected_str


@pytest.mark.parametrize(
    "street, city, postal_code",
    [
        ("123", "Toulouse", 31400),
        ("Labege", "toulouse", 31000),
        ("Jean Jaurès", "Toulouse", 31200),
    ],
)
def test_address_type_errors(street, city, postal_code):


    if not isinstance(street, str) or not isinstance(city, str) or not isinstance(postal_code, int):
        with pytest.raises(TypeError):
            raise TypeError(
                f"Invalid type(s) for street, city, or postal_code: {type(street)}, {type(city)}, {type(postal_code)}"
            )
    else:
        address = Address(street=street, city=city, postal_code=postal_code)
        assert isinstance(address, Address)
