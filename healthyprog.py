from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load('water.mp3')
    mixer.music.play()
    while True:
        user_input=input()
        if user_input==stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylog.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    init_water=time()
    init_eye=time()
    init_exercise=time
    watersecs=5*60
    eyesecs=10*60
    exercisesecs=10*60
    while True:
        if time()-init_water>watersecs:
            print("drink water  ,water done then type DRANK")
            musiconloop("water.mp3","drank")
            init_water=time()
            log_now("drank water at")

        if time() - init_eye > eyesecs:
            print("do eye exercise  , done then type DONE")
            musiconloop("eyes.mp3", "done")
            init_eye = time()
            log_now("eyeexercise done at")

        #if time() - init_exercise > exercisesecs:
            print("exersice do  ,doone exercise then type DO")
            musiconloop("exercise.mp3", "do")
            init_water = time()
            log_now("done exercise at")