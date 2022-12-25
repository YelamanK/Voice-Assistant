import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit

listener = sr.Recognizer()
player = pyttsx3.init()

def listen():
    with sr.Microphone() as input_device:
        print("I am ready. Listening...")
        voice_content = listener.listen(input_device)
        text_command = listener.recognize_google(voice_content)
        text_command = text_command.lower()
        print(text_command)

    return text_command

def talk(text):
    player.say(text)
    player.runAndWait()

def voiceChange():
    eng = pyttsx3.init() #initialize an instance
    voice = eng.getProperty('voices') #get the available voices
    # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    eng.setProperty('voice', voice[2].id) #changing voice to index 1 for female voice
    eng.say("Hey there! How can I help you?") #say method for passing text to be spoken
    eng.runAndWait() #run and process the voice command

def run_voice_bot():
        command = listen()
        if "Jason" in command:
            command = command.replace("Jason", "")
        if "what is" in command:
            command = command.replace("what is", "")
            info = wikipedia.summary(command, 5)
            talk(info)

        elif "who is" in command:
            command = command.replace("who is", "")
            info = wikipedia.summary(command, 5)
            talk(info)

        elif "play" in command:
            command = command.replace("play", "")
            pywhatkit.playonyt(command)

        else:
            talk("Sorry, I'm unable to find what you're looking for")

if __name__ == "__main__":
    voiceChange()

run_voice_bot()