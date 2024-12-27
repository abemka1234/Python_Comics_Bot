import telegram
import os 
import dotenv
from download_comic import download_random_comic


def public_image(image_path,token,chat_id,alt):
    bot = telegram.Bot(token)
    with open(image_path, 'rb') as file:
        bot.send_photo(chat_id,file,caption=alt)


def main():
    try:
        dotenv.load_dotenv()
        token = os.getenv('TOKEN')
        chat_id = os.getenv('CHAT_ID')
        public_image('comic.png',token,chat_id,download_random_comic())
    finally:
        os.remove('comic.png')


if __name__ == '__main__':
    main()