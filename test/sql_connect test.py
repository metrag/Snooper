import pymysql
from config import host,user,password,database,port


try:
    # Подключаемся к базе данных
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 database=database,
                                 port=port)
    
    # Если подключение успешно
    print("Подключение успешноо!")
    
    # Закрываем подключение
    connection.close()

except pymysql.MySQLError as e:
    # Обработка ошибок подключения
    print("Ошибка подключения к базе данных:")
    print(e)