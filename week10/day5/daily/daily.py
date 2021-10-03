# this code returns to us the amount of time it takes a webpage "yandex.com" to load 
import requests


def time_to_load():
    time = requests.get('https://www.yandex.com').elapsed.total_seconds()
    print(f'The time it took to load the page is {round(time,2)} seconds')


time_to_load()