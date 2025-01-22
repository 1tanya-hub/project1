import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    """Process recognized commands and perform actions."""
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook.")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
        speak("Opening Instagram.")
    else:
        speak("Sorry, I didn't understand the command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            # Listen for the wake word
            with sr.Microphone() as source:
                print("Listening for the wake word 'Jarvis'...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source)

            # Recognize the wake word
            wake_word = recognizer.recognize_google(audio).lower()
            if wake_word == "jarvis":
                speak("Jarvis is active. Please give a command.")
                
                # Listen for the actual command
                with sr.Microphone() as source:
                    print("Listening for a command...")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    command_audio = recognizer.listen(source)

                # Process the command
                command = recognizer.recognize_google(command_audio)
                print(f"Command: {command}")
                processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Request error from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
