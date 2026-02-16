class Company:
    def __init__(self, company_id: int, name: str, email: str):
        self.company_id = company_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Company({self.company_id}, {self.name}, {self.email})"
        
comp1 = Company(101, "Tech Solutions Inc.", "contact@techsolutions.com")
print(comp1)        