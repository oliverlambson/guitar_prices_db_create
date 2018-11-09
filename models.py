import peewee as pw

from config import db


class BaseModel(pw.Model):
    class Meta:
        database = db


class Brand(BaseModel):
    name = pw.CharField(unique=True)

    def __str__(self):
        return f'Brand: {self.name}'


class SubBrand(BaseModel):
    name = pw.CharField()
    brand = pw.ForeignKeyField(Brand, backref='sub_brands')

    def __str__(self):
        return f'SubBrand: {self.name} - of Brand: {self.brand.name}'


class Range(BaseModel):
    name = pw.CharField()
    brand = pw.ForeignKeyField(Brand, backref='ranges')

    def __str__(self):
        return f'Range: {self.name} - of Brand: {self.brand.name}'


class Model(BaseModel):
    name = pw.CharField()
    brand = pw.ForeignKeyField(Brand, backref='models')

    def __str__(self):
        return f'Model: {self.name} - of Brand: {self.brand.name}'


class Guitar(BaseModel):
    variant = pw.CharField(null=True)
    year = pw.SmallIntegerField()
    price = pw.DecimalField(decimal_places=2)
    brand = pw.ForeignKeyField(Brand, backref='brands')
    sub_brand = pw.ForeignKeyField(SubBrand, backref='sub_brands')
    range_name = pw.ForeignKeyField(Range, backref='ranges')
    model = pw.ForeignKeyField(Model, backref='models')

    def __str__(self):
        return f'Guitar: {self.brand.name} {self.sub_brand.name} {self.range_name.name} {self.model.name} {self.variant} {self.year} ${self.price}'


def create_db_tables():
    db.create_tables([Brand, SubBrand, Range, Model, Guitar])
