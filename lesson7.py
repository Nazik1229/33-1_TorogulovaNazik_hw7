import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print('Ошибка при подключении')
    return conn


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_product(connection, product):
    sql = '''INSERT INTO products
    (product_tittle, price, quantity)
    VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_product_quantity(connection, id, new_quantity):
    sql = '''UPDATE products
    SET quantity = ?
    WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (new_quantity, id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_product_price(connetcion, id, new_price):
    sql = '''UPDATE products
    SET pricev= ?
    WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (new_price, id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(connection, id):
    sql = '''DELETE FROM products
    WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(connection):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_of_cheap_product(connection):
    sql = '''SELECT * FROM products
    WHERE price < 100 AND quantity > 5'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def search_product_by_tittle(connection, search):
    sql = '''SELECT * FROM products
    WHERE product_title LIKE ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, ('%' + search + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


sql_to_creat_products_table = '''
CREAT TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price FLOAT(10, 2) NOT NULL DEFAULT 0.02,
quantity INTEGER NOT NULL DEFAULT 0
)
'''


connection = create_connection('''hw.db''')
if connection is not None:
    print("Успешное подключение")
    # create_table(connection, sql_to_creat_products_table)
    # insert_product(connection,
    #                ('Жидкое мыло дря рук', 84, 15))
    # insert_product(connection,
    #                ('Детское мыло', 50, 20))
    # insert_product(connection,
    #                ('Горький шоколад', 90, 25))
    # insert_product(connection,
    #                ('Молочный шоколад', 83, 25))
    # insert_product(connection,
    #                ('Крем для рук', 120, 10))
    # insert_product(connection,
    #                ('Крем для лица', 197, 10))
    # insert_product(connection,
    #                ('Попкорн', 54, 7))
    # insert_product(connection,
    #                ('Зубная щетка', 290, 12))
    # insert_product(connection,
    #                ('Зубная паста', 250, 15))
    # insert_product(connection,
    #                ('Зубная нить', 236, 5))
    # insert_product(connection,
    #                ('Маска для лица', 150, 5))
    # insert_product(connection,
    #                ('Маска для сна', 300, 15))
    # insert_product(connection,
    #                ('Туалетная бумага', 12, 100))
    # insert_product(connection,
    #                ('Бумага А4', 350, 10))
    # insert_product(connection,
    #                ('Хлеб', 25, 90))

    # select_all_products(connection)
    # select_of_cheap_product(connection)
    # update_product_price(connection, 4, 90)
    # update_product_quantity(connection, 4, 20)
    # delete_product(connection, 3)

    connection.close()
