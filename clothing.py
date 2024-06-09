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

c.execute("""SELECT rowid, * from clothing WHERE item_type LIKE '%pants%' 
          AND description NOT LIKE '%sweat%' 
          AND description NOT LIKE '%jeans%'
          ORDER BY years_old DESC""")

items = c.fetchall()
total_cost = 0
for item in items:
    total_cost = total_cost + int(item[-1])
    print(item)
print(total_cost)

conn.commit()
conn.close()
