import pyttsx3

engine = pyttsx3.init()  # object creation


def speech_rate():
    rate = engine.getProperty('rate')
    print(rate)
    engine.setProperty('rate', 125)


def speech_volume():
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    print(volume)  # printing current volume level
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1


def read_in_female_voice(engine, txt_content):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(txt_content)
    engine.runAndWait()


def give_details():
    engine.say('My current speaking rate is ' + str(rate))


# On linux make sure that 'espeak' and 'ffmpeg' are installed
def save_my_speech():
    engine.save_to_file('Hello World', 'test.mp3')
    engine.runAndWait()


engine.stop()
