import sqlite3


def connectWithDB():
    connectUrl = '/Users/kamillatitova/sqlite'
    connection = sqlite3.connect(connectUrl)
    cursor = connection.cursor()
    return cursor


def sendRequest(cursor, sql):
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return result


# def getAllTables(cursor):
#     cursor.execute('Select name From sqlite_master WHERE type="table"')
#     tablesBuf = cursor.fetchall()
#     tables = []
#     for table in tablesBuf:
#         tables.append(table[0])
#     return tables

def getAllData(cursor):
    cursor.execute('select scripts.script_text from scripts where author="164098"')
    DataBuff = cursor.fetchall()
    data_tables = []
    for data_table in DataBuff:
        print(data_table)
    return data_tables


if __name__ == '__main__':
    cursor = connectWithDB()

    # sendRequest(cursor, 'Select * from users')
    # tables = getAllTables(cursor)
    datas = getAllData(cursor)
    # print(tables)
    print(datas)