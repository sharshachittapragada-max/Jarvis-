import os
from openai import OpenAI
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key="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")
# Initialize speech engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()
mic_index = 0  # change if needed

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone(device_index=mic_index) as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command
    except:
        return ""

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Jarvis, a smart personal assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

print("Jarvis is ready! Say 'exit' to quit.")

while True:
    command = listen_command()
    if command:
        if "exit" in command.lower():
            speak("Goodbye!")
            break

        reply = ask_ai(command)
        print("Jarvis:", reply)
        speak(reply)