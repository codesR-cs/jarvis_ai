import os
import eel
from backend.feature import *
from backend.Command import *
eel.init('frontend')
os.system('start msedge.exe --app="http://localhost:8000/index.html"')
playAssistantSound()
eel.start('index.html', mode=None, block=True)