#!/usr/bin/env python3
import pandas as pd
import sqlite3
import sys
from argparse import ArgumentParser

if __name__ == '__main__':

    parser = ArgumentParser(description="Convert CSV files to SQLite tables.")

    parser.add_argument("-d",
                        dest     = "database",
                        required = True,
                        help     = "SQLite Database File.",
                        type     = str)

    parser.add_argument("-c",
                        dest     = "csv",
                        required = True,
                        help     = "CSV File.",
                        type     = str)

    parser.add_argument("-t",
                        dest     = "table",
                        required = True,
                        help     = "SQLite Database Table.",
                        type     = str)

    parser.add_argument("-i",
                        dest     = "if_exists",
                        required = True,
                        choices  = ['append','replace','fail'],
                        help     = "What to do if table exists.",
                        type     = str)

    parser.add_argument("-q",
                        dest     = "quotechar",
                        required = False,
                        default  = '"',
                        help     = "CSV quote char.",
                        type     = str)

    parser.add_argument("-s",
                        dest     = "separator",
                        required = False,
                        default  = ',',
                        help     = "CSV separator char.",
                        type     = str)

    args = parser.parse_args()

    try:
        csv_data = pd.read_csv(args.csv,quotechar=args.quotechar,sep=args.separator)
    except Exception as ex:
        print(str(ex),file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(args.database)
    cur  = conn.cursor()

    try:
        csv_data.to_sql(args.table,
                        conn,
                        if_exists = args.if_exists,
                        index     = False,
                        chunksize = 50000)
    except Exception as ex:
        print(str(ex),file=sys.stderr)
        sys.exit(1)
