#****************************************************************************************************
#
#       Name:         Alex Orescanin
#       Course:       COSC 2110 Computer Languages: Python
#       Assignment:   create_phonebook_db.py
#       Due Date:     11/27/2020
#       Description:
#               This program will create a database named phonebook
#
#****************************************************************************************************

import sqlite3

def create_phonebook_db():

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    cur.execute('''DROP TABLE IF EXISTS Entries''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Entries (EntryID INTEGER PRIMARY KEY NOT NULL,
                    Name TEXT, Phone TEXT)''')
    cur.execute('''INSERT INTO Entries (EntryID, Name, Phone)
                   VALUES(?, 'Jason Lee', '555-1212')''')
    cur.execute('''INSERT INTO Entries (EntryID, Name, Phone)
                   VALUES(?, 'Amanda Green', '555-0101')''')
    cur.execute('''INSERT INTO Entries (EntryID, Name, Phone)
                   VALUES(?, 'Jenna Jacobs', '555-9090')''')
    cur.execute('''INSERT INTO Entries (EntryID, Name, Phone)
                   VALUES(?, 'Alfredo Greer', '555-1234')''')
    cur.execute('''INSERT INTO Entries (EntryID, Name, Phone)
                   VALUES(?, 'Jules Landis', '555-2345')''')

    conn.commit()
    conn.close()

    display_entries()

#****************************************************************************************************

def display_entries():
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

if __name__ == 'create_phonebook_db':
    create_phonebook_db()