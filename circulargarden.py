import math
radius = float(input("whats the radiues of the garden in meters? "))
A = math.pi * radius ** 2
C = 2 * math.pi * radius
sqrt = math.sqrt(A)
sqrt_down = math.ceil(A)
sqrt_up = math.floor(A)
print(f"your area is {A:.2f}", f"your circumference is {C:.2f}", f"your sqaure root is {sqrt:.2f}", f"area rounded up {A:.2f}", f"area rounded down{A:.2f}" )

