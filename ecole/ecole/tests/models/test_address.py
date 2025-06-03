from models.address import Address
import pytest


@pytest.mark.parametrize(
    "street, city, postal_code",
    [
        ("123", "Toulouse", 31400),
        ("Labege", "toulouse", 31000),
        ("Jean Jaurès", "Toulouse", 31200),
    ],
)
def test_address_type_errors(street, city, postal_code):
    if (
            not isinstance(street, str)
            or not isinstance(city, str)
            or not isinstance(postal_code, int)
    ):
        with pytest.raises(TypeError):
            raise TypeError(
                f"Invalid type(s): {type(street)}, {type(city)}, "
                f"{type(postal_code)}"
            )
    else:
        address = Address(street=street, city=city, postal_code=postal_code)
        assert isinstance(address, Address)
