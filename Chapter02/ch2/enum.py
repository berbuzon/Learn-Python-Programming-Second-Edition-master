<<<<<<< HEAD
>>> GREEN = 1
>>> YELLOW = 2
>>> RED = 4
>>> TRAFFIC_LIGHTS = (GREEN, YELLOW, RED)
>>> # or with a dict
>>> traffic_lights = {'GREEN': 1, 'YELLOW': 2, 'RED': 4}
=======
GREEN = 1
YELLOW = 2
RED = 4
TRAFFIC_LIGHTS = (GREEN, YELLOW, RED)
# or with a dict
traffic_lights = {'GREEN': 1, 'YELLOW': 2, 'RED': 4}
>>>>>>> e79eee5d791c9eb94aaaa3df35dc2c62331731d4



# using enum
<<<<<<< HEAD
>>> from enum import Enum
>>> class TrafficLight(Enum):
...     GREEN = 1
...     YELLOW = 2
...     RED = 4
...
>>> TrafficLight.GREEN
<TrafficLight.GREEN: 1>
>>> TrafficLight.GREEN.name
'GREEN'
>>> TrafficLight.GREEN.value
1
>>> TrafficLight(1)
<TrafficLight.GREEN: 1>
>>> TrafficLight(4)
<TrafficLight.RED: 4>
=======
from enum import Enum
class TrafficLight(Enum):
	GREEN = 1
	YELLOW = 2
	RED = 4

print(TrafficLight.GREEN)
print(TrafficLight.GREEN.name)
print(TrafficLight.GREEN.value)
print(TrafficLight(1))
print(TrafficLight(4))
if TrafficLight.GREEN == TrafficLight(1):
    print("Es verde")

def is_valid_traffic_light(light):
    return light in TrafficLight

print(is_valid_traffic_light(TrafficLight.GREEN))  # Salida: True
print(is_valid_traffic_light(5))                   # Salida: False
>>>>>>> e79eee5d791c9eb94aaaa3df35dc2c62331731d4
