import speech_recognition as sr
import pyttsx3
import pyautogui as gui

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 125)
running = 1
play = 1

def talk(text):
    engine.say(text)
    engine.runAndWait()

def start():
    play = 1
    while running:
        try:
            with sr.Microphone() as source:
                print('Listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice, language='tr-TR')
                command = command.lower()
                print(f"Verilen komut: {command}")
                if 'dur' in command or 'pause' in command or 'durdur' in command:
                    if play == 0:
                        print('Video is already paused')
                        talk('Video is already paused.')
                    else:
                        gui.press('space')
                        print('Video paused.')
                        talk('Video paused.')
                    
                    if 'oynat' in command or 'devam' in command or 'play' in command:
                        gui.press('space')
                        print('Video is playing.')
                        play = 1
                    
                    if 'sessize al' in command or 'sustur' in command:
                        gui.press('m')
                    
                    if 'sesini aç' in command:
                        gui.press('m')
                
        except:
            pass

start()