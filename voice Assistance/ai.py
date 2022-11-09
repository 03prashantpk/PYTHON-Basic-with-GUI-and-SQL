import pyttsx3

engine = pyttsx3.init()
engine.say("Hello sir , this is for testing purpose.")
engine.runAndWait()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hello prashant , i love you . will you marry me")
engine.runAndWait()

engine.setProperty('voice', voices[0].id)
engine.say("Sir , this is not good . She is my crush , you already have 3-4 girlfriends!!!")
engine.runAndWait()