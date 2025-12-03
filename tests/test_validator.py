import pytest
from services.validator_service import Validator

"""
Since Validator is static we do not need a setup or teardown between tests

"""


def test_invalid_email():
    # Arrange
    # This is a bad email because it does not contain @ or end in .com or .se
    bad_email = "abcsd"

    # Act
    # We test our validator and get a result
    result = Validator.is_valid_email(bad_email)

    # Assert
    # We check that the result is correct
    assert result == False


def test_valid_email():
    # Arrange
    # This is a correct email because it has something before @ and ends in .com
    # No special characters
    bad_email = "kimmo@email.com"

    # Act
    # We test our validator and get a result
    result = Validator.is_valid_email(bad_email)

    # Assert
    # We check that the result is correct
    assert result == True


"""
Write more tests for emails:

Valid emails:
test@test.se
test@test.com
test123@test.com
123@test.com
123456LarsSvensson@test.se


Invalid emails:
@test.se
123@mail.fi
@mail.fi
totallyvalidemail.se
kimmo+ahola@test.se - no plus in the email
"""


"""
Write tests for first names:

Valid names:
Kimmo
My
Bo
Britt-Marie
Anna-Lisa
Anna Lisa     ----- spaces are ok in the middle

Invalid names:
123       ---- no numbers in the name
"  "      ----- the name can not have whitespace
Britt-  --- can not end with special characters
Marie-
!!Britt!!-Marie
"A     " - no spaces at the end

Hint for these: create a list or string of allowed characters in your function
爱爱    ---- No chinese characters
Ирина    ----- No cyrillic characters
Σοφία    ------ No Greek characters
Zoé     ----- no accents on the names. Or should it be allowed? Up to you!
"""


"""
Write tests for valid dates. Check the readme for my rules or make up your own rules!

"""
