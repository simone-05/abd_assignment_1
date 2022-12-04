import sql_conn


# Static class
class database_manager():
    # Tries to connect to the db, if it fails, it exits, otherwise it returns an object to operate
    def connect(self, name, password, database):
        self.sql = sql.conn(name,password, database)
        # if connection failed
        if not self.sql.status: 
           raise Exception("Connection failed")
           
        # returns an operations object, where we can do crud operations on the db
        return operations(self.sql) #


# Class which contains methods to do crud operations on the database
class operations():
    def __init__(self, sql):
        self.sql = sql
    
    def insert(self, columns, table, values):
        return success|fail

    def read(self, columns, tables, condition):
        return list_of_entries

    def update(self, columns, tables, values, condition):
        return list_of_affected_rows

    def delete(self, table, condition):
        return list_of_affected_rows

#---------------------------
# Example function
db_mng1 = database_manager.connect("server1", "123456", "db1") 
db_mng1.read("*", "TABLE1", "UPLOAD_TS > $LAST_TS")

db_mng1.insert(["name", "age"], "TABLE1", ["batman", "69"])
db_mng1.insert(["name", "age"], "TABLE1", ["thanos", "420"])

db_mng1.update(["name", "age"], "TABLE2", ["spiderman", "42"], "POWER < 666")

db_mng1.delete("TABLE2", "POWER > 9000")
