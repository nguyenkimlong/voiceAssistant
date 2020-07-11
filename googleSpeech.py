
from gtts import gTTS

import os
import pyglet
import pygame

# import pymedia
# tts = gTTS(text='Good morning', lang='en')
_text ='You can use another google translate domain for translation. If multiple URLs are provided it then randomly chooses a domain'

from googletrans import Translator
translator = Translator()
_trans = translator.translate(_text,dest='vi')
print(_trans.text)
_text = _trans.text

# tts = gTTS(text=_text, lang='vi')
tts = gTTS(text=_text, lang='vi')
filename = 'tmp/temp.mp3'
# tts = gTTS(text='안녕하세요', lang='ko')

tts.save(filename)
from io import BytesIO

# def say(_text):
#     tts = gTTS(text=_text, lang='vi')
#     fp = BytesIO()
#     tts.write_to_fp(fp)
#     fp.seek(0)
#     pygame.mixer.init()
#     pygame.mixer.music.load(fp)
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
# say(_text)

from pyglet.gl import *
pyglet.options['audio'] = ('openal', 'directsound', 'silent')

music = pyglet.resource.media(filename)
music.play()
pyglet.app.run()

os.remove(filename) #remove temperory file