import sys
import webbrowser
import speech_recognition as sr
import pyttsx3

# voice function


def talk(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()

# function to listen to commands


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio).lower()
        print('You say ' + task)
    except sr.UnknownValueError:
        talk('I don`t understand')
        task = command()

    return task

# Command execution function


def make_something(task):
    if 'youtube' in task:
        talk('opening')
        url = 'https://www.youtube.com/'
        webbrowser.open(url)
    elif 'github' in task:
        talk('opening')
        url = 'https://github.com/kad1m'
        webbrowser.open(url)
    elif 'google' in task:
        talk('opening')
        url = 'https://www.google.com/'
        webbrowser.open(url)
    elif 'linkedin' in task:
        talk('opening')
        url = 'https://www.linkedin.com/in/dmytro-lytvynenko/'
        webbrowser.open(url)
    elif 'stop' in task:
        print('stop')
        talk('goodbye')
        sys.exit()


while True:
    make_something(command())




