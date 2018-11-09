import peewee as pw

db = pw.SqliteDatabase('competitors.db', pragmas={'foreign_keys': 1}) # pragmas={'foreign_keys': 1} enables foreign key constraints in SQLite
