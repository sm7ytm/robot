from init import *
from legs import *

print('Moving servo')

# Move servo on channel 1 card left 
# and channel 2 on card right between extremes.

def move(sekvens):
    
    p1, p2, p3 = styrkod[sekvens]
        
    left_leg.set_pwm(p1, p2, p3)
    time.sleep(1)



#    left_leg.set_pwm(p1, p2, p3)
#    time.sleep(2)

#    right.set_pwm(2, 0, 200)
#    time.sleep(1)
#    right.set_pwm(2, 0, 400)
#    time.sleep(2)
    
