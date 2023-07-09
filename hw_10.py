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
        

phone_book = AddressBook({})


def input_error(func):
    def wrapper(*args):
        try:
            result = func(*args)
        except TypeError: 
            return "Enter the data correctly"
        except KeyError:
            return "Enter the data correctly"
        except ValueError:
            return "Enter the data correctly"
        except IndexError:
            return "Enter the data correctly"

        return result
    return wrapper


def greeting(*args):
    result = "How can I help you?"
    return result


def checking_args(*args):
    if args[0].isalpha():
        name = args[0].capitalize()
        phone = args[1]
        if (phone.startswith("+") and phone[1:].isnumeric()) or phone.isnumeric():            
            pass
        else:       
            return "Give me name and phone please"
    elif args[0].isdigit():
        return "Give me name and phone please"
    

@input_error
def add(*args):
    result = checking_args(*args)
    if result:
        return result
    else:
        name = Name(args[0].capitalize())
        phone = Phone(args[1])
        record = Record(name, phone)
        result = phone_book.add_record(record)
    return result


@input_error
def change(*args): 
    result = checking_args(*args)
    if result:
        return result
    else:
        name = Name(args[0].capitalize())
        phone = Phone(args[1])
        record = Record(name)
        if phone_book.get(record.name.value):
            rec = phone_book[record.name.value]
            if rec.phones:
                for item in rec.phones:
                    old_phone = item            
                    result = rec.change_phone(old_phone, phone)
                    return f"{name}'s {result}"
            else:
                return f"{name}'s name doesn't have a phone"
        else:
            return f"Name {name} does not exist"


@input_error
def phone(*args):
    if args[0].isalpha:
        name = Name(args[0].capitalize())
        record = Record(name)
        for key, value in phone_book.items():
            if key == record.name.value:                             
                return f"{key} has phone number {', '.join(str(phone) for phone in value.phones)}"
        else:
            return f"Name '{name}' was not found"
    else:
        return "Give me name please"
        
    
def show_all(*args):    
    return "\n".join((str(record.name) + ' - ' + ', '.join(str(phone) for phone in record.phones)) for record in phone_book.values())

def exit(*args):
    return "Good bye!"


def no_command(*args):    
    return "Unknown command. Supported commands\n\nadd name number\nchange name number\nphone name\nshow all\nexit"


commands = {greeting: ("hello", ),
            add: ("add", ),
            change: ("change", ),
            phone: ("phone", ),
            show_all: ("show all", ),
            exit: ("good bye", "close", "exit")}


def parser(text: str) -> tuple[callable, tuple[str]|None]:
    for key, value in commands.items():
        for val in value:
            if text.startswith(val):                                
                return key, text.replace(val, "").strip().split()
            
    return no_command, ""


def main():
    while True:
        user_input = input(">>>").lower()
        command, data = parser(user_input)
        result = command(*data)
        print(result)
        if result == "Good bye!":
            break
        

if __name__ == "__main__":
    main()
    