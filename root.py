import speech_recognition as sr
import webbrowser
import subprocess

def open_website(url):
    webbrowser.open(url)

def search_google(query):
    search_url = f"http://www.google.com/search?q={query}"
    webbrowser.open_new_tab(search_url)

def open_software(software_name):
    try:
        subprocess.Popen([software_name])  # Open the software
    except:
        print(f"Could not open {software_name}.")

if __name__ == "__main__":
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")

    if "open my certificate" in command:
        filename1 = r"C:\Users\kalba\Pictures\Screenshots\Harvard certificate.png"
        subprocess.Popen([filename1], shell=True) 
    elif "open browser" in command:
        open_website("http://www.google.com")

    elif "search" in command:
        search_query = command.replace("search", "").strip()
        search_google(search_query)

    elif "open software" in command:
        software_name = command.replace("open software", "").strip()
        open_software(software_name)

    else:
        print("Command not recognized.")