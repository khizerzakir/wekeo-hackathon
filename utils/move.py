import math

def get_speed(u, v):
  return math.sqrt(math.pow(u, 2) + math.pow(v, 2))

def get_direction(u, v):
  return (180 + math.atan2(u, v) * (180 / math.pi)) % 360