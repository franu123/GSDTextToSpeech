import pyttsx3

from txtspeak import read_in_female_voice
from webdata import get_data_from_web

engine = pyttsx3.init()
news_data = get_data_from_web()

read_in_female_voice(engine, news_data)