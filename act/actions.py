import os
import subprocess as sp 
from audio.speech import speak
from PIL import ImageGrab 
from decouple import config 
from act.screenrecord import record_screen, stop_recording
import threading
from aim.vision import describe_image
import webbrowser
from audio.speech import speak, listen

programs = {
    'notepad': "notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'word': "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    'excel': "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    'powerpoint': "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
}

def open_notepad():
    os.startfile(programs['notepad'])

def open_word():
    sp.Popen(programs['word'])

def open_excel():
    sp.Popen(programs['excel'])

def open_ppt():
    sp.Popen(programs['powerpoint'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(programs['calculator'])

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_website():            
    speak('Which website would you like to open?')
    url = listen().lower()
    webbrowser.open(url)

def take_screenshot():
    media_dir=config("MEDIA_DIR")
    screenshot_file=config("SCREENSHOT_FILE")
    screenshot = ImageGrab.grab()
    screenshot.save(media_dir + "/" + screenshot_file)
    print("Screenshot saved as: " +  screenshot_file)
    speak("Screenshot saved as " + screenshot_file)

def start_screen_record():
    recording_thread = threading.Thread(target=record_screen)
    recording_thread.start()

def stop_screen_record():
    stop_recording()

def camera_vision():
    media_dir=config("MEDIA_DIR")
    screenshot_file=config("SCREENSHOT_FILE")
    screenshot = ImageGrab.grab()
    screenshot.save(media_dir + "/" + screenshot_file)

    speak(describe_image())
