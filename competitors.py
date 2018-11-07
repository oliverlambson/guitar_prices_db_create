import sys

import peewee as pw


db = pw.SqliteDatabase('competitors.db')


class BaseModel(pw.Model):
    class Meta:
        database = db


class Brand(BaseModel):
    name = pw.CharField(unique=True)


class SubBrand(BaseModel):
    name = pw.CharField()
    brand = pw.ForeignKeyField(Brand, backref='sub_brands')


class Range(BaseModel):
    name = pw.CharField()
    brand = pw.ForeignKeyField(Brand, backref='ranges')


class Model(BaseModel):
    name = pw.CharField()
    brand = pw.ForeignKeyField(Brand, backref='models')


class Guitar(BaseModel):
    variant = pw.CharField(null=True)
    year = pw.SmallIntegerField()
    price = pw.DecimalField(decimal_places=2)
    brand = pw.ForeignKeyField(Brand, backref='brands')
    sub_brand = pw.ForeignKeyField(SubBrand, backref='sub_brands')
    range_name = pw.ForeignKeyField(Range, backref='ranges')
    model = pw.ForeignKeyField(Model, backref='models')


def create_db_tables():
    db.create_tables([Brand, SubBrand, Range, Model, Guitar])


def test():
    create_db_tables()
    brand = Brand.create(name='Gibson')
    sub_brand = SubBrand.create(name='USA', brand=brand)
    range_name = Range.create(name='Les Paul', brand=brand)
    model = Model.create(name='Standard', brand=brand)
    guitar = Guitar.create(
        variant='var1',
        year=2018,
        price=3399,
        brand=brand,
        sub_brand=sub_brand,
        range_name=range_name,
        model=model
    )


if __name__ == '__main__':
    db.connect()
    if 'createtables' in sys.argv:
        create_db_tables()
    if 'test' in sys.argv:
        test()
    db.close()
