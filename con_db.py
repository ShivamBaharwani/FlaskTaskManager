import MySQLdb as connector
mydb = connector.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='1234'
)
my_cursor = mydb.cursor()
my_cursor.execute("create database if not exists todo")
my_cursor.execute('use todo')
my_cursor.execute('create table if not exists todo_table(title varchar(200), description varchar(2000))')

# list all databases
my_cursor.execute('Show databases')
print('Databases:')
for db in my_cursor:
    print(db[0])

#print the table
my_cursor.execute('use todo')
my_cursor.execute('Select * from todo_table')
print('\ntodo table contents:')
for row in my_cursor:
    print(f'title: {row[0]}, description: {row[1]}')

# close the cursor and connection
my_cursor.close()
mydb.close()