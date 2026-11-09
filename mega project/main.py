import speech_recognition as sr
import webbroser
import pyttsx3
recognizer = sr.Recognizer()
engine  = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you today?")
    # with sr.Microphone() as source:
    #     print("Listening...")
    #     audio = recognizer.listen(source)
    #     try:
    #         text = recognizer.recognize_google(audio)
    #         print("You said: " + text)
    #         engine.say(text)
    #         engine.runAndWait()
    #     except sr.UnknownValueError:
    #         print("Sorry, I could not understand the audio.")
    #     except sr.RequestError as e:
    #         print("Could not request results; {0}".format(e))
