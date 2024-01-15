"""
Author: Mehdi Mirzaie
Session 8 - Periodic Profile Update
Source: Mr.Hidden cli-bot course
Link to course: https://www.youtube.com/watch?v=ZVNTuU3vQTQ&list=PLlmUZ5fUSlwDAlqBZ_qlWScBYf_D80C0d
"""

import os
import schedule
from pyrogram import Client
from config.settings import NAME, API_ID, API_HASH, PROXY
from time import sleep
from datetime import datetime
from random import choice

BIO = 'Our world is the creation of our mind.'
IMAGES_DIRECTORY = 'images'


class ImageHandler:
    """
    This class is responsible for handling images.
    random_image is a method that chooses a random image from the specified directory.
    You can add a method to generate an image by using cv2 library.
    """

    def __init__(self, directory: str) -> None:
        self.directory = directory

    def get_image_list(self):
        list_dir = os.listdir(self.directory)
        list_dir = list(map(lambda x: f'{self.directory}/{x}', list_dir))
        return [item for item in list_dir if os.path.isfile(item)]

    def random_image(self):
        image_list = self.get_image_list()
        print(f' Selecting a random image from {self.directory} '.center(100, '='))
        return choice(image_list)

    @property
    def image(self):
        """Generate a profile's image"""
        return self.random_image()


class Profile:
    def __init__(self, bot: Client, image_handler: ImageHandler) -> None:
        self.bot = bot
        self.image_handler = image_handler

    @property
    def bio(self, const_bio: str = BIO) -> str:
        now = datetime.now().strftime("%H:%M")
        return f'{const_bio} Time: {now}'

    def update_profile(self, first_name: str = None, last_name: str = None, bio: str = None) -> None:
        kwargs = {key: value for key, value in locals().items() if value is not None and key != 'self'}
        with self.bot as bot:
            bot.update_profile(**kwargs)

    def set_random_profile_image(self):
        image = self.image_handler.image
        with self.bot as bot:
            bot.set_profile_photo(photo=image)
        print(f' Set profile photo: {image} '.center(100, '='))

    def update_profile_bio(self):
        print(' Updating profile... '.center(50, '='))
        self.update_profile(bio=self.bio)


def job():
    app = Client(NAME, API_ID, API_HASH, proxy=PROXY)
    img_handler = ImageHandler(IMAGES_DIRECTORY)

    print(' Job is running... '.center(50, '='))
    profile = Profile(app, img_handler)

    # Updates Profile information
    profile.update_profile_bio()

    # If you want to choose a random image for your profile photo.
    # profile.set_random_profile_image()


def main():
    print(' Press Ctrl+C to stop bot... '.center(50, '='), end='\n\n\n')
    try:
        schedule.every(10).seconds.do(job)
        while True:
            schedule.run_pending()
            sleep(2)
    except KeyboardInterrupt:
        print(' Bot stopped '.center(50, 'X'))


if __name__ == '__main__':
    main()
