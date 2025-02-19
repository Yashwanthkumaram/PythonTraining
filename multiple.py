phone_map ={}


class ContactDetails:
    def __init__(self, phone_number, address):
        if phone_map.__contains__(phone_number):
            raise Exception("phone number already used")
        phone_map[phone_number]=True
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return (f"Employee contaact number {self.phone_number} and lives in {self.address} ")
    


class Person:
    def __init__(self, name , dob, contact):
        self.name = name
        self.dob = dob
        self.contact = contact
        
 
    def display(self):
        print(self.name)

    def __str__(self):
        return (f"emp name is {self.name} ")
 
class Employee(Person):
    def attribute_validator(self, name, idnumber, salary, post, dob, contacts):
        if type(contacts) is not list:
            raise Exception("not a list")
        else:
            for contact in contacts:
                if type(contact) is not ContactDetails:
                    raise Exception ("Not All List elements are Contact Objects")
        if type(name) is not str :
            raise Exception(f"{name} not a String")
        if type(idnumber) is not int:
            raise Exception(f"{idnumber} not a Number")
        if type(salary) is not int:
            raise Exception(f"{salary} not a Number")
        if type(post) is not str:
            raise Exception(f"{post} not a String")
        if type(dob) is not str:
            raise Exception(f"{dob} not a String")
        
        
        


    def __init__(self, name, idnumber, salary, post, dob, contacts ):
        
        self.attribute_validator( name, idnumber, salary, post, dob, contacts )               

        super().__init__(name,dob,contacts)  # Using super() to call Person's __init__()
        self.idnumber=idnumber
        self.salary = salary
        self.post = post

    def has_id():
        print(self.idnumber)

    def __str__(self):
        return (f" emp name is {self.name} and has emp id {self.idnumber} and  has salary {self.salary} and emp post{self.post} an was born on {self.dob} has phone numbers {[i.phone_number for i in contacts]} and lives {[i.address for i in contacts]} ")


contact1 = ContactDetails(12345 ,"PG ADDress")
contact2 = ContactDetails(12334567 ,"PG ADDress")
contact3 = ContactDetails(54322 ,"home ADDress")
contact4 = ContactDetails(54322 ,"home ADDress")

contact = [contact1, contact2 , "hello I'm the imposter"]
contacts = [contact1, contact2, ]



emp =Employee("ramesh",124, 45322,"intern", "12/12/2003",contacts)



print(emp)

# Same as yesterday added UNIQUE Contacts Contraints




