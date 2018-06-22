from init import *
from ben import *

def move(side, sekvens):

    port, start, stop = styrkod[sekvens]

    
    if (side == 'r'):
        left.set_pwm(port, start, stop)
    
    elif (side == 'l'):
        right.set_pwm(port, start, stop)
    
    else:
        pass
    
    time.sleep(1)


move('l', 'VFVC')
move('l', 'VFVA')
move('r', 'HFVC')
move('r', 'HFVA')
