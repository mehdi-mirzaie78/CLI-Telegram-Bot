"""
Author: Mehdi Mirzaie
Session 5 - Schedule Messages
Source: Mr.Hidden cli-bot course
Link to course: https://www.youtube.com/watch?v=ZVNTuU3vQTQ&list=PLlmUZ5fUSlwDAlqBZ_qlWScBYf_D80C0d
"""
import schedule
from time import sleep
from datetime import datetime
from pyrogram import Client
from config.settings import NAME, API_ID, API_HASH, PROXY

app = Client(NAME, API_ID, API_HASH, proxy=PROXY)


def send_message(_chat_id, _text):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with app:
        app.send_message(_chat_id, f"{_text}\n{now}")


schedule.every(20).seconds.do(send_message, 'me', 'Hello how are you dear friend?')
# schedule.every().day.at("05:59").do(send_message, 'me', 'Hello how are you dear friend?')
# schedule.every().hour.do(send_message, 'me', 'hello')
# schedule.every().day.do(send_message, 'me', 'hello')
# schedule.every(5).to(10).minutes.do(send_message, 'me', 'hello')
# schedule.every().monday.do(send_message, 'me', 'hello')
# schedule.every().wednesday.at("14:22").do(send_message, 'me', 'hello')
# schedule.every().minute.at(":17").do(send_message, 'me', 'hello')


while True:
    schedule.run_pending()
    sleep(1)
