"""
Task 1
Pick your solution to one of the exercises in this module. Design tests for this solution and write tests
using unittest library.
"""
# import unittest
# from homework_12 import Library, Book, Author
#
#
class LibraryTest(unittest.TestCase):
    def setUp(self):
        self.library_name = "FirstLibrary"
        self.firstLibrary = Library(self.library_name, [], set())

    def testSettingObject(self):
        self.assertEqual(self.firstLibrary.name, self.library_name)

    def testNewLibraryEmtpy(self):
        # убедимся что у нас в новой библиотеке ничего нет
        self.assertEqual(self.firstLibrary.books, []) # книг нет
        self.assertEqual(self.firstLibrary.authors, {}) # авторов нет
        
    def testingNewBookMethod(self):
        author_name = "Джоан Роулинг"
        rowling = Author(author_name, "Великобритания", "31 июля 1965г", [])
        self.firstLibrary.new_book(Book("Гарри Поттер и философский камень", 1997, rowling))
        # мы дали книгу автора проверяем есть ли в ней наш автор только и всего.
        self.assertContains(self.firstLibrary.authors, author_name)
        # вот тут ты ступаешь по тонкому льду вмешательства в личную жизнь класса. Проверяем что книгу дали книга есть. Не на какой она полке (индексе) а просто есть и все.
        self.assertIsInstance(self.firstLibrary.books[0], Book)


if __name__ == '__main__':
    unittest.main()


"""
Task 2

Write tests for the Phonebook application, which you have implemented in module 1. Design tests for this solution and 
write tests using unittest library
"""
import unittest
import phonebook
import json
from phonebook import Contact, Phonebook
import os

class ContactTest(unittest.TestCase):
    def setUp(self) -> None:
        """
        def __init__(self, name, surname,  phone, city):
        """
        self.testContact = Contact("Ivanka", "hnybediuk", "0981777", "kiev")

    def testInit(self):
        self.assertEqual(self.testContact.name, "Ivanka")
        self.assertEqual(self.testContact.surname, "Hnybediuk")
        self.assertEqual(self.testContact.fullname, "Ivanka Hnybediuk")
        self.assertEqual(self.testContact.phone, "0981777")
        self.assertEqual(self.testContact.city, "Kiev")

    def testPrint(self):
        self.assertEqual(self.testContact.__str__(), 'Ivanka Hnybediuk\n0981777\nKiev\n')



class PhonebookTest(unittest.TestCase):
    def setUp(self):
        self.testPhonebook = Phonebook('testBook')
        self.testContact = Contact("Ivanka", "hnybediuk", "0981777", "kiev")
        self.anValidContact = Contact("Galya", "hnybediuk", "8888777", "vinitsia")
        self.invalidContact = 'Ivanka Hnybediuk 0988888 kiev'

    def testInit(self):
        #не используем файл существующий. Создаем темповый файл и в него в сетапе класса или теста пишем если нужны данные
        self.assertEqual(self.testPhonebook.filename, "testBook.json")
        self.assertIsInstance(self.testPhonebook.contactList, list)


    def testAdd_contact(self):
        self.testPhonebook.add_contact(self.testContact)
        self.assertIn(self.testContact, self.testPhonebook.contactList)


    @unittest.expectedFailure
    def testAddInvalidContact(self):
        self.testPhonebook.add_contact(self.invalidContact)


    def testSaving(self):
        #проверить что данные сохраняются можно только выгрузив их во временный файл а потом оттуда загрузить и убедиться что есть что.
        self.testPhonebook.add_contact(self.testContact)
        self.testPhonebook.saving_changing()
        self.assertTrue(os.path.exists(self.testPhonebook.filename))
        #писать функционал а именно читать файл тут не верно. Мы хотим под определенным именем сохранить. Где в какой папке это будет сложено это дело метода сохранения (может вообще на стороннем сервере)
        with open(self.testPhonebook.filename) as f:
            data = json.load(f)
            self.assertIn(self.testContact, data)

    def testDelete(self):
        self.testPhonebook.add_contact(self.testContact)
        self.testPhonebook.add_contact(self.anValidContact)
        self.testPhonebook.saving_changing()
        self.testPhonebook.deleteContact(self.anValidContact.fullname)
        self.testPhonebook.saving_changing()
        with open(self.testPhonebook.filename) as f:
            data = json.load(f)
            self.assertNotIn(self.anValidContact, data)

    def tearDown(self):
        if os.path.exists(self.testPhonebook.filename):
            os.remove(self.testPhonebook.filename)


if __name__ == "__main__":
    unittest.main()
