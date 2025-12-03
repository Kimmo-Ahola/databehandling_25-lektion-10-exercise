import pytest
from services.customer_service import Customer, CustomerService


@pytest.fixture
def setup() -> CustomerService:
    return CustomerService()


def test_create_customer(setup: CustomerService, monkeypatch) -> None:
    # Arrange
    first_name = "Kimmo"
    last_name = "Ahola"
    email = "kimmoahola@test.se"

    # This is an example of mocking
    # Since the create_customer method needs to get values from the methods inside it
    # we fake method calls using monkeypatch
    monkeypatch.setattr(setup, "get_valid_first_name", lambda: first_name)
    monkeypatch.setattr(setup, "get_valid_last_name", lambda: last_name)
    monkeypatch.setattr(setup, "get_valid_email", lambda: email)

    # Act
    result: Customer | None = setup.create_customer()

    # Assert

    assert result is not None
    assert result.first_name == first_name
    assert result.last_name == last_name
    assert result.email == email


def test_create_invalid_customer(setup: CustomerService, monkeypatch) -> None:
    # Arrange
    first_name = None # Invalid first name
    last_name = "Ahola"
    email = "email@email.se"

    # This is an example of mocking
    # Since the create_customer method needs to get values from the methods inside it
    # we fake method calls using monkeypatch
    monkeypatch.setattr(setup, "get_valid_first_name", lambda: first_name)
    monkeypatch.setattr(setup, "get_valid_last_name", lambda: last_name)
    monkeypatch.setattr(setup, "get_valid_email", lambda: email)

    # Act
    result: Customer | None = setup.create_customer()

    # Assert

    assert result is None
