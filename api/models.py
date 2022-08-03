from sqlalchemy import Table, Column, Integer, String, Sequence, DateTime, MetaData

metadata = MetaData()

users = Table(
    "py_user", metadata,
    Column("id", Integer, Sequence("user_id_seq"), primary_key=True),
    Column("email", String(101)),
    Column("password", String(101)),
    Column("Fullname", String(101)),
    Column("created_on", DateTime),
    Column("status", String(1))
)
