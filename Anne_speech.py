import pyttsx   # text-to-speech library

engine = pyttsx.init()

rate = engine.getProperty("rate")
engine.setProperty("rate", 120)

engine.say("This is a test for a personal assistant")

engine.runAndWait() # THIS LINE IS IMPORTANT, runs the speech engine