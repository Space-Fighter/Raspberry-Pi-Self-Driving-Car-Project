#import movements as mov
import keyboard  # using module keyboar
import time
while True:
    print('press a key')
    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        print('You Pressed A Key!')
        break  # finishing the loop
    time.sleep(1)
