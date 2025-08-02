import playsound as ps
import eel
@eel.expose
def playAssistantSound():
    music_dir= "frontend\\assets\\audio\\jrsound.mp3"
    ps.playsound(music_dir)