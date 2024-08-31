import os
import json

def write_dict_to_json(file, data):
    if os.path.exists(file):
        # Если файл существует, читаем существующие данные
        with open(file, 'r', encoding='utf-8-sig') as f:
            existing_data = json.load(f)
    else:
        # Если файл не существует, создаем пустой словарь
        existing_data = {}

    # Объединяем существующие данные и новые данные
    updated_data = {**existing_data, **data}

    # Записываем обновленные данные в файл JSON с правильной кодировкой
    with open(file, 'w', encoding='utf-8-sig') as f:
        json.dump(updated_data, f, indent=2, ensure_ascii=False)

def write_dict_to_json_null(output_file):
    with open(output_file, 'w', encoding='utf-8-sig') as f:
        json.dump(None, f, indent=2, ensure_ascii=False)