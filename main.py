from customer_service import Customer, CustomerService

if __name__ == "__main__":
    service = CustomerService()
    result: Customer = service.create_customer()

    print("Du har skapat en 'Kund' som ser ut som följande: ")
    print("Förnamn: ", result.first_name)
    print("Efternamn: ", result.last_name)
    print("E-post: ", result.email)
