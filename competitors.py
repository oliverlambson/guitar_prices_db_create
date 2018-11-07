import sys

import peewee as pw


db = pw.SqliteDatabase('competitors.db')


class BaseModel(pw.Model):
    class Meta:
        database = db


class Brand(BaseModel):
    name = pw.CharField()


# class SubBrand(BaseModel):
#     brand_name = pw.ForeignKeyField(Brand, backref='name')
#     name = pw.CharField()
#
#
# class Range(BaseModel):
#     brand_name = pw.ForeignKeyField(Brand, backref='name')
#     name = pw.CharField()
#
#
# class Model(BaseModel):
#     brand_name = pw.ForeignKeyField(Brand, backref='name')
#     name = pw.CharField()
#
#
# class Guitar(BaseModel):
#     brand_name = pw.ForeignKeyField(Brand, backref='name')
#     sub_brand_name = pw.ForeignKeyField(SubBrand, backref='name')
#     range_name = pw.ForeignKeyField(Range, backref='name')
#     model_name = pw.ForeignKeyField(Model, backref='name')
#     variant = pw.CharField(null=True)
#     year = pw.SmallIntegerField()
#     price = pw.DecimalField(decimal_places=2)


def create_db_tables():
    db.create_tables([Brand])
    # db.create_tables([Brand, SubBrand])


def test():
    create_db_tables()
    Brand.create(name='gibson')


if __name__ == '__main__':
    db.connect()
    if 'createtables' in sys.argv:
        create_db_tables()
    if 'test' in sys.argv:
        test()
    db.close()
