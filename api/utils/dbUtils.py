import databases
import sqlalchemy
from functools import lru_cache
from api import config
from api.models import metadata


# 1 using pydantic to load .env file configurations

@lru_cache()
def setting():
    return config.Settings()


def database_config():
    return str(
        setting().DB_CONNECTION + "://" + setting().DB_USERNAME + ":" + setting().DB_PASSWORD +
        "@" + setting().DB_HOST + ":" + setting().DB_PORT + "/" + setting().DB_DATABASE)


database = databases.Database(database_config())
engine = sqlalchemy.create_engine(database_config())
metadata.create_all(engine)
