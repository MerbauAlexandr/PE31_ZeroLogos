# C:\Users\Pavlu4ini\PycharmProjects\PE31_ZeroLogos\logo_gen.py
import requests
import random
import time
import base64
import os
import config as cfg


def generate_logo(forma, style, description):
    # Получаем IAM-токен
    iam_token = cfg.get_iam_token()

    # Настраиваем заголовки с актуальным IAM-токеном
    headers = {
        "Authorization": f"Bearer {iam_token}",
        "Content-Type": "application/json"
    }

    # Данные для запроса
    data = {
        "modelUri": f"art://{cfg.catalog_id}/yandex-art/latest",
        "generationOptions": {
            "seed": f"{random.randint(0, 1000000)}",
            "aspectRatio": {
                "widthRatio": "1",
                "heightRatio": "1"
            }
        },
        "messages": [
            {
                "weight": "1",
                "text": f"Нарисуй логотип в форме {forma} под описание: {description}, в стиле: {style}"
            }
        ]
    }

    # Отправляем POST-запрос на генерацию изображения
    response = requests.post(cfg.url_1, headers=headers, json=data)
    if response.status_code == 200:
        request_id = response.json()['id']
        time.sleep(20)  # Ожидание обработки запроса
        headers.pop("Content-Type")

        # Отправляем GET-запрос для получения результата
        response = requests.get(f"{cfg.url_2}/{request_id}", headers=headers)
        if response.status_code == 200:
            image_base64 = response.json()['response']['image']
            image_data = base64.b64decode(image_base64)
            image_path = os.path.join('static', 'image.jpeg')

            # Сохраняем изображение
            with open(image_path, 'wb') as file:
                file.write(image_data)
            return image_path
        else:
            return f"Ошибка ответа: {response.status_code} - {response.text}"
    else:
        return f"Ошибка запроса: {response.status_code} - {response.text}"
