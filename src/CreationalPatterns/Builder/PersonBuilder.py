from CreationalPatterns.Builder.Person import Person

class PersonBuilder:
    def __init__(self,person=Person()):
        self._person = person
    
    @property
    def workInfo(self):
        return EmploymentInfoBuilder(self._person)

    @property
    def liveInfo(self):
        return AddressBuilder(self._person)
    
    @property
    def personalInfo(self):
        return PersonalInfoBuilder(self._person)

    def build(self):
        return self._person

class PersonalInfoBuilder(PersonBuilder):
    def __init__(self,person):
        super().__init__(person)
    
    def his_name(self,name):
        self._person.name = name
        return self
    
    def his_age(self,age):
        self._person.age = age
        return self
    
    def his_gender(self,gender):
        self._person.gender = gender
        return self

class AddressBuilder(PersonBuilder):
    def __init__(self,person):
        super().__init__(person)
    
    def lives_at(self,address):
        self._person.street_address = address
        return self
    
    def city(self,city):
        self._person.city = city
        return self
    
class EmploymentInfoBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def works_at(self,company_name):
        self._person.company_name = company_name
        return self
    
    def as_a(self,position):
        self._person.position = position
        return self
    
    def earnings(self,value):
        self._person.annual_income = value
        return self
