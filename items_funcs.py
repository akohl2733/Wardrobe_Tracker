import sqlite3

def how_describe():
    while True:
        descrip_choice = input('How you would describe this clothing? (Press enter for any)\n').lower()
        if descrip_choice == '':
            break
        c.execute(f"SELECT * FROM clothing WHERE description LIKE '%{descrip_choice}%'")
        results = c.fetchall()
        if len(results) < 1:
            print('\nUnfortunately there is nothing described like that, please enter something else...\nIf you wish to bypass this, please press enter\n')
        else:
            break

def which_clothing_item():
    while True:
        clothing_item = input('Which type of clothing item is this? (Press enter for any)\n').lower()
        if clothing_item == '':
            break
        c.execute(f"SELECT * FROM clothing WHERE description LIKE '%{clothing_item}%'")
        results = c.fetchall()
        if len(results) < 1:
            print('\nUnfortunately there is nothing described like that, please enter something else...\nIf you wish to bypass this, please press enter\n')
        else:
            break