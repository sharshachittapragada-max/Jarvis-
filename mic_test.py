import speech_recognition as sr

# Choose the microphone index (0 is usually default)
mic_index = 0

# Initialize recognizer
r = sr.Recognizer()

with sr.Microphone(device_index=mic_index) as source:
    print("Speak something...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError:
    print("Speech service unavailable")