from collections import UserDict

class Field():
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)    
 
     
class Name(Field):
    pass


class Phone(Field):
    pass


class Record():
    def __init__(self, name: Name, phone=None):
        self.name = name        
        self.phones = [phone] if phone else []

    def __str__(self):
        return f'{self.name.value}: {self.phones}'
        
    def __repr__(self):
        return str(self.phones)
        
    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def delete_phone(self, phone):
        for item in self.phones:
            if item.value == phone.value:
                self.phones.remove(item)

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        self.delete_phone(old_phone)
        self.phones.append(new_phone)
        return f"phone {old_phone} was replaced by {new_phone}"


class AddressBook(UserDict):    
    def add_record(self, record: Record):
        if record.name.value not in self.keys():
            self.data[record.name.value] = record 
            return f"Added {record.name.value} with phone number {', '.join(str(phone) for phone in record.phones)}"
        else:            
            return f"Record {record.name.value} alredy exists"
        