from init import *
from ben import *

def move(sekvens):

    side, port, start, stop = styrkod[sekvens]

    
    if (side == 'l'):
        left.set_pwm(port, start, stop)
    
    elif (side == 'r'):
        right.set_pwm(port, start, stop)
    
    else:
        pass
    
