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