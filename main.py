from datetime import datetime
from classes import AddressBook, Record, Field, Birthday, Name, Phone


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

@input_error
def birthday_command(*args):
    name = Name(args[0].capitalize())
    bd = Birthday(datetime.strptime(args[1], "%Y-%m-%d").date())
    if name in phone_book:
        rec = phone_book[name]    
        rec.birthday = bd
    else:
        rec = Record(name, birthday=bd)
        phone_book.add_record(rec)
    return f"{name}'s birthday {bd}"


def greeting_command(*args):
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
def add_command(*args):
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
def change_command(*args): 
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
def phone_command(*args):
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
        
    
def show_all_command(*args):
    return "\n".join((str(record.name) + ' - ' + ', '.join(str(phone) for phone in record.phones)) for record in phone_book.values())

def exit_command(*args):
    return "Good bye!"


def no_command(*args):    
    return "Unknown command. Supported commands\n \
        \nadd name number\nchange name number\nphone name\nshow all\nbirthday name yyyy-mm-dd\nexit"


commands = {greeting_command: ("hello", ),
            add_command: ("add", ),
            change_command: ("change", ),
            phone_command: ("phone", ),
            show_all_command: ("show all", ),
            birthday_command: ("birthday", ),
            exit_command: ("good bye", "close", "exit")}


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
    