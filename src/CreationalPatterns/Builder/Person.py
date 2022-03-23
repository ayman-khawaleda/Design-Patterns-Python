


class Person:
    def __init__(self):
    # PersonInfo
        self.name = None
        self.age = None
        self.gender = None
    #address
        self.street_address = None
        self.city = None
    #employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f"PersonalInfo: {self.name}|{self.age}|{self.gender}\nAddressInfo: {self.street_address}|{self.city}\nEmploymentInfo: {self.company_name}|{self.position}|{self.annual_income}\n"
