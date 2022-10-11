SPEED_OF_LIGHT = 300000000 #? rychlost světla ve vakuu

def time_by_light_speed(lenght):
    return lenght / SPEED_OF_LIGHT

def hmotnostNaMesici(hmotnost, gravKonstPuvod, gravKonstNew):
    return hmotnost * (gravKonstNew / gravKonstPuvod)