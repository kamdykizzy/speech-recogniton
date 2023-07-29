import speech_recognition as sr
#create recogniser
def Commandlister():
    #create the speech recogniser
    recognizer = sr.Recognizer()
    print("listening for speech...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source=source)
        audio = recognizer.listen(source)
        print("hello")
        query = recognizer.recognize_google(audio)
        print(f'listener says: {query}')
        
# function invocation
Commandlister()