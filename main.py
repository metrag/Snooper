import requests
import json
import base64
import tkinter as tk
from tkinter import filedialog


######################################################################
api_key_numlook = "num_live_HQWbCfNDhO42LEBZNKe3vIpfPE5FgNfaD489DHfT"
API_KEY_Searchface = "52413b-551790-6db4a8-1744e0-345be2"
API_URL = "https://search4faces.com/api/json-rpc/v1"
######################################################################
import time
import sys

def type_out(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    

text="""  ___|
\___ \  __ \   _ \   _ \  __ \  
      | |   | (   | (   | |   | 
_____/ _|  _|\___/ \___/  .__/  
                         _|"""

# Запускаем анимацию
type_out(text, delay=0.02)

# Перекрашиваем в зеленый цвет
print("\033[92m" + text + "\033[0m")


choice=input("Приветствую в нашм приложение Snoop.\n1) Пробив по номеру\n2) Пробив по фото\n")
if choice=="1":
    def validate_phone_number(api_key_numlook, phone_number):
        # URL для проверки номера
        
        url = f"https://api.numlookupapi.com/v1/validate/{phone_number}?apikey={api_key_numlook}"
        # Выполнение GET-запроса
        response = requests.get(url)
        
        # Проверка статуса ответа
        if response.status_code == 200:
            try:
                data = response.json()
                return data
            except requests.exceptions.JSONDecodeError:
                return {"error": "Failed to decode JSON response"}
        else:
            return {"error": f"Request failed with status code {response.status_code}, response text: {response.text}"}

    # Номер телефона для проверки
    phone_number = "+7"+input("Input number +7")

    # Вызов функции и вывод результата
    result = validate_phone_number(api_key_numlook, phone_number)
    print("Номер телефона:" , result['number'], "\nСтрана:", result['country_name'], "\nЛокация:", result['location'],
        "\nОператор сотовой связи:",result['carrier'])







else:









    def send_request(method, params):
        headers = {
            "Content-Type": "application/json",
            "x-authorization-token": API_KEY_Searchface
        }
        
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "id": "some-id",
            "params": params
        }

        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
        return response.json()



    def detect_faces(image_base64):
        """Обнаружение лиц на изображении. Разметка лица по x y z"""
        params = {
            "image": image_base64
        }
        response = send_request("detectFaces", params)
        print("Начинаем поиск")
        print('-'*30)
        return response.get('result', {})






    def search_face(image_id, face_data):
        """Основная функция для поиска людей"""
        params = {
            "image": image_id,
            "face": face_data,
            "source": "vk_wall",
            "hidden": True,
            "results": 10,
            "lang": "ru"
        }
        response = send_request("searchFace", params)
        print(json.dumps(response, indent=4, ))
            # Получаем список профилей из ответа
        profiles = response.get('result', {}).get('profiles', [])
        
        # Выводим информацию о каждом профиле
        for profile in profiles:
            print(f"Имя: {profile.get('first_name', '')} {profile.get('last_name', '')}")
            print(f"Профиль: {profile.get('profile', '')}")
            print(f"Процент схожести: {profile.get('score', '')}")
            print(f"Город: {profile.get('city', '')}")
            print(f"Страна: {profile.get('country', '')}")
            print(f"Фото: {profile.get('photo', '')}")
            print("-" * 40)






    def encode_image_to_base64(image_path):
        """Кодирует изображение в формат Base64."""
        print("Snooper")
        print("Фото загружено\nКодируем")
        print('-'*30)
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')
        return encoded_image

    def select_image_and_process():
        """Выбор изображения и выполнение операций detectFaces и searchFace."""
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(
            title="Выберите изображение",
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
        )

        if file_path:
            # Кодируем изображение в Base64
            base64_image = encode_image_to_base64(file_path)
            
            # Выполняем обнаружение лиц
            detect_faces_result = detect_faces(base64_image)
            
            if "faces" in detect_faces_result and len(detect_faces_result["faces"]) > 0:
                # Если лица обнаружены, берем первое лицо и выполняем поиск по соцсетям
                image_id = detect_faces_result["image"]
                face_data = detect_faces_result["faces"][0]
                search_face(image_id, face_data)
            else:
                print("Лица не обнаружены.")

    if __name__ == "__main__":
        select_image_and_process()  # Обнаружение лиц и поиск профилей
