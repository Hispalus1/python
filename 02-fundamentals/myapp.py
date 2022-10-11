import myModule as mod
import random


SPEED_OF_LIGHT = 300000000
EARTH_GRAVITY = 9.807
MOON_GRAVITY = 1.62

value = random.randint(300000, 1000000)
vaha = random.randint(100, 666)

vysledek1 = round((mod.time_by_light_speed(value)),5)
vysledek2 = round(mod.hmotnostNaMesici(vaha, EARTH_GRAVITY, MOON_GRAVITY),2)


print("Světlo urazí "+str(value)+" km za " + str(vysledek1) + "s")


print("Hmotnost "+str(vaha)+"kg na Zemi je na Měsíci " +
      str(vysledek2) + " kg")