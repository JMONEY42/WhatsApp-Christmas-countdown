import pywhatkit as pwk
from datetime import date 
import random, os

MESSAGE_LINK = "ENTER_MESSAGE_LINK"
IMAGE_PATH = "PATH_FOR_IMAGES"

def random_num():
    image = random.choice(os.listdir(IMAGE_PATH))
    return image

def send_message():
    daysTillChristmas = days_till_christmas()
    image = random_num()
    if daysTillChristmas == 0:
        pwk.sendwhats_image\
        (MESSAGE_LINK, f"{IMAGE_PATH}{image}",\
             f"\U0001F973 \U0001F384 \U00002744  ITS CHRISTMAS!!!!  \U0001F973 \U0001F384 \U00002744", tab_close=True) 
    else:
        pwk.sendwhats_image\
            (MESSAGE_LINK, f"{IMAGE_PATH}{image}",\
                f"\U0001F973 \U0001F384 \U00002744 Only {daysTillChristmas} days till Christmas \U0001F973 \U0001F384 \U00002744", tab_close=True) 

def days_till_christmas():
    today = date.today()
    year = today.year
    christmas = date(year, 12, 25)
    if today > christmas:
        year = year + 1
        christmas = date(year, 12, 25)
    daysTillChristmas = (christmas - today).days
    return daysTillChristmas

send_message()
