import sqlite3
import yaml


try:

    yml_file = "../Config/conig.yml"
    with open(yml_file, "r") as f:
        data = yaml.safe_load(f)

    fields = data['fields']

    jsonFilePath = data['output_file']
    dataBaseFilePath = data['data_file']
    tableName = data['table_name']


    connection = sqlite3.connect(dataBaseFilePath)
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {tableName}")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()

except:
    print("File not found!")