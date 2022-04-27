import argparse, peewee, random as rd, datetime, sys

db =  peewee.SqliteDatabase("db/db.db")
class BaseModel(peewee.Model):
    class Meta:
        database = db

class clients(BaseModel):
    name = peewee.CharField()
    city = peewee.CharField()
    address = peewee.CharField()
    

class orders(BaseModel):
    client = peewee.ForeignKeyField(clients)
    date = peewee.DateField()
    amount = peewee.IntegerField()
    description = peewee.CharField()
   

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--init', action='store_const', const=True, help='Создание таблиц в базе данных')
    parser.add_argument('-f', '--fill', action='store_const', const=True, help='Заполнение таблиц данными')
    parser.add_argument('-s', '--show', action='store', metavar='tablename', help = 'Вывод данных из указанной таблицы')
    return parser

def NewTables():
    print('Creating new tables...')
    clients.create_table()
    orders.create_table()
    print('Done!')

def initing():
    table_list = db.get_tables()
    if table_list == []:
        NewTables()
    else:
        print('Dropping all tables...')
        db.drop_tables((clients, orders))
        NewTables()

def filling():
    clients_data = [
        {"name":'client_1', "city": 'city_1', "address": 'address_1'},
        {"name":'client_2', "city": 'city_2', "address": 'address_2'},
        {"name":'client_3', "city": 'city_3', "address": 'address_3'},
        {"name":'client_4', "city": 'city_4', "address": 'address_4'},
        {"name":'client_5', "city": 'city_5', "address": 'address_5'},
        {"name":'client_6', "city": 'city_6', "address": 'address_6'},
        {"name":'client_7', "city": 'city_7', "address": 'address_7'},
        {"name":'client_8', "city": 'city_8', "address": 'address_8'},
        {"name":'client_9', "city": 'city_9', "address": 'address_9'},
        {"name":'client_10', "city": 'city_10', "address": 'address_10'}
    ]
    orders_data = [
        {"client": 1, "date": datetime.date(rd.randint(1980,2020),rd.randint(1,12),15), "amount":7, "description": 'blablabla'},
        {"client": 2, "date": datetime.date(rd.randint(1980,2020),rd.randint(1,12),15), "amount":7, "description": 'blablabla'},
        {"client": 3, "date": datetime.date(rd.randint(1980,2020),rd.randint(1,12),15), "amount":7, "description": 'blablabla'},
        {"client": 4, "date": datetime.date(rd.randint(1980,2020),rd.randint(1,12),15), "amount":7, "description": 'blablabla'},
        {"client": 5, "date": datetime.date(rd.randint(1980,2020),rd.randint(1,12),15), "amount":7, "description": 'blablabla'},
        {"client": 6, "date": datetime.date(rd.randint(1980,2020),rd.randint(1,12),15), "amount":7, "description": 'blablabla'},
        {"client": 7, "date": datetime.date(rd.randint(1980,2020),rd.randint(1,12),15), "amount":7, "description": 'blablabla'},
        {"client": 8, "date": datetime.date(rd.randint(1980,2020),rd.randint(1,12),15), "amount":7, "description": 'blablabla'},
        {"client": 9, "date": datetime.date(rd.randint(1980,2020),rd.randint(1,12),15), "amount":7, "description": 'blablabla'},
        {"client": 10, "date":datetime.date(rd.randint(1980,2020),rd.randint(1,12),15), "amount":7, "description": 'blablabla'}
    ]
    print('Addind data...')
    query = clients.insert_many(clients_data)
    query.execute(database= None)
    query = orders.insert_many(orders_data)
    query.execute(database= None)
    print('Done') 
    



if __name__ == '__main__':

    parser = createParser()
    namespace = parser.parse_args()
 
    
    if namespace.init:
        initing()


    if namespace.fill:
        filling()
        

    if namespace.show != None:
        if db.table_exists(namespace.show):
            model = locals()[namespace.show]
            query = model.select()
            cols = db.get_columns(namespace.show)
            for col in cols:
                print(col.name, end='   ')
            for row in query:
                print('\n')
                for col in cols:
                    string = 'print(row.' + col.name +', end =  "    ")'  
                    exec(string)
        else:
            print("Таблица '{}' в базе данных не найдена".format(namespace.show))

    if (namespace.show == None) and (namespace.fill == None) and (namespace.init == None):
        parser.print_help()
        