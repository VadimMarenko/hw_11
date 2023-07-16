from datetime import datetime
from classes import AddressBook, Record, Birthday, Name, Phone


address_book = AddressBook({})


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except (TypeError, KeyError, ValueError, IndexError) as e: 
            return f"{e} Enter the data correctly"
                    
    return wrapper

@input_error
def birthday_command(*args):
    name = Name(args[0].capitalize())
    bd = Birthday(args[1])
    if name in address_book:
        rec: Record = address_book[str(name)]    
        rec.birthday = bd
        return rec.days_to_birthday(bd)
        return f"Added date of birth {str(rec.birthday)} for {name}"
    else:
        rec = Record(name, birthday=bd)
        address_book.add_record(rec)
        return rec.days_to_birthday(bd)
    return f"{name}'s birthday {bd}"


@input_error
def add_command(*args):
    name = Name(args[0].capitalize())
    phone = Phone(args[1])
    rec: Record = address_book.get(str(name))
    if rec:
        return rec.add_phone(phone)
    else:
        record = Record(name, phone)
        return address_book.add_record(record)
     

@input_error
def change_command(*args): 
    name = Name(args[0].capitalize())
    old_phone = Phone(args[1])
    new_phone = Phone(args[2])  
    rec: Record = address_book.get(str(name))
    if rec:
        return rec.change_phone(old_phone, new_phone)
    return f"No contact {name} in address book"
    

@input_error
def phone_command(*args):    
    name = Name(args[0].capitalize())
    record = Record(name)
    for key, value in address_book.items():
        if key == record.name.value:                             
            return f"{key} has phone number {', '.join(str(phone) for phone in value.phones)}"
    else:
        return f"Name '{name}' was not found"
        
    
def greeting_command(*args):
    return f"How can I help you? \
        \n {help()}"


def show_all_command(*args):
    return "\n".join((str(record.name) + ' ' + (str(record.birthday) if record.birthday else "-") + ' ' + (', '.join(str(phone) for phone in record.phones))) for record in address_book.values())


def exit_command(*args):
    return "Good bye!"


def help():
    return "Supported commands\n \
        \nadd name number \
        \nchange name number \
        \nphone name \
        \nshow all \
        \nbirthday name dd-mm-yyyy \
        \nexit \
        \n"


def no_command(*args):    
    return f"Unknown command. {help()}"


COMMANDS = {
    greeting_command: ("hello", ),
    add_command: ("add", ),
    change_command: ("change", ),
    phone_command: ("phone", ),
    show_all_command: ("show all", ),
    birthday_command: ("birthday", ),
    exit_command: ("good bye", "close", "exit")
}


def parser(text: str):
    for key, value in COMMANDS.items():
        for val in value:
            if text.startswith(val):                                
                return key, text[len(val):].strip().split()
            
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
    