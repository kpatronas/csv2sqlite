# csv2sqlite
Simple CSV to SQLite converter

## Usage
Minimal usage example
```
csv2sqlite.py -d mydatabase.db -c ./mycsv.csv -t mytable -i replace
```
-d DATABASE: SQLite Database (required)
-c CSV: The CSV file to convert (required)
-t TABLE: The SQLite Database table to be used (required)
-i {append,replace,fail}: append, appends to the table if data exist, replace drops the table before insertion, fail exits if table exists (required)
[-q QUOTECHAR]: CSV quote character, defaults to "
[-s SEPARATOR]: CSV field separator character, defaults to ,
