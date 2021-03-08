import random
def randInt(min=0, max=100):
    if min > max or max < 0:
        print("Min must be less than max. Max cannot be less than 0.")
    else:
        num = random.random() * (max - min) + min
    return round(num)
print(randInt(min=100, max=200))