import sys

from config import db
from models import create_db_tables
from records import add_csv_to_db
from outputs import plot_histograms
from test import test_create_db_and_record


if __name__ == '__main__':
    db.connect()

    if 'createtables' in sys.argv:
        create_db_tables()
    if 'test' in sys.argv:
        test_create_db_and_record()
    if 'csv' in sys.argv:
        idx = sys.argv.index('csv')
        filename = sys.argv[idx+1]
        add_csv_to_db(filename)
    if 'hist' in sys.argv:
        plot_histograms()

    db.close()
