from models import Brand, SubBrand, Range, Model, Guitar, create_db_tables


def test_create_db_and_record():
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
