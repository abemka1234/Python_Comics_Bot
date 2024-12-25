import telegram
import os 
import dotenv
from download_comic import download_random_comic


def public_image(image_path,token,chat_id,alt):
    bot = telegram.Bot(token)
    print(bot.getUpdates())
    with open(image_path, 'rb') as file:
        bot.send_photo(chat_id,file,caption=alt)


def main():
    dotenv.load_dotenv()
    token = os.getenv('TOKEN')
    public_image('comic.png',token,'-1002334774251',download_random_comic())
    os.remove('comic.png')


if __name__ == '__main__':
    main()