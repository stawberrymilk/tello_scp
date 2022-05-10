rom djitelopy import tello
from time import sleep

me = Tello.Tello()
me.connect()

print(me.get_battery())
