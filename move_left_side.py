from init import *
from ben import *

def move(side, sekvens):

    port, start, stop = styrkod[sekvens]

    
    if (side == 'l'):
        left.set_pwm(port, start, stop)
    
    elif (side == 'r'):
        right.set_pwm(port, start, stop)
    
    else:
        pass
    
    time.sleep(1)


move('l', 'VFVC')
move('l', 'VFVA')
move('r', 'HFLC')
move('r', 'HFLA')
move('r', 'HFVC')
move('r', 'HFVA')
