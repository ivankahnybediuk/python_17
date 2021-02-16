"""
Task 2
Extend Phonebook application
Functionality of Phonebook application:
Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program
The first argument to the application should be the name of the phonebook. Application should load JSON data, if it is
 present in the folder with application, else raise an error. After the user exits, all data should be saved
 to loaded JSON.
"""
import json


def rewritting_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)


def add_new_entries(name, lastname, phone, city):
    # name = input('Имя: ').capitalize()
    # lastname = input("Фамилия: ").capitalize()
    # phone = input("Телефон: ")
    # city = input("Город: ")
    reading('phonebook.json')
    contact = {
        'firstName': name,
        "lastName": lastname,
        "fullName": name + " " + lastname,
        "phone": phone,
        "city": city
    }
    load_list.append(contact)
    rewritting_json('phonebook.json', load_list)


def searching(parametr, value):
    with open('phonebook.json') as file:
        phonebook = json.load(file)
        search_result = []
        for item in phonebook:
            if item.get(parametr) == value:
                search_result.append(item)
                printing_contact(item)
        if search_result == 0:
            print('не найдено!!!!')



def printing_contact(item):
    print(
        f"{'-' * 20}\n Имя: {item['firstName']}\nФамилия: {item['lastName']}\nТелефон: {item['phone']}\nГород: {item['city']}\n"
        + "-" * 20)


def delete_by_phone(phone):
    item = searching('phone', phone)
    load_list.remove(item)
    rewritting_json('phonebook.json', load_list)


def update_contact(phone):
    item = searching('phone', phone)
    load_list.remove(item)
    new_name = input("Введите новое имя (просто Enter, если без изменений)").capitalize()
    new_lasrname = input("Введите новую фамилию (просто Enter, если без изменений)").capitalize()
    new_phone = input("Введите новый телефон (просто Enter, если без изменений)")
    new_city = input("Введите новый город (просто Enter, если без изменений)").capitalize()
    if new_name:
        item["firstName"] = new_name
        item["fullName"] = new_name + " " + item["lastName"]
    if new_lasrname:
        item["lastName"] = new_lasrname
        item["fullName"] = item["firstName"] + " " + new_lasrname
    if new_phone:
        item["phone"] = new_phone
    if new_city:
        item["city"] = new_city
    load_list.append(item)
    rewritting_json('phonebook.json', load_list)


def reading(file):
    with open(file) as file_read:
        try:
            load_list = json.load(file_read)
        except:
            load_list = []
        return load_list

if __name__ == "__main__":
    reading()
    action = input('Нужно добавить контакт(A), искать в книге(S), удалить(D) или изменить(C) контакт?').upper()
    if action == "A":
        add_new_entries()
    elif action == "D":
        phone_to_delete = input('Введите номер для удаления \n')
        delete_by_phone(phone_to_delete)
    elif action == "C":
        phone_to_change = input('Введите номер для изменения \n')
        update_contact(phone_to_change)
    elif action == "S":
        search_by = input(
            "Вы выбрали поиск, по какому параметру искать? N - имя, L- фамилия, F - полное имя, P - номер,"
            " C - город").upper()
        searching_parametrs = {
            "N": 'firstName',
            "L": "lastName",
            "F": "fullName",
            "P": "phone",
            "C": "city"
        }
        search_by_value = (input(" Введите значение для поиска \n").lower()).capitalize()
        if search_by in searching_parametrs.keys():
            for key, value in searching_parametrs.items():
                searching(value, search_by_value)
        else:
            print("Не верные данные!")



