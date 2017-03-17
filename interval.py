def interval(string,start,end):
    return string[start:end]

def concat(fst_string,snd_string):
    return fst_string + snd_string
def sufix(string,lenght):
    return string[-abs(lenght):]
def complement(string):
    string = string.upper()
    d={'A' : 'T', 'T' : 'A',
       'C' : 'G', 'G' : 'C'}
    return ''.join(d[s] for s in string if s in d.keys())
def complement_reverse(string):
    string = string.upper()
    string = string[::-1]
    return complement(string)


