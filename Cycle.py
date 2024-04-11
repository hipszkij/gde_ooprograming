import math

def cycleCircumference(r: float):
    return 2 * r * math.pi

def areaOfCicle(r: float):
    return math.pow(r,2) * math.pi


r: float = 4;

print(cycleCircumference(r))
print(areaOfCicle(r))