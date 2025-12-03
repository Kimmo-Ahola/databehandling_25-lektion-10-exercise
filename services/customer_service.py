from services.validator_service import Validator


class Customer:
    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email


class CustomerService:
    def get_valid_email(self) -> str | None:
        while True:
            print("Det är bra att skriva ut reglerna för vad som gäller för en email")
            email: str = input("Ange en e-post (q to quit): ")
            if email == "q":
                return None
            if Validator.is_valid_email(email):
                return email
            else:
                print("Din epost var inte korrekt!")

    def get_valid_first_name(self) -> str | None:
        while True:
            print(
                "Det är bra att skriva ut reglerna för vad som gäller för ett förnamn: minst 2 tecken, inga specialtecken, inga mellanrum etc. Era regler gäller!"
            )
            name: str = input("Ange ett förnamn (q to quit): ")
            if name == "q":
                return None
            if Validator.is_valid_first_name(name):
                return name
            else:
                print("Ditt namn var inte korrekt. Försök igen!")

    def get_valid_last_name(self) -> str | None:
        while True:
            print(
                "Det är bra att skriva ut reglerna för vad som gäller för ett efternamn: minst 2 tecken, inga specialtecken, inga mellanrum etc. Era regler gäller!"
            )
            name: str = input("Ange ett efternamn (q to quit): ")
            if name == "q":
                return None
            if Validator.is_valid_last_name(name):
                return name
            else:
                print("Ditt namn var inte korrekt. Försök igen!")

    def create_customer(self) -> Customer | None:
        first_name: str | None = self.get_valid_first_name()
        last_name: str | None = self.get_valid_last_name()
        email: str | None = self.get_valid_email()

        if first_name and last_name and email:
            return Customer(first_name, last_name, email)
        else:
            return None
