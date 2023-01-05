import pyttsx3
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-0].id)

engine.say("Olá meu nome é Karen, e eu fui criada para ajudar meu mestre")
engine.runAndWait()