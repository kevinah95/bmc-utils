
import random
import re
import itertools
from .const import *

def verify_adn(string):
    ADN = ("ATCG")
    limit = len(string)
    flag = True
    string = string.upper()
    if string == "":
        print("No es una secuencia de ADN válida")
    else:
        for i in range(limit):
            if not string[i] in ADN:
                flag = False
    return flag


def verify_arn(string):
    string = string
    ARN = ("AUCG")
    limit = len(string)
    flag = True
    string = string.upper()
    if string == "":
        print("No es una secuencia de ARN válida")
    else:
        for i in range(limit):
            if not string[i] in ARN:
                flag = False
    return flag

# largo de hilera


def length(string):
    return len(string)

# obtener el elemento i-ésimo de una hilera dada


def i_esimo(string):
    indice = string[1]
    print(indice)

# verificar si s es una subsecuencia de t, además el proceso inverso, si t
# una supersecuencia de s


def subsequence(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    if len(str2) == 0:
        print("Si es subsecuencia")
    else:
        limit = len(str1)
        for i in range(limit):
            if str2[0] == str1[i]:
                subsequence = str2[1:]
        if(len(str2) == 0):
            print("s es subsecuencia de t y t es supersecuencia de s")
        else:
            print("s no es subsecuencia de t y t no es supersecuencia de s")

# verificar si s es un substring de t, además el proceso inverso, si t una
# superstring de s


def substring(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    if(str1 in str2):
        print("s es substring de t y t es super string de s")
    else:
        print("s no es substring de t y t no es super string de s")

# operación intervalo, recibe índices i y j de entrada


def interval(string, start, end):
    return string[start:end]

# operación concatenación


def concat(fst_string, snd_string):
    return fst_string + snd_string

# operación prefijo, recibe índices s y k de entrada, para obtener los
# primeros k simbolos de s


def prefix(string, length):
    result = string[:length]
    print(result)

# operación sufijo, recibe índices s y k de entrada, para obtener los
# últimos k simbolos de s


def sufix(string, length):
    return string[-abs(length):]

# verificar si p es un prefijo de s


def prefix_check(string, prefix):
    length = len(prefix)
    flag = False
    if(length <= len(string)):
        to_compare = string[:length]
        if(to_compare == prefix):
            flag = True
    return flag


# verificar si s es un sufijo de t


def sufix_check(string, sufix):
    length = len(sufix)
    if length <= len(string):
        to_compare = string[length:]
        if to_compare == sufix:
            print("SÃƒÂ­ es sufijo")
        else:
            print("No es sufijo")
    else:
        print("No es sufijo")

# calcular el complemento de una hilera de ADN


def complement(string):
    string = string.upper()
    d = {'A': 'T', 'T': 'A',
         'C': 'G', 'G': 'C'}
    return ''.join(d[s] for s in string if s in d.keys())

# calcular el complemento inverso de una hilera de ADN


def complement_reverse(string):
    string = string.upper()
    string = string[::-1]
    return complement(string)

# verificar si la hilera s es palíndromo


def palindrome(string):
    return string[::-1] == string

# Generador aleatorio de secuencias de ADN


def random_secuence(string, length):
    new_string = ""
    for _ in range(length):
        new_string += random.choice(string)
        print(new_string)


# Traductor ADN a ARN
def adn_to_arn(string):
    string = string.upper()
    if verify_adn(string):
        return string.replace("T", "U")
    else:
        return ""

## Traductor Genético: ADN a aminoácidos

def translate(dictionary, string):
    pattern = re.compile('|'.join(dictionary.keys()))
    result = pattern.sub(lambda x: dictionary[x.group()], string)
    return result

def adn_to_aminoacid(strADN):
    to_change = len(strADN) % 3
    strADN = strADN[:-to_change]
    print("Se removeran las ultimas" + str(to_change) + "letras")
    str_arn = adn_to_arn(strADN)
    print("Full")
    print(translate(TABLE_GENETIC_CODE_FULL, str_arn))
    print("3-letras")
    str_new_seq = translate(TABLE_GENETIC_CODE_THREE_LETTERS, str_arn)
    print(str_new_seq)
    print("1-letra")
    print(translate(TABLE_GENETIC_CODE_SINGLE_LETTER, str_new_seq))

def one_to_three_aux(string, dictionary):
    aux_string = ""
    for i in range(0, len(string), 1):
        codon = string[i:i + 1]
        for key, value in dictionary.items():
            if value == codon:
                aux_string += key
    return aux_string

def three_to_adn_aux(string, dictionary):
    big_list = []
    aux_list = []
    for i in range(0, len(string), 3):
        codon = string[i:i + 3]
        for key, value in dictionary.items():
            if value == codon:
                aux_list.append(key)
        big_list.append(aux_list)
        aux_list = []
    return big_list

def three_to_adn(string):
    big_list = three_to_adn_aux(string, TABLE_GENETIC_CODE_THREE_LETTERS)
    list01 = list(itertools.product(*big_list))
    new_data = (' '.join(w) for w in list01)
    print(list(new_data))

def one_to_adn(string):
    s = one_to_three_aux(string, TABLE_GENETIC_CODE_SINGLE_LETTER)
    big_list = three_to_adn_aux(s, TABLE_GENETIC_CODE_THREE_LETTERS)
    list02 = list(itertools.product(*big_list))
    new_data = (' '.join(w) for w in list02)
    print(list(new_data))
