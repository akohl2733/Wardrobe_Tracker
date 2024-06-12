import sqlite3


def how_describe():

    while True:
        descrip_choice = input('How you would describe this clothing? (Press enter for any)\n').lower()
        if descrip_choice == '':
            return descrip_choice
        c.execute(f"SELECT * FROM clothing WHERE description LIKE '%{descrip_choice}%'")
        results = c.fetchall()
        if len(results) < 1:
            print('\nUnfortunately there is nothing described like that, please enter something else...\nIf you wish to bypass this, please press enter\n')
        else:
            return descrip_choice

def which_clothing_item():
    while True:
        clothing_item = input('Which type of clothing item is this? (Press enter for any)\n').lower()
        if clothing_item == '':
            return clothing_item
        c.execute(f"SELECT * FROM clothing WHERE item_type LIKE '%{clothing_item}%'")
        results = c.fetchall()
        if len(results) < 1:
            print('\nUnfortunately there is nothing described like that, please enter something else...\nIf you wish to bypass this, please press enter\n')
        else:
            return clothing_item

def coloring():
    while True:
        color_choice = input('What color is this clothing? (Press enter for any)\n').lower()
        if color_choice == '':
            return color_choice
        c.execute(f"SELECT * FROM clothing WHERE color LIKE '%{color_choice}%'")
        results = c.fetchall()
        if len(results) < 1:
            print('\nUnfortunately there is nothing with that color, please enter something else...\nIf you wish to bypass this, please press enter\n')
        else:
            return color_choice
        
def branding():
    while True:
        brand_choice = input('Which brand are we looking for? (Press enter for any)\n').lower()
        if brand_choice == '':
            return brand_choice
        c.execute(f"SELECT * FROM clothing WHERE brand LIKE '%{brand_choice}%'")
        results = c.fetchall()
        if len(results) < 1:
            print('\nUnfortunately there is nothing branded like that, please enter something else...\nIf you wish to bypass this, please press enter\n')
        else:
            return brand_choice