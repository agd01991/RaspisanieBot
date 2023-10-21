import requests
import datetime
import time
import re
from pytz import timezone
from urllib.parse import quote

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
token="6427592954:AAGgNQSwhq7r5baOpFAJpmrJumWa-ntOs5E"
my_chat_id = "394369310"
logs_chat_id2 = "-4039568612"
final_chat_id3 = "-1001985927111"

# Функция для отправки сообщения в Telegram
def send_message_to_telegram(sbj, room, chat):
  chat_id = chat
  message = f"{sbj} \n{room}"
  message = quote(message)
  url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
  requests.get(url).json()

moscow_timezone = timezone('Europe/Moscow')
current_time = datetime.datetime.now(moscow_timezone)

sbj = 'Бот перезапущен на amvera'
room = f'Время запуска {current_time}'

print(f'{sbj} \n{room}')
send_message_to_telegram(sbj, room, my_chat_id)
send_message_to_telegram(sbj, room, logs_chat_id2)

while True:
    # Ваш код для получения расписания
    url = "https://rasp.dmami.ru/site/group?group=234-321&session=0"
    payload = {}
    headers = {
        'cookie': 'group=234-321',
        'referer': 'https://rasp.dmami.ru/?234-321'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

    if response.status_code == 200:
        moscow_timezone = timezone('Europe/Moscow')
        current_time = datetime.datetime.now(moscow_timezone)
        schedule_data = response.json()
        print(current_time)
        print(current_time.weekday(), current_time.hour, current_time.minute, current_time.second)
        # На понедельник
        if current_time.weekday() == 0:

            print('Сегодня понедельник!')

            # Проверяем, что текущее время 17:55
            if current_time.hour == 17 and current_time.minute == 54:
                print('Время 17:55')
                sbj = 'Основы языкознания'
                room = 'Ссылка в группе "234-321"'
                send_message_to_telegram(sbj, room, my_chat_id)
                send_message_to_telegram(sbj, room, final_chat_id3)
                time.sleep(60)
            # Проверяем, что текущее время 19:30
            if current_time.hour == 19 and current_time.minute == 29:
                print('Время 19:30')
                sbj = 'Научно-исследовательская и проектная деятельность'
                room = 'https://teams.microsoft.com/l/meetup-join/19:ACCwkZlMB2VUyGLZaWGvyIz5zMFC_GblQMCnw9d41qs1@thread.tacv2/1695047924859?context=%7B%22Tid%22:%2230b86380-7ee9-41a2-afbf-dd87752f1db1%22,%22Oid%22:%2238f19c67-90d5-461b-899e-42103096b463%22%7D'
                send_message_to_telegram(sbj, room, my_chat_id)
                send_message_to_telegram(sbj, room, final_chat_id3)
                time.sleep(60)

        # На вторник
        if current_time.weekday() == 1:
          
            print('Сегодня вторник!')
            



            room = 'Ссылка в группе "234-321"'
            sbj = 'Обучающие системы'

            # Проверяем, что текущее время 19:30
            if current_time.hour == 19 and current_time.minute == 29:
                print('Время 19:30')
                url_match = re.search(r'href="([^"]+)"', room)
                room = url_match.group(1)
                send_message_to_telegram(sbj, room, my_chat_id)
                send_message_to_telegram(sbj, room, final_chat_id3)
                time.sleep(60)

        # На среду 
        if current_time.weekday() == 2:

            print('Сегодня среда!')


            room = 'https://us04web.zoom.us/j/74707651287?pwd=KpaENgf53Um6BMvvfWLIQ9X2fGJY5e.1'
            sbj = 'Анатомия и физиология человека'

            # Проверяем, что текущее время 19:30
            if current_time.hour == 19 and current_time.minute == 29:
                print('Время 19:30')
                url_match = re.search(r'href="([^"]+)"', room)
                room = url_match.group(1)
                send_message_to_telegram(sbj, room, my_chat_id)
                send_message_to_telegram(sbj, room, final_chat_id3)
                time.sleep(60)

        # На четверг 
        if current_time.weekday() == 3:

            print('Сегодня четверг!')
            # Четверг, 7 пара
            room = 'https://teams.microsoft.com/l/meetup-join/19:LfmBvtjhlBb3ETLUFzP_HW_2036v9Zlqcmxoom7GatE1@thread.tacv2/1695919237565?context=%7B%22Tid%22:%2230b86380-7ee9-41a2-afbf-dd87752f1db1%22,%22Oid%22:%2238f19c67-90d5-461b-899e-42103096b463%22%7D'
            sbj = 'Компьютерная лингвистика'

            # Проверяем, что текущее время 19:30
            if current_time.hour == 19 and current_time.minute == 29:
                print('Время 19:30')
                send_message_to_telegram(sbj, room, my_chat_id)
                send_message_to_telegram(sbj, room, final_chat_id3)
                time.sleep(60)

        # На пятницу
        if current_time.weekday() == 4:

            print('Сегодня пятница!')
            # Пятница, 6 пара
            room = 'https://us06web.zoom.us/j/6423304512?pwd=STdqekhJVVVkNGlMM2RJdlNQc2FXdz09'
            sbj = 'Логика и алгоритмы'

            # Проверяем, что текущее время 17:50
            if current_time.hour == 17 and current_time.minute == 49:
                print('Время 17:50')
                send_message_to_telegram(sbj, room, my_chat_id)
                send_message_to_telegram(sbj, room, final_chat_id3)
                time.sleep(60)

        # На субботу
        if current_time.weekday() == 5:

            print('Сегодня суббота!')
            # Суббота, 2 - 3 пара

            # Проверяем, что текущее время 10:40
            if current_time.hour == 10 and current_time.minute == 39:
                print('Время 10:40')
                room = 'http://clck.ru/MCYiY'
                sbj = 'Современные технологии программирования'
                send_message_to_telegram(sbj, room, my_chat_id)
                send_message_to_telegram(sbj, room, final_chat_id3)
                time.sleep(60)
            
            # Проверяем, что текущее время 12:20
            if current_time.hour == 12 and current_time.minute == 19:
                print('Время 12:20')
                room = 'https://teams.microsoft.com/l/meetup-join/19%3ameeting_MWIxMGY1ODUtZmJlMi00MjlmLThkNDEtZWViMmY1YjE2NmMy%40thread.v2/0?context=%7b%22Tid%22%3a%2230b86380-7ee9-41a2-afbf-dd87752f1db1%22%2c%22Oid%22%3a%221672541d-24a4-4e53-ada8-5cb860827e5b%22%7d'
                sbj = 'Биомедицинские технологии'
                send_message_to_telegram(sbj, room, my_chat_id)
                send_message_to_telegram(sbj, room, final_chat_id3)
                time.sleep(60)


    else:
        print("Ошибка при запросе к API")

    sbj = 'Бот работает на amvera'
    room = f'{current_time.weekday()}  {current_time.hour}  {current_time.minute}  {current_time.second}'
    
    send_message_to_telegram(sbj, room, logs_chat_id2)

    time.sleep(57)




# git pull amvera master
# git push amvera master