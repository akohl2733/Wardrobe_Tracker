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


while True:
    res = input('Do you want to search by brand?\nReturn y/n...')
    if res == 'n':
        clothing_item = input('What type of clothing item would you like to search? (Press enter to skip)\n')
        color_choice = input('What color of clothing do you want to check on? (Press enter to skip)\n')
        brand_choice = ''
        break
    elif res == 'y':
        brand_choice = input('Which brand are we searching by?\n')
        clothing_item = input('What type of clothing item would you like to search? (Press enter to skip)\n')
        color_choice = input('What color of clothing do you want to check on? (Press enter to skip)\n')
        break
    else:
        print('please enter a legit value\n')

c.execute(f"""SELECT rowid, * from clothing WHERE item_type LIKE '%{clothing_item}%'
          AND color LIKE '%{color_choice}%'
          AND brand LIKE '%{brand_choice}%'
          ORDER BY item_type DESC, size""")

items = c.fetchall()
total_cost = 0
if len(items) == 0:
    print('\nYou got nothing my man!')
else:
    print(f'\n\n{color_choice} {clothing_item}')
    print('_____________________________________')
    for item in items:
        total_cost = total_cost + int(item[-1])
        print('{0} -- You have "{1}" by {2} at size {3}'.format(item[1], item[2], item[4], item[3]))
    print()
    print('len items:  ' + str(len(items)))
    print('total price of items:  ' + str(total_cost))
    print('\n')

conn.commit()
conn.close()
