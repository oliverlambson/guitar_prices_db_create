import sys
import csv

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

    gibson = Brand.create(name='Gibson')
    usa = SubBrand.create(name='USA', brand=gibson)
    les_paul = Range.create(name='Les Paul', brand=gibson)
    standard = Model.create(name='Standard', brand=gibson)
    guitar = Guitar.create(
        variant=None,
        year=2018,
        price=3399,
        brand=gibson,
        sub_brand=usa,
        range_name=les_paul,
        model=standard
    )

def add_csv_to_db(filename):
    with open(filename) as csv_file:
        csv_rows = csv.reader(csv_file, delimiter=';')
        i = 0
        types_ok = True
        for row in csv_rows:
            (
                arg_brand,
                arg_sub_brand,
                arg_range_name,
                arg_model,
                arg_variant,
                arg_year,
                arg_price
            ) = row

            try:
                arg_year = int(arg_year)
                arg_price = float(arg_price)
                # print(
                #     f"{arg_brand} {arg_sub_brand} {arg_range_name} "
                #     f"{arg_model} {arg_variant} {arg_year} ${arg_price:.2f}"
                # )
            except ValueError:
                types_ok = False
                print("!! type not ok")

            if types_ok:
                brand, new_brand = Brand.get_or_create(
                    name=arg_brand
                )
                sub_brand, new_sub_brand = SubBrand.get_or_create(
                    name=arg_sub_brand,
                    brand=brand
                )
                range_name, new_range = Range.get_or_create(
                    name=arg_range_name,
                    brand=brand
                )
                model, new_model = Model.get_or_create(
                    name=arg_model,
                    brand=brand
                )
                guitar, new_guitar = Guitar.get_or_create(
                    variant=arg_variant,
                    year=arg_year,
                    price=arg_price,
                    brand=brand,
                    sub_brand=sub_brand,
                    range_name=range_name,
                    model=model
                )

                if new_brand:
                    print(f"Brand added:     {brand.name}")
                if new_sub_brand:
                    print(f"Sub-brand added: {sub_brand.name}")
                if new_range:
                    print(f"Range added:     {range_name.name}")
                if new_model:
                    print(f"Model added:     {model.name}")
                if new_guitar:
                    print(f"Guitar added:    {brand.name} {sub_brand.name} "
                          f"{range_name.name} {model.name} {arg_variant} "
                          f"{arg_year} ${arg_price:.2f}")


if __name__ == '__main__':
    db.connect()
    if 'createtables' in sys.argv:
        create_db_tables()
    if 'test' in sys.argv:
        test()
    if 'csv' in sys.argv:
        idx = sys.argv.index('csv')
        filename = sys.argv[idx+1]
        add_csv_to_db(filename)

    db.close()
