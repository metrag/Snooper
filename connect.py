import pymysql
from config import *

connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=database,
                             port=port)

cursor = connection.cursor()