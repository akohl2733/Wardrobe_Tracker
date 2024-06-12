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

def tester(type, column, x):
    while True:
        x = input(f'What is this piece of clothing\'s {type}? (Press enter for any)\n').lower()
        if x == '':
            return x
        c.execute(f"SELECT * FROM clothing WHERE {column} LIKE '%{x}%'")
        results = c.fetchall()
        if len(results) < 1:
            print('\nUnfortunately there is nothing described like that, please enter something else...\nIf you wish to bypass this, please press enter\n')
        else:
            return x




while True:
    res = input('Do you want to search by brand?\nReturn y/n...').lower()
    if res == 'n':
        clothing_item, color_choice, descrip_choice, brand_choice = None, None, None, None
        clothing_item, color_choice, descrip_choice, brand_choice = tester('type', 'item_type', clothing_item), tester('color', 'color', color_choice), tester('description', 'description', descrip_choice), ''
        break
    elif res == 'y':
        clothing_item, color_choice, descrip_choice, brand_choice = None, None, None, None
        brand_choice, clothing_item, color_choice, descrip_choice = tester('brand', 'brand', brand_choice), tester('type', 'item_type', clothing_item), tester('color', 'color', color_choice), tester('description', 'description', descrip_choice)
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