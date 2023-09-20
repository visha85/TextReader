import os #for passing the command
import pygame #for executing our audio
#You Also Need To Install EdgeTTS Module


print("Welcome To Dhuani ध्वनि (Text to Speech.\n")

# speak function that Uses EdgeTTS to save audio file as data.mp3, then execute it using  pygame
def speak(data):
    
    # pass command using os module to generate a audio file
    command=f'edge-tts --rate=-15% --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    # pygame init and loading
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")
    # playing the audio
    try:
     pygame.mixer.music.play()

     while pygame.mixer.music.get_busy():
         pygame.time.Clock().tick(10)
    except Exception as e:
     print("\nSomething went wrong in pygame :\n",e)
     # close pygame
    finally:
     pygame.mixer.music.stop()
     pygame.mixer.quit()
  

# main execuation and voice variables
while True:
  Userlang=input("Enter Your Speech Language (Hindi & English):").lower()
  if Userlang == "hindi" or Userlang == "hi":
    voice="hi-IN-MadhurNeural"
  elif Userlang== "english" or Userlang == "en":
    voice="en-US-SteffanNeural"
  Userinput=input("Enter Your Query: ")
  speak(Userinput)
 




     





