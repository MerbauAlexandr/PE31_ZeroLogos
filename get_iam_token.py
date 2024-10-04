import requests

# Замените на ваш OAuth-токен
oauth_token = "ваш_oauth_токен"

# URL для получения IAM-токена
url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"

# Тело запроса с OAuth-токеном
data = {
    "yandexPassportOauthToken": oauth_token
}

# Отправка POST-запроса для обмена на IAM-токен
response = requests.post(url, json=data)

# Проверка ответа
if response.status_code == 200:
    iam_token = response.json()['iamToken']
    print("IAM-токен:", iam_token)
else:
    print(f"Ошибка: {response.status_code} - {response.text}")
