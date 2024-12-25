import requests
import random

def download_random_comic(path='comic.png'):
    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()
    max_comic_number = response.json()['num']
    comic_number = random.randint(1,max_comic_number)
    link = 'https://xkcd.com/{0}/info.0.json'.format(comic_number)
    response = requests.get(link)
    response.raise_for_status()
    comic_json = response.json()
    comic_image = requests.get(comic_json['img']).content
    with open('comic.png', 'wb') as file:
        file.write(comic_image)
    return comic_json['alt']