import json
from json import JSONEncoder

class Contact:
    def __init__(self, name, surname,  phone, city):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.fullname = f"{self.name} {self.surname}"
        self.phone = phone
        self.city = city.capitalize()


    def __str__(self):
        return f'{self.fullname}\n{self.phone}\n{self.city}\n'

    def __eq__(self, other):
       return self.__dict__== other


class ContactEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Phonebook:
    def __init__(self, name, contactList = []):
        self.filename = f"{name}.json"
        self.contactList = contactList


    def add_contact(self, contact):
        if isinstance(contact, Contact):
            try:
                with open(self.filename) as f:
                    self.contactList = json.load(f)
                    self.contactList.append(contact)
            except:
                self.contactList.append(contact)
        else:
            raise TypeError ("Invalid type of contsct")

    def deleteContact(self, name):
        with open (self.filename) as f:
            self.contactList = json.load(f)
            for i in self.contactList:
                if i['fullname'] == name:
                    self.contactList.remove(i)


    def saving_changing(self):
        with open(self.filename, 'w') as f:
            json.dump(self.contactList, f, cls=ContactEncoder)

if __name__ == "__main__":
    first = Phonebook("first")
    first.add_contact(Contact("Иванка", "гнибедюк", "09812876366", "киев"))
    first.add_contact(Contact("Valya", "Kin", "0981287556", "киев"))
    first.deleteContact("Valya Kin")
