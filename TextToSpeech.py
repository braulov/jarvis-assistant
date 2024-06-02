from gtts import gTTS
import os

class TextToSpeech:
    def __init__(self, path = 'answer.mp3'):
        self.language = 'en'
        self.path = path
    def generate(self,text):
        myobj = gTTS(text=text, lang=self.language, slow=False)
        myobj.save(self.path)
        os.system("play -q answer.mp3")

