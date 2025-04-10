import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please start speaking...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    audio_data = recognizer.listen(source)  # Listen for speech

# Convert speech to text
try:
    print("Processing...")
    text = recognizer.recognize_google(audio_data)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
