from gtts import gTTS
import subprocess
import os

checking = 'Just sent the result for'
language = 'en'
myobj = gTTS(text=checking, lang=language, slow=False)
myobj.save("prefix.mp3")
return_code = subprocess.call(["afplay", "/Users/zuziak/Desktop/voice_app/prefix.mp3"])


