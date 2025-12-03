from services.customer_service import Customer, CustomerService

if __name__ == "__main__":
    service = CustomerService()
    result: Customer | None = service.create_customer()
    if result:
        print("Du har skapat en 'Kund' som ser ut som följande: ")
        print("Förnamn: ", result.first_name)
        print("Efternamn: ", result.last_name)
        print("E-post: ", result.email)
    else:
        print("Du avbröt och en kund skapades inte!")
