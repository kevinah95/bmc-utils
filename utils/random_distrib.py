import random,math

def poisson(mu):
    b = 1
    i = 0
    while b >= math.exp(-mu):
        b *= random.uniform(0, 1)
        i += 1
    return i - 1

def normal(mu,sigma):
    p1 = random.uniform(-1, 1)
    p2 = random.uniform(-1, 1)
    p = p1 * p1 + p2 * p2   
    while (p >= 1):
        p1 = random.uniform(-1, 1)
        p2 = random.uniform(-1, 1)
        p = p1 * p1 + p2 * p2
    return mu + sigma * p1 * math.sqrt(-2 * math.log(p) / p)

def linear():
    return random.random()