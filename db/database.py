from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()


URL = os.getenv("MYSQL_HOST")
PORT = os.getenv("MYSQL_PORT")
DB = os.getenv("MYSQL_DATABASE")
USER = os.getenv("MYSQL_USER")
PSWD = os.getenv("MYSQL_PSWD")

SQLALCHEMY_DATABASE_URI = "mysql://"+USER+":"+PSWD+"@"+URL+":"+PORT+"/"+DB

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()