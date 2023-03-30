import sqlite3

class Database:
    def __init__(self, database_file_path, table_name, fields):
        self.database_file_path = database_file_path
        self.table_name = table_name
        self.fields = fields
        self.connection = sqlite3.connect(database_file_path)
        self.cursor = self.connection.cursor()


        column_names = [field['field_name'] for field in fields]
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, {', '.join(column_names)})"
        self.cursor.execute(create_table_sql)

    def add_data(self, data):
        column_names = [field['field_name'] for field in self.fields]
        values = tuple(data[column_name] for column_name in column_names)
        insert_sql = f"INSERT INTO {self.table_name} ({', '.join(column_names)}) VALUES ({', '.join(['?']*len(column_names))})"
        self.cursor.execute(insert_sql, values)
        self.connection.commit()

    def close(self):
        self.connection.close()