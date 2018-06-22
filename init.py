from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

left = Adafruit_PCA9685.PCA9685(address=0x40)
right = Adafruit_PCA9685.PCA9685(address=0x41)


left.set_pwm_freq(60)
right.set_pwm_freq(60)
