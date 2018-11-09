import platform

import peewee as pw

from config import db
from models import Brand, SubBrand, Range, Model, Guitar

# if on Mac us TkAgg backend for matplotlib
if platform.system() == 'Darwin':
    import matplotlib as mpl
    mpl.use('TkAgg')
import matplotlib.pyplot as plt


def view_guitars():
    guitars = Guitar.select()
    separator_line = '-'*8*11
    print(separator_line)
    print(f"{'Brand':7.7s}\t"
          f"{'SubBrand':15.15s}\t"
          f"{'Range':15.15s}\t"
          f"{'Model':15.15s}\t"
          f"{'Variant':15.15s}\t"
          f"{'Year':7.7s}\t"
          f"{'Price':7.7s}\t"
    )
    print(separator_line)
    for i, guitar in enumerate(guitars):
        if i == 999: # 999 is max SQLite query return size
            break
        print(f'{guitar.brand.name:7.7s}\t'
              f'{guitar.sub_brand.name:15.15s}\t'
              f'{guitar.range_name.name:15.15s}\t'
              f'{guitar.model.name:15.15s}\t'
              f'{guitar.variant:15.15s}\t'
              f'{guitar.year}\t'
              f'{guitar.price:8.2f}'
        )
    print(separator_line)


def plot_histograms():
    pass
