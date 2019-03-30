import pygame, time
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
#joystick1 = pygame.joystick.Joystick(1)
#joystick1.init()
#print(joystick.get_name)

while 1:
    time.sleep(0.5)
    #print(pygame.joystick.get_count())
    pygame.event.pump()
    
    fb = joystick.get_axis(0)#move axis
    lr = joystick.get_axis(1)#move axis
    ud = joystick.get_axis(2)#move axis
    tw = joystick.get_axis(3)#move axis
    lt = joystick.get_axis(4) #Left trigger
    rt = joystick.get_axis(5) #right trigger
    #rt1 = joystick1.get_axis(5) #right trigger
    trig = joystick.get_button(0)
    trig1 = joystick.get_button(1)
    trig2 = joystick.get_button(2)
    trig3 = joystick.get_button(3)
    trig4 = joystick.get_button(4)
    trig5 = joystick.get_button(5)
    trig6 = joystick.get_button(6)
    trig7 = joystick.get_button(7)
    trig8 = joystick.get_button(8)
    trig9 = joystick.get_button(9)
    trig10 = joystick.get_button(10)
    trig11 = joystick.get_button(11)
    trig12 = joystick.get_button(12)
    trig13 = joystick.get_button(13)
    #sp = joystick.get_hat(0)(0)
    enable = joystick.get_button(1)
    print("Trigger",rt)
    #print(rt1)
    print(lt)
    print(fb)
    print(lr)
    print(ud)
    print(tw)
    print(trig)
    print(trig1)
    print(trig2)
    print(trig3)
    print(trig4)
    print(trig5)
    print(trig6)
    print(trig7)
    print(trig8)
    print(trig9)
    print(trig10)
    print(trig11)
    print(trig12)
    print(trig13)
    #print(sp)
    print(enable)


