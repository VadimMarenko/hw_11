from datetime import datetime
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


class Birthday(Field):
    pass


class Record():
    def __init__(self, name:Name, phone=None, birthday=None):
        self.name = name        
        self.phones = [] #[phone] if phone else []
        self.birthday = birthday        
        if phone:
            self.add_phone(phone)

    def __str__(self):
        return str(self)
        
    def __repr__(self):
        return str(self)
        
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
    
    def days_to_birthday(self, birthday:datetime):
        date_now = datetime.now().date()
        date_bd = self.birthday.replace(year=date_now.year)
        if date_bd >= date_now:            
            result = date_bd - date_now
        else:
            date_bd = self.birthday.replace(year=date_now.year + 1)
            result = date_bd - date_now

        return f"{self.name}'s birthday will be in {result} days"


class AddressBook(UserDict):    
    def add_record(self, record: Record):
        if record.name.value not in self.keys():
            self.data[record.name.value] = record 
            return f"Added {record.name.value} with phone number {', '.join(str(phone) for phone in record.phones)}"
        else:            
            return f"Record {record.name.value} alredy exists"
        