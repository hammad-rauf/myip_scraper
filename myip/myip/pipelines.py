import sqlite3

class MyipPipeline(object):
    def __init__(self):

        self.create_connection()
        self.create_table()
        pass

    def create_connection(self):

        self.conn = sqlite3.Connection('mysip.db')
        self.curr = self.conn.cursor()
    
    def create_table(self):

        self.curr.execute("drop table if exists mysip_table")
        self.curr.execute("CREATE TABLE mysip_table( wesbite text, rating int, visiter int)")

    def process_item(self, item, spider):

        self.store_db(item)

        return item

    def store_db(self,item):

        self.curr.execute(f"insert into mysip_table values ('{item['name']}',{item['rating']},{item['visiter']})")

        self.conn.commit()
