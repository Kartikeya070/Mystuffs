from gtts import gTTS
import os


mytext = "Hello bikku bhaiya"

language="en"
output= gTTS(text=mytext,lang=language,slow=False)
output.save("output.mp3")

os.system("start output.mp3")


