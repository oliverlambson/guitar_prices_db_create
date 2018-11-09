import sys

from config import db
from models import create_db_tables
from records import add_csv_to_db
from outputs import view_guitars, plot_histograms
from test import test_create_db_and_record, test_matplotlib_working


if __name__ == '__main__':
    db.connect()

    # functionality
    if 'createtables' in sys.argv:
        create_db_tables()
    if 'csv' in sys.argv:
        idx = sys.argv.index('csv')
        filename = sys.argv[idx+1]
        add_csv_to_db(filename)
    if 'viewguitars' in sys.argv:
        view_guitars()
    if 'hist' in sys.argv:
        plot_histograms()

    # tests
    if 'test_create_db_and_record' in sys.argv:
        test_create_db_and_record()
    if 'test_matplotlib_working' in sys.argv:
        test_matplotlib_working()

    db.close()
