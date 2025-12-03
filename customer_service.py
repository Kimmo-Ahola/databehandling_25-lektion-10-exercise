from validator import Validator

class Customer():
    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email

class CustomerService():
    def get_valid_email(self) -> str:
        while True:
            email: str = input("Ange en e-post: ")
            if Validator.is_valid_email(email):
                return email
            else:
                print("Din epost var inte korrekt!")

    def get_valid_first_name(self) -> str:
        while True:
            name: str = input("Ange ett förnamn: ")
            if Validator.is_valid_first_name(name):
                return name
            else:
                print("Ditt namn var inte korrekt. Försök igen!")

    def get_valid_last_name(self) -> str:
        while True:
            name: str = input("Ange ett förnamn: ")
            if Validator.is_valid_first_name(name):
                return name
            else:
                print("Ditt namn var inte korrekt. Försök igen!")

    def create_customer(self) -> Customer:
        first_name: str = self.get_valid_first_name()
        last_name: str = self.get_valid_last_name()
        email: str = self.get_valid_email()

        return Customer(first_name, last_name, email)