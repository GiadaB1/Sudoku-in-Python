from pygame import*



def numbers(ev):#returns the number selected through the keyboard
    if(ev.key == K_1):
        value = 1
    elif(ev.key == K_2):
        value = 2
    elif(ev.key == K_3):
        value = 3
    elif(ev.key == K_4):
        value = 4
    elif(ev.key == K_5):
        value = 5
    elif(ev.key == K_6):
        value = 6
    elif(ev.key == K_7):
        value = 7
    elif(ev.key == K_8):
        value = 8
    elif(ev.key == K_9):
        value = 9
    else:
        value = 0
        
    return value

