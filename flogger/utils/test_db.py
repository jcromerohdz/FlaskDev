import os
from flask_sqlalchemy import sqlalchemy

class TestDB:
    def __init__(self):
        self.db_name = os.environ['DATABASE_NAME'] + '_test'
        self.db_host = os.environ['DB_HOST']
        self.db_root_password = os.environ['POSTGRES_ROOT_PASSWORD']
        if self.db_root_password:
            self.db_username = 'postgres'
            self.db_password = self.db_root_password
        else:
            self.db_username = os.environ['DB_USERNAME']
            self.db_password = os.environ['DB_PASSWORD']
        self.db_uri = 'postgresql://%s:%s@%s:5432' %(self.db_username, self.db_password, self.db_host)

    def create_db(self):
        # create the database if root user
        if self.db_root_password:
            engine = sqlalchemy.create_engine(self.db_uri)
            conn = engine.connect()
            conn.execute("COMMIT")
            conn.execute("CREATE DATABASE "+ self.db_name)
            conn.close()
        return self.db_uri + '/' + self.db_name

    def drop_db(self):
        # drop the database if root user
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute("COMMIT")
        conn.execute("SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE datname = 'flogger_test' AND pid <> pg_backend_pid()")
        conn.close()

        if self.db_root_password:
            engine = sqlalchemy.create_engine(self.db_uri)
            conn = engine.connect()
            conn.execute("COMMIT")
            conn.execute("DROP DATABASE " + self.db_name)
            conn.close()