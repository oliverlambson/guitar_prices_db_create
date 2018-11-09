import platform

import numpy as np

from models import Brand, SubBrand, Range, Model, Guitar, create_db_tables

# if on Mac us TkAgg backend for matplotlib
if platform.system() == 'Darwin':
    import matplotlib as mpl
    mpl.use('TkAgg')
import matplotlib.pyplot as plt


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

def test_matplotlib_working():
    x = np.linspace(0,10,1000)
    y = x**2
    plt.plot(x,y)
    plt.title('Test plot')
    plt.show()
