from peewee import Model as PeeweeModel, SqliteDatabase
from dotenv import dotenv_values

env = dotenv_values('.env')
db = SqliteDatabase(env['DATABASE_PATH'])


class Model(PeeweeModel):
    class Meta:
        database = db

    def save_force(self, only=None):
        return self.save(force_insert=True, only=only)
