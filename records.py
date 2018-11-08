import csv
import peewee as pw

from models import Brand, SubBrand, Range, Model, Guitar, create_db_tables


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
