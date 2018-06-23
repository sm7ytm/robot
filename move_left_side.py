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
    
    


move('VFVC')
time.sleep(1)
move('VFVA')
move('HFLC')
time.sleep(1)
move('HFLA')
move('HFVC')
time.sleep(1)
move('HFVA')
time.sleep(1)
move('VTLB')
move('VTBB')
