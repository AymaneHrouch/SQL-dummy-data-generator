# SQL-dummy-data-generator
This is a very simple dummy data generator for SQL, it will generate as many rows you want.
You have to enter three variables
1. **n (optional)**: number of desired rows, 10 if omitted.
2. **table name**
3. . **data**: Structure of data should be 'column1 datatype1, column2 datatype2, ...'

### Supported datatypes
* **int**: generate random integer
* **float**: generate random float between 0 and 100
* **varchar**: generate random word containing characters between 5 and 10

The script will print the SQL commands and copy them to the clipboard so you can easily paste them in sqlplus or whatever plateform are you using to insert your data.
