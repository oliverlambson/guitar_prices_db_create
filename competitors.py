import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create database connection to SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    """ create table in database using SQL statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    return None


def create_brand(conn, brand):
    """ create new brand record in brands table """
    sql = """ INSERT INTO brands (brand_name)
                VALUES (?) """
    cur = conn.cursor()
    cur.execute(sql, brand)
    conn.commit()
    return None


def create_sub_brand(conn, sub_brand):
    """ create new sub_brand record in sub_brands table """
    sql = """ INSERT INTO sub_brands (brand_name, sub_brand_name,
                          manufacture_loc, component_type)
                VALUES (?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, sub_brand)
    conn.commit()
    return None


def create_range(conn, range_record):
    """ create new range record in ranges table """
    sql = """ INSERT INTO ranges (brand_name, range_name)
                VALUES (?,?) """
    cur = conn.cursor()
    cur.execute(sql, range_record)
    conn.commit()
    return None


def create_model(conn, model):
    """ create new model record in models table """
    sql = """ INSERT INTO models (brand_name, range_name, model_name)
                VALUES (?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, model)
    conn.commit()
    return None


def create_price(conn, price):
    """ create new price record in prices table """
    sql = """ INSERT INTO prices (brand_name, range_name, model_name,
                          variant_name, price)
                VALUES (?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, price)
    conn.commit()
    return None


def main():
    # --- consts ---------------------------------------------------------------
    db_path = "competitors.db"
    sql_brands = """ CREATE TABLE IF NOT EXISTS brands (
                        id integer PRIMARY KEY,
                        brand_name text NOT NULL
                     ); """

    sql_sub_brands = """ CREATE TABLE IF NOT EXISTS sub_brands (
                            id integer PRIMARY KEY,
                            brand_name text NOT NULL,
                            sub_brand_name text NOT NULL,
                            manufacture_loc text,
                            component_type text,
                            FOREIGN KEY (brand_name) REFERENCES brands (brand_name)
                         ); """

    sql_ranges = """ CREATE TABLE IF NOT EXISTS ranges (
                        id integer PRIMARY KEY,
                        brand_name text NOT NULL,
                        range_name text NOT NULL,
                        FOREIGN KEY (brand_name) REFERENCES brands (brand_name)
                     ); """

    sql_models = """ CREATE TABLE IF NOT EXISTS models (
                        id integer PRIMARY KEY,
                        brand_name text NOT NULL,
                        range_name text NOT NULL,
                        model_name text NOT NULL,
                        FOREIGN KEY (brand_name) REFERENCES brands (brand_name),
                        FOREIGN KEY (range_name) REFERENCES ranges (range_name)
                     ); """

    sql_prices = """ CREATE TABLE IF NOT EXISTS prices (
                        id integer PRIMARY KEY,
                        brand_name text NOT NULL,
                        range_name text NOT NULL,
                        model_name text NOT NULL,
                        variant_name text,
                        price real NOT NULL,
                        FOREIGN KEY (brand_name) REFERENCES brands (brand_name),
                        FOREIGN KEY (range_name) REFERENCES ranges (range_name),
                        FOREIGN KEY (model_name) REFERENCES models (model_name)
                     ); """

    # --- execution ------------------------------------------------------------
    # create database
    conn = create_connection(db_path)
    if conn is not None:
        # create tables
        create_table(conn, sql_brands)
        create_table(conn, sql_sub_brands)
        create_table(conn, sql_ranges)
        create_table(conn, sql_models)
        create_table(conn, sql_prices)

        # create records
        create_brand(conn, ("PRS",))
        create_sub_brand(conn, ('PRS', 'Core', 'USA', 'Premium'))
        create_range(conn, ('PRS', 'Custom'))
        create_model(conn, ('PRS', 'Custom' ,'Custom 24'))
        create_price(conn, ('PRS', 'Custom', 'Custom 24', 'Piezo', 3800))
    else:
        print("Database connection unsuccessful.")

    conn.close()
    

if __name__ == "__main__":
    main()
