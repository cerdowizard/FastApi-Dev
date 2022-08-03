from api.utils.dbUtils import database
from api.auth import schema


def find_exist_user(email: str):
    query = "select * from py_user where status='1' and email=:email"
    return database.fetch_one(query, values={"email": email})


def save_new_user(user: schema.UserCreate):
    query = "INSERT INTO py_user VALUES(nextval('user_id_seq'), :email,:password,:fullname, now() at time zone 'UTC', '1')"
    return database.execute(query, values={"email": user.email, "password": user.password, "fullname": user.fullname})
