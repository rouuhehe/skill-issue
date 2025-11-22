import time, random, gi
import pyperclip as pc
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("(っ╥﹏╥ς) cs student detected, opinion rejected")

words_response = {
    "error": ["skill issue", "jeje", ":3", "toda la vida lo mismo"],
    "syntax error": ["skill issue galáctico", "upsi", "toda la vida lo mismo"],
    "syntaxerror": ["skill issue galáctico", "upsi", "toda la vida lo mismo"],
    "exception error": ["#gptazo", ":3"],
    "exceptionerror": ["#gptazo", ":3"],
    "fatal": ["smh", "toda la vida lo mismo"],
    "warning": ["xdd", "bruh", "toda la vida lo mismo"],
    "failed": ["oh", "oh okay", "dontgotherecuzyoullneverreturn"],
    "exception": ["#gptazo", ":3"],
    "critical": ["smh", "toda la vida lo mismo"],
    "denied": ["ya fue ya", "una raya más al tigre"],
    "unauthorized": ["me odia", "no one has to know bbygirl"],
    "not found": ["ya no ya", "tlaboca"],
    "segmentation fault": ["upsi", "upsi :3", "toda la vida lo mismo"]
}

last_content = pc.paste().lower()

def sound_alert(word):
    # Placeholder for sound alert functionality
    pass

def get_random_response(content):
    global last_content

    if last_content == content:
        return
    
    for word,res in words_response.items():
        if word in content:
            Notify.Notification.new("Ain't no way..", random.choice(res)).show()
            break

    last_content = content

print("starting...")

while True:
    lowered = pc.paste().lower()
    if lowered == "potodestroyer69":
        Notify.Notification.new("Exiting", "Goodbye! ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧").show()
        break
    get_random_response(lowered)
    time.sleep(1)  # Check every second

