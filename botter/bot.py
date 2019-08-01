import requests


offset = 539210982  # параметр необходим для подтверждения обновления
# URL = 'https://api.telegram.org/bot'  # URL на который отправляется запрос
URL = 'https://api.telegram.org/bot'  # URL на который отправляется запрос
TOKEN = '324952871:AAEI94LF9VitVYdKARABxknQSJKy4vHUymA'  # токен вашего бота, полученный от @BotFather
data = {'timeout': 100, 'offset': 3}
proxies = {'https': 'socks5h://localhost:9050', 'http': "socks5h://localhost:9050"}

def send_message(text):
    message_data = {  # формируем информацию для отправки сообщения
        'chat_id': -204554547,  # куда отправляем сообщение
        'text': text,  # само сообщение для отправки
    }

    response = requests.post(URL + TOKEN + '/sendMessage', data=message_data, proxies=proxies)
    print('tor ip: {}'.format(response.text.strip()))


def send_file(file, caption):
    message_data = {
        "chat_id": -362689456,
        "caption": caption
    }
    files = {'document': open(file, 'rb')}
    requests.post(URL + TOKEN + '/sendDocument', data=message_data, files=files)
