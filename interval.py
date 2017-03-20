import random,math,re

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
            print("SÃƒÂ­ es sufijo")
        else:
            print("No es sufijo")
    else:
        print("No es sufijo")


# def poisson(mu):
#     b = 1
#     i = 0
#     while b >= math.exp(-mu):
#         b *= random.uniform(0, 1)
#         i += 1
#     return i - 1

# def normal(mu,sigma):
#     p1 = random.uniform(-1, 1)
#     p2 = random.uniform(-1, 1)
#     p = p1 * p1 + p2 * p2   
#     while (p >= 1):
#         p1 = random.uniform(-1, 1)
#         p2 = random.uniform(-1, 1)
#         p = p1 * p1 + p2 * p2
#     return mu + sigma * p1 * math.sqrt(-2 * math.log(p) / p)


# def verify_adn(string):
#     Sec=string
#     ADN=("ATCG")
#     limit=len(Sec)
#     flag=True
#     Sec=Sec.upper()
#     if Sec=="":
#         print("No es una secuencia de ADN válida")
#     else:
#         for i in range(limit):
#             if not(Sec[i] in ADN):
#                 flag=False
# ##        if flag==True:
# ##            print("Es una secuencia de ADN válida")
# ##        else:
# ##            print("No es una secuencia de ADN válida")
#     return flag


def adn_to_arn(string):
    string = string.upper()
    if verify_adn(string):
        return string.replace("T","U")
    else:
        return "No es una secuencia de ADN válida"

def adn_to_aminoacid(string):
    d={'A' : 'T', 'T' : 'A',
       'C' : 'G', 'G' : 'C'}


s = 'GATTTTCTA'
d = {
'TTT':'Fenilalanina',
'TTC':'Fenilalanina',
'TTA':'Leucina',
'TTG':'Leucina',
'CTT':'Leucina',
'CTC':'Leucina',
'CTA':'Leucina',
'CTG':'Leucina',
'ATT':'Isoleucina',
'ATC':'Isoleucina',
'ATA':'Isoleucina',
'ATG':'Metionina',
'GTT':'Valina',
'GTC':'Valina',
'GTA':'Valina',
'GTG':'Valina',
'TCT':'Serina',
'TCC':'Serina',
'TCA':'Serina',
'TCG':'Serina',
'CCT':'Prolina',
'CCC':'Prolina',
'CCA':'Prolina',
'CCG':'Prolina',
'ACT':'Treonina',
'ACC':'Treonina',
'ACA':'Treonina',
'ACG':'Treonina',
'GCT':'Alanina',
'GCC':'Alanina',
'GCA':'Alanina',
'GCG':'Alanina',
'TAT':'Tirosina',
'TAC':'Tirosina',
'TAA':'STOP',
'TAG':'STOP',
'CAT':'Histidina',
'CAC':'Histidina',
'CAA':'Glutamina',
'CAG':'Glutamina',
'AAT':'Asparagina',
'AAC':'Asparagina',
'AAA':'Lisina',
'AAG':'Lisina',
'GAT':'Acido Aspartico',
'GAC':'Acido Aspartico',
'GAA':'Acido Glutamico',
'GAG':'Acido Glutamico',
'TGT':'Cisteina',
'TGC':'Cisteina',
'TGA':'STOP',
'TGG':'Triptofano',
'CGT':'Arginina',
'CGC':'Arginina',
'CGA':'Arginina',
'CGG':'Arginina',
'AGT':'Serina',
'AGC':'Serina',
'AGA':'Arginina',
'AGG':'Arginina',
'GGT':'Glicina',
'GGC':'Glicina',
'GGA':'Glicina',
'GGG':'Glicina'
}

pattern = re.compile('|'.join(d.keys()))
result = pattern.sub(lambda x: d[x.group()], s)
print(result)
