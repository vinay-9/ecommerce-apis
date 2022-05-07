from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


host = "the host name"
port = "port name"
username = "------the username------------"
password = "-----------the password-----------"
db_name = "ecommerce"


engine = create_engine(
    "mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8".format(
        username, password, host, port, db_name
    ),
)

Base = declarative_base()
Session = sessionmaker(bind=engine)
