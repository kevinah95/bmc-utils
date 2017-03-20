import random,math

def interval(string,start,end):
    return string[start:end]

def concat(fst_string,snd_string):
    return fst_string + snd_string
def sufix(string,length):
    return string[-abs(length):]
def complement(string):
    string = string.upper()
    d={'A' : 'T', 'T' : 'A',
       'C' : 'G', 'G' : 'C'}
    return ''.join(d[s] for s in string if s in d.keys())
def complement_reverse(string):
    string = string.upper()
    string = string[::-1]
    return complement(string)

def sufix_check(string, sufix):
    length = len(sufix)
    if(length <= len(string)):
        to_compare = string[:length]
        if(to_compare == sufix):
            print("SÃ­ es sufijo")
        else:
            print("No es sufijo")
    else:
        print("No es sufijo")


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

