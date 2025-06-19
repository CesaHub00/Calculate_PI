# find π from a random function (0,1)

import random
def estimate_pi(n):
    number_pt_circle = 0
    number_pt_total = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        distance = x**2 + y**2
        if distance <= 1:
            number_pt_circle += 1
        number_pt_total += 1
    return 4 * number_pt_circle/number_pt_total

number = input()
result = estimate_pi(int(number))
print(result)
