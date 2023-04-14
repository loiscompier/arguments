# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
## Part 1: Greet Template
def greet(name, message = "Hello, <name>!"):
    return message.replace("<name>", name)
# test 
#print(greet("Lois"))
#print (greet('Bob', "What's up, <name>!"))


##Part 2: Force
import math 

def force ( mass, body ="earth"):
    gravity = {
         'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6,
    }

    if body.lower() not in gravity:
        raise ValueError("Invalid celestial body specified.")
    #mass = round( mass, 1)
    b = gravity[body.lower()]
    x = round(mass * b, 2)
    return x
#test 
# print (force(7.6666, "earth"))

## Part 3: Gravity

def pull (m1,m2,d): 
    G = 6.674e-11
    Y = G* ((m1*m2/d**2))
    return Y 

print(pull (800,1500,3))