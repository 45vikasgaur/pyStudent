ith sr.Microphone() as source:
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
    #         print(