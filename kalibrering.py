from __future__ import division

# Import the PCA9685 module.
import Adafruit_PCA9685

""" En modul för att testa servots ändlägen samt räkna ut
    var centerläget hamnar med hjälp av dessa två.
    Anslut servot till styrkortet med standard-adress, och
    till port 0. Sen är det bara att köra programmet.
"""

# Skapar ett objekt/instans av klassen Adafruit_PCA9685
srv = Adafruit_PCA9685.PCA9685(address=0x40)

# Variabler för positionerna
center = 300
cw = 300
ccw = 300


# Set frequency to 60hz, good for servos.
srv.set_pwm_freq(60)


# Ställer servot i tillfälligt center-läge innan testet startar
srv.set_pwm(0, 0, center)


# Första loopen för att kolla medurs-läget
print("Först stegar vi medurs")

while True:
    srv.set_pwm(0, 0, cw)
    print(cw)
    val = input("Nytt steg? (j/n)")
    if val != "n":
        cw += 5
    else:
        break


# Åter till center-läge
print("Återgår till center-läge")
srv.set_pwm(0, 0, center)


# Andra loopen för att kolla moturs-läget
print("Då stegar vi moturs")

while True:
    srv.set_pwm(0, 0, ccw)
    print(ccw)
    val2 = input("Nytt steg? (j/n)")
    if val2 != "n":
        ccw -= 5
    else:
        break


# Här kör vi en återgång till centerläge och
# det läget ska räknas ut med hjälp av cw och ccw
new_center = int((ccw + cw) / 2)
srv.set_pwm(0, 0, new_center)

# Då visar vi vad som blivit framtestat
print("Skriv ner dessa värden och märk servot med dem")
print("Angivet värde för ccw är: " + str(ccw))
print("Angivet värde för center är: " + str(new_center))
print("Angivet värde för cw är: " + str(cw))
