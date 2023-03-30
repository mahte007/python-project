import yaml
import json
import sqlite3

def load_yaml(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
        return data
    
def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f)

def save_data_to_db(file_path, table_name, fields, data_list):

    connection = sqlite3.connect(file_path)
    cursor = connection.cursor()
    column_names = [field["field_name"] for field in fields]
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, {', '.join(column_names)})"
    cursor.execute(create_table_sql)

    for data in data_list:
        values = tuple(data[column_name] for column_name in column_names)
        insert_sql = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(['?']*len(column_names))})"
        cursor.execute(insert_sql, values)

    connection.commit()
    connection.close()

