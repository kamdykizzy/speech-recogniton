import spee
#create recogniser
def Commandlister():
    #create the speech recogniser
    recognizer = sr.Recognizer()
    print("listeng for speech...")
    
    with sr.Microphone()as source:
        audio = recognizer.listen(source)
        query = recognizer.recognise_google(audio)
        print(f'listener says: {query}')
        
# function invocation
Commandlister()