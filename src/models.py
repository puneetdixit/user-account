import peewee

from src.database_manager import Database

database = Database()


class Users(peewee.Model):
    email = peewee.CharField(primary_key=True)
    first_name = peewee.CharField()
    last_name = peewee.CharField()
    password = peewee.CharField()

    class Meta:
        database = database.db
        db_table = 'users'