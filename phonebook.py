#****************************************************************************************************
#
#       Name:         Alex Orescanin
#       Course:       COSC 2110 Computer Languages: Python
#       Assignment:   phonebook.py
#       Due Date:     11/27/2020
#       Description:
#               This program will allow the user to manipulate the database
#
#****************************************************************************************************

import sqlite3

def main():
    keep_going = 1

    while keep_going != 6:
        print(' ' * 20, 'Menu')
        print('-' * 50)
        print('1 - Display All\n2 - Create a New Phonebook Entry\n'
              '3 - Read a Phonebook Entry\n4 - Update a Phonebook Entry\n'
              '5 - Delete a Phonebook Entry\n6 - Exit')
        keep_going = int(input('Enter your choice: '))
        while keep_going < 1 or keep_going > 6:
            keep_going = int(input('Invalid option, please re-enter: '))

        if keep_going == 1:
            display_all()

        elif keep_going == 2:
            create_row()

        elif keep_going == 3:
            read_row()

        elif keep_going == 4:
            update_row()

        elif keep_going == 5:
            delete_row()

        print('\n')

#****************************************************************************************************

def display_all():
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()

        cur.execute('''SELECT *
                        FROM Entries''')

        results = cur.fetchall()

        for row in results:
            print(f'{row[0]:<4} {row[1]:16} {row[2]}')

    except sqlite3.Error as err:
        print("database error ", err)

    finally:
        if conn != None:
            conn.close()

#****************************************************************************************************

def create_row():
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()

        newName = input('Name: ')
        newPhone = input('Phone Number: ')

        cur.execute('''INSERT INTO Entries (Name, Phone)
                        VALUES(?, ?)''', (newName, newPhone))

        print('New Entry Added')

        conn.commit()

    except sqlite3.Error as err:
        print("database error ", err)

    finally:
        if conn != None:
            conn.close()

#****************************************************************************************************

def read_row():
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()

        nameRequest = input('Name to search for: ')

        cur.execute('''SELECT Name, Phone
                        FROM Entries
                        WHERE Name == ?''', (nameRequest,))
        result = cur.fetchall()

        if not result:
            print('Item is not in database.')
        else:
            for row in result:
                print(f'{row[0]:<16} {row[1]}')

    except sqlite3.Error as err:
        print("database error ", err)

    finally:
        if conn != None:
            conn.close()

#****************************************************************************************************

def update_row():
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()

        nameRequest = input('Name to search for: ')

        cur.execute('''SELECT *
                        FROM Entries
                        WHERE Name == ?''', (nameRequest,))
        results = cur.fetchall()

        if not results:
            print('Item is not in database.')
        else:
            print('ID  Name            Phone')
            for row in results:
                print(f'{row[0]:<4} {row[1]:16} {row[2]}')
            ID_request = int(input('Enter the ID of the entry you wish to update: '))
            newName = input('Enter the new name: ')
            newPhone = input('Enter the new phone: ')
            cur.execute('''UPDATE Entries
                            SET Name = ?
                            WHERE EntryID == ?''',
                            (newName, ID_request))
            cur.execute('''UPDATE Entries
                            SET Phone = ?
                            WHERE EntryID == ?''',
                            (newPhone, ID_request))

            print('Entry Updated.')

            conn.commit()

    except sqlite3.Error as err:
        print("database error ", err)

    finally:
        if conn != None:
            conn.close()

#****************************************************************************************************

def delete_row():
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()

        nameRequest = input('Name to search for: ')

        cur.execute('''SELECT *
                        FROM Entries
                        WHERE Name == ?''', (nameRequest,))
        results = cur.fetchall()

        if not results:
            print('Item is not in database.')
        else:
            id = 'ID'
            name = 'Name'
            phoneNum = 'Phone Number'
            print(f'{id:<4} {name:16} {phoneNum}')
            for row in results:
                print(f'{row[0]:<4} {row[1]:16} {row[2]}')
            ID_request = int(input('Enter the ID of the entry you wish to delete: '))
            response = input('Are you sure? (y/n)')
            if response.lower() == 'y':
                cur.execute('''DELETE FROM Entries
                                WHERE EntryID == ?''',
                                (ID_request,))

            print('Entry Deleted.')

            conn.commit()

    except sqlite3.Error as err:
        print("database error ", err)

    finally:
        if conn != None:
            conn.close()


#****************************************************************************************************

if __name__ == '__main__':
    main()

#****************************************************************************************************
# Sample Output:
#                      Menu
# --------------------------------------------------
# 1 - Display All
# 2 - Create a New Phonebook Entry
# 3 - Read a Phonebook Entry
# 4 - Update a Phonebook Entry
# 5 - Delete a Phonebook Entry
# 6 - Exit
# Enter your choice: 1
# 1    Jason Lee        555-1212
# 2    Amanda Green     555-0101
# 3    Jenna Jacobs     555-9090
# 4    Alfredo Greer    555-1234
# 5    Jules Landis     555-2345
# 6    John Doe         123-4567
#
#
#                      Menu
# --------------------------------------------------
# 1 - Display All
# 2 - Create a New Phonebook Entry
# 3 - Read a Phonebook Entry
# 4 - Update a Phonebook Entry
# 5 - Delete a Phonebook Entry
# 6 - Exit
# Enter your choice: 2
# Name: John Doe
# Phone Number: 123-4567
# New Entry Added
#
#
#                      Menu
# --------------------------------------------------
# 1 - Display All
# 2 - Create a New Phonebook Entry
# 3 - Read a Phonebook Entry
# 4 - Update a Phonebook Entry
# 5 - Delete a Phonebook Entry
# 6 - Exit
# Enter your choice: 3
# Name to search for: Jason Lee
# Jason Lee        555-1212
#
#
#                      Menu
# --------------------------------------------------
# 1 - Display All
# 2 - Create a New Phonebook Entry
# 3 - Read a Phonebook Entry
# 4 - Update a Phonebook Entry
# 5 - Delete a Phonebook Entry
# 6 - Exit
# Enter your choice: 4
# Name to search for: Jason Lee
# ID  Name            Phone
# 1    Jason Lee        555-1212
# Enter the ID of the entry you wish to update: 1
# Enter the new name: Janet Doe
# Enter the new phone: 765-4321
# Entry Updated.
#
#
#                      Menu
# --------------------------------------------------
# 1 - Display All
# 2 - Create a New Phonebook Entry
# 3 - Read a Phonebook Entry
# 4 - Update a Phonebook Entry
# 5 - Delete a Phonebook Entry
# 6 - Exit
# Enter your choice: 5
# Name to search for: Jason
# Item is not in database.
#
#
#                      Menu
# --------------------------------------------------
# 1 - Display All
# 2 - Create a New Phonebook Entry
# 3 - Read a Phonebook Entry
# 4 - Update a Phonebook Entry
# 5 - Delete a Phonebook Entry
# 6 - Exit
# Enter your choice: 5
# Name to search for: John Doe
# ID   Name             Phone Number
# 6    John Doe         123-4567
# 7    John Doe         123-4567
# Enter the ID of the entry you wish to delete: 7
# Are you sure? (y/n)y
# Entry Deleted.
#
#
#                      Menu
# --------------------------------------------------
# 1 - Display All
# 2 - Create a New Phonebook Entry
# 3 - Read a Phonebook Entry
# 4 - Update a Phonebook Entry
# 5 - Delete a Phonebook Entry
# 6 - Exit
# Enter your choice: 6
#****************************************************************************************************

