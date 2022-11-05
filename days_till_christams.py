import pywhatkit as pwk
from datetime import date 
import random, os

GROUP_LINK = "ENTER_GROOP_LINK"
PHONE_NUMBER = "ENTER_PHONE_NUMBER"
IMAGE_PATH = "PATH_FOR_IMAGES"

def random_num():
    image = random.choice(os.listdir(IMAGE_PATH))
    return image

def send_message():
    daysTillChristmas = days_till_christmas()
    image = random_num()
    #pwk.sendwhatmsg_to_group_instantly(PHONE_NUMBER, f"Only {daysTillChristmas} days till christmas", 10, tab_close=True) # send message to phone number 
    pwk.sendwhats_image\
        (GROUP_LINK, f"{IMAGE_PATH}{image}",\
             f"\U0001F973 \U0001F384 \U00002744 Only {daysTillChristmas} days till Christmas \U0001F973 \U0001F384 \U00002744", tab_close=True) # send message to grope

def days_till_christmas():
    today = date.today()
    christmas = date(2022, 12, 25)
    daysTillChristmas = (christmas - today).days
    return daysTillChristmas

send_message()
