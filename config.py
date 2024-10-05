# C:\Users\Pavlu4ini\PycharmProjects\PE31_ZeroLogos\config.py
import os
from dotenv import load_dotenv
import requests

# Загружаем переменные из .env
load_dotenv()

# Получаем OAuth-токен из .env
oauth_token = os.getenv('OAUTH_TOKEN')

# Функция для получения IAM-токена
def get_iam_token():
    url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
    data = {
        "yandexPassportOauthToken": oauth_token
    }
    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json()['iamToken']
    else:
        raise Exception(f"Ошибка: {response.status_code} - {response.text}")

# Остальные параметры
catalog_id = "b1gnm09h06o5ufr781h7"
url_1 = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"
url_2 = "https://llm.api.cloud.yandex.net:443/operations"
