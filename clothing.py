import sqlite3
from items import clothing_items

conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE clothing (
        item_type text NOT NULL,
        description text,
        size text,
        brand text,
        color text NOT NULL,
        years_old integer,
        price integer
)""")

c.executemany("INSERT INTO clothing VALUES (?, ?, ?, ?, ?, ?, ?)", (clothing_items))

def tester(type, x):
    while True:
        x = input(f'{type} clothing? (Press enter for any)\n').lower()
        if x == '':
            return x
        c.execute(f"SELECT * FROM clothing WHERE description LIKE '%{x}%'")
        results = c.fetchall()
        if len(results) < 1:
            print('\nUnfortunately there is nothing described like that, please enter something else...\nIf you wish to bypass this, please press enter\n')
        else:
            return x


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




while True:
    res = input('Do you want to search by brand?\nReturn y/n...').lower()
    if res == 'n':
        clothing_item, color_choice, descrip_choice, brand_choice = None, None, None, None
        clothing_item, color_choice, descrip_choice, brand_choice = tester('Article of', clothing_item), tester('Color of', color_choice), tester('Description of', descrip_choice), ''
        break
    elif res == 'y':
        brand_choice, clothing_item, color_choice, descrip_choice = branding(), which_clothing_item(), coloring(), how_describe()
        break
    else:
        print('Please type either "y" or "n"')

c.execute(f"""SELECT rowid, * from clothing WHERE item_type LIKE '%{clothing_item}%'
          AND color LIKE '%{color_choice}%'
          AND brand LIKE '%{brand_choice}%'
          AND description LIKE '%{descrip_choice}%'
          ORDER BY item_type DESC, size""")

items = c.fetchall()
if len(items) == 0:
    print('\nYou got nothing my man!')
else:
    print(f'\n\n{color_choice} {clothing_item}')
    print('_____________________________________')
    for item in items:
        print('{0} -- You have "{1}" by {2} at size {3}'.format(item[1], item[2], item[4], item[3]))
    print()
    print('len items:  ' + str(len(items)))
    print('\n')

conn.commit()
conn.close()


# brand_choice = input('Which brand are we searching by?\n').lower()
# c.execute(f"SELECT * FROM clothing WHERE brand LIKE '%{brand_choice}%'")
# results = c.fetchall()
# if len(results) < 1:
#     raise ValueError
# else:
#     print('You have some items from {0} here...\n'.format(results[0][3]))
# clothing_item, color_choice = choices()
# break