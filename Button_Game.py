from gpiozero import LED, Button
from time import sleep 
import random


led = LED(4) 

 
left_button = Button(14, bounce_time=0.1)
right_button = Button(15, bounce_time=0.1)


left_name = input('Enter name for Left Player : ')
right_name = input('Enter name for Right Player : ') 

left_score = 0
right_score = 0
led_is_on = False 

def pressed(button):
    global left_score, right_score, led_is_on
    
   
    if button.pin.number == 14:
        if led_is_on:
            left_score += 1 
            print(left_name + ' scored! Total: ' + str(left_score))
        else:
            left_score -= 1 
            print(left_name + ' pressed too early! Penalty! Total: ' + str(left_score))
            
    elif button.pin.number == 15:
        if led_is_on:
            right_score += 1
            print(right_name + ' scored! Total: ' + str(right_score))
        else:
            right_score -= 1
            print(right_name + ' pressed too early! Penalty! Total: ' + str(right_score))

  
    if left_score == 5:
        print(left_name + ' WINS THE GAME!')
        exit()
    elif right_score == 5:
        print(right_name + ' WINS THE GAME!')
        exit()
    
 
    led.off()
    led_is_on = False

left_button.when_pressed = pressed
right_button.when_pressed = pressed

print("Game Starting... Watch the LED!")

while True:
  
    wait_time = random.uniform(2, 8)
    sleep(wait_time)
    
    led.on()
    led_is_on = True 
    
  
    while led_is_on:
        sleep(0.1)
