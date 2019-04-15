import pymysql.cursors
import json


class MariaSQL(object):

    def __init__(self, host='localhost', port=3306, user='root', password='password', db='mysql', charset='utf8mb4'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db_name = db
        self.charset = charset
        self.db = self.connect()

    def connect(self):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db_name,
            charset=self.charset,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True)

    def use(self, db_name):
        self.db_name = db_name
        self.db = self.connect()

    def show_tables(self):
        return self.query('show tables')

    def query(self, sql):
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            ret_val = cursor.fetchall()
        return ret_val

    def create_db(self, db_name):
        sql = """
            create database if not exists {db_name};
        """
        return self.query(sql.format(db_name=db_name))

    def create_table(self, name, table_def=None, primary_key='id'):
        sql = """
            create table if not exists {name} ({columns}, {keys}) ENGINE=InnoDB CHARACTER SET %s;
        """ % self.charset

        if primary_key != 'id':
            keys = 'PRIMARY KEY ({primary_key}), KEY(id)'.format(primary_key=primary_key)
        else:
            keys = 'PRIMARY KEY (id)'

        if type(table_def) is dict:
            columns = list()
            for key in table_def.items():
                if key[1] is int:
                    columns.append("`{col}` INT".format(col=key[0]))
                elif key[1] is str:
                    columns.append("`{col}` varchar(255)".format(col=key[0]))
                elif key[1] is float:
                    columns.append("`{col}` double".format(col=key[0]))
                elif key[1] is dict:
                    columns.append("`{col}` LONGTEXT".format(col=key[0]))
                elif isinstance(key[1], str):
                    columns.append("`{col}` {type}".format(col=key[0], type=key[1]))
            columns.append("`id` INT NOT NULL AUTO_INCREMENT")
            sql = sql.format(name=name, columns=", ".join(columns), keys=keys)
            ret_val = self.query(sql)
        else:
            ret_val = self.query(name)
            
        self.db.commit()
        return ret_val

    def insert(self, table, data, on_duplicate=False):
        sql = """
            insert into `{table}` ({columns}) values ({values}){ending}
        """
        columns, values, duplicate = list(), list(), list()
        for key, value in data.items():
            columns.append(key)
            values.append(type_handling(value))
            duplicate.append("`{key}` = {value}".format(key=key, value=type_handling(value)))
        
        columns = "`" + "`,`".join(columns) + "`"
        values = str(values).strip('[]').replace('None', 'NULL')

        if on_duplicate:
            ending = " ON DUPLICATE KEY UPDATE "
            ending += ", ".join(duplicate) 
            ending += ";"
        else:
            ending = ";"

        # print(sql)
        query = sql.format(table=table, columns=columns, values=values, ending=ending).strip()
        # print(query)
        ret_val = self.query(query)
        self.db.commit()
        return ret_val

    def insert_on_duplicate(self, table, data):
        return self.insert(table, data, True)


def type_handling(value):
    if type(value) is dict:
        formatted = "{value}".format(value=json.dumps(value))
    elif type(value) is int or type(value) is float:
        formatted = "{value}".format(value=value)
    elif type(value) is str:
        formatted = "{value}".format(value=value)
    elif type(value) is bytes:
        formatted = "'{value}'".format(value=value.decode())
    else:
        formatted = "NULL"
    return formatted
