from faker import Faker
fake = Faker()

class NameCard:
    def __init__ (self, name,company, position, email) :
        self.name= name 
        self.company = company
        self.position = position
        self.email = email
        
        
    def __str__(self):
        return f' {self.name}  , {self.company} . {self.position} , {self.email}'
    
    # Rozwiniecie o CONTACT - nie działa poprawnie
    def contact (self) :
        print ("dzwonie do ",  self.name)
       
base = []
for i in range(5):
    person  = NameCard (name=fake.name(), company=fake.company(), position=fake.job(), email=fake.email())
    base.append(person)
    print(person)


print ("-----------")

class Base(NameCard):
    def __init__(self, phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone = phone
        
    def __str__(self):
        return f' name : {self.name} , phone :  {self.phone} , email : {self.email}'
for i in range(5):
     person_base  = Base (company = fake.company(), name=fake.name(), phone= fake.phone_number(), position=fake.job(), email=fake.email())
    
     print(person_base)

print ("xxxxxxxx")

class Business(Base):
    def __init__(self,*args, **kwargs):
       super().__init__(*args, **kwargs)
       
    def __str__(self):
        return f' position : {self.position} , company :  {self.company} , phone : {self.phone}'
    def __str__(self):
        return f'Wybieram numer : {self.phone} i dzwonie do {self.name}'
for i in range(5):
     person_business  = Business (position=fake.job(), name=fake.name(),company= fake.company(), email=fake.email(), phone=fake.phone_number())
    
     print(person_business)

    

  