import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("hello there my name is Jexi, your virtual AI system")
engine.say('what can i do for you?')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


try:
    with sr.Microphone() as source:
        listener.pause_threshold = 1
        listener.adjust_for_ambient_noise(source)
        print("listening....")
        talk('your wish is my command')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        if 'Jexi' or 'alexa' in command:
            talk(command)
        else:
            talk("i don't know what the fuck you just said")

except:
    talk(' you are not connected to the internet, please connect to the internet and try again.')
