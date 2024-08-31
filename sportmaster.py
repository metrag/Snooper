from make_json import *
from connect import *

def search_in_sportmaster(phone):
    search_query = """
    SELECT * FROM sportmaster
    WHERE phone_number = %s
    LIMIT 1
    """
    
    try:
        cursor.execute(search_query, (phone))
        result = cursor.fetchone()

        if result:
            result_dict = {
                'id': result[0],
                'full_name': result[1],
                'birth_date': str(result[2]),
                'city': result[4],
                'address': result[5]
            }
            return result_dict
        else:
            pass
    finally:
        cursor.close()
        connection.close()