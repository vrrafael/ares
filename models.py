from datetime import datetime
from peewee import SqliteDatabase, Model, CharField, DateTimeField, AutoField

db = SqliteDatabase("database.db")


class Log(Model):
    log_id = AutoField(column_name="id")
    device_id = CharField(max_length=17)
    temperatura = CharField(max_length=3)
    umidade = CharField(max_length=3)
    dt_registro = DateTimeField(default=datetime.now())

    class Meta:
        database = db
        table_name = "logs"


db.connect()
db.create_tables([Log], safe=True)
