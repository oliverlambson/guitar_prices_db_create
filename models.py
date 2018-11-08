import peewee as pw

from config import db


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
