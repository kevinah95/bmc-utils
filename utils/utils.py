def verify_adn(string):
    Sec=string
    ADN=("ATCG")
    limit=len(Sec)
    flag=True
    Sec=Sec.upper()
    if Sec=="":
        print("No es una secuencia de ADN válida")
    else:
        for i in range(limit):
            if not(Sec[i] in ADN):
                flag=False
##        if flag==True:
##            print("Es una secuencia de ADN válida")
##        else:
##            print("No es una secuencia de ADN válida")
    return flag


def verify_arn(string):
	Sec=string
	ARN=("AUCG")
	limit=len(Sec)
	flag=True
	Sec=Sec.upper()
	if Sec=="":
	    print("No es una secuencia de ARN válida")
	else:
	    for i in range(limit):
	        if not(Sec[i] in ARN):
	            flag=False
	    # if flag==True:
	    #     print("Es una secuencia de ARN válida")
	    # else:
	    #     print("No es una secuencia de ARN válida")
	return flag

## largo de hilera

def length(string):
    return len(string)
## obtener el elemento i-ésimo de una hilera dada
def i_esimo(string)
	indice=string[1]
	print(indice)

##verificar si s es una subsecuencia de t, además el proceso inverso, si t una supersecuencia de s

def subsecuence(str1,str2):
str1=str1.upper()
str2=str2.upper()
if(len(str2)==0):
     print("Si es subsecuencia")
else:
    limit=len(str1)
    for i in range(limit):
        if str2[0]==str1[i]:
            subsecuence=str2 [1:]
    if(len(str2)==0):
        print("s es subsecuencia de t y t es supersecuencia de s")
    else:
        print("s no es subsecuencia de t y t no es supersecuencia de s")

## verificar si s es un substring de t, además el proceso inverso, si t una superstring de s

def substring(str1,str2)
str1=str1.upper()
str2=str2.upper()
if(str1 in str2):
    print("s es substring de t y t es super string de s")
else:
    print("s no es substring de t y t no es super string de s")

## operación intervalo, recibe índices i y j de entrada

def interval(string,start,end):
    return string[start:end]

## operación concatenación

def concat(fst_string,snd_string):
    return fst_string + snd_string

## operación prefijo, recibe índices s y k de entrada, para obtener los primeros k simbolos de s

def prefix(string,length)
	result=string[:length]
	print(result)

## operación sufijo, recibe índices s y k de entrada, para obtener los últimos k simbolos de s

def sufix(string,length):
    return string[-abs(length):]

## verificar si p es un prefijo de s

def prefix_check(string, prefix):
    length = len(prefix)
    flag = False
    if(length <= len(string)):
        to_compare = string[:length]
        if(to_compare == prefix):
            flag = True
    return flag
print(prefix_check(string,prefix))

## verificar si s es un sufijo de t

def sufix_check(string, sufix):
    length = len(sufix)
    if(length <= len(string)):
        to_compare = string[length:]
        if(to_compare == sufix):
            print("SÃƒÂ­ es sufijo")
        else:
            print("No es sufijo")
    else:
        print("No es sufijo")

## calcular el complemento de una hilera de ADN

def complement(string):
    string = string.upper()
    d={'A' : 'T', 'T' : 'A',
       'C' : 'G', 'G' : 'C'}
    return ''.join(d[s] for s in string if s in d.keys())

## calcular el complemento inverso de una hilera de ADN

def complement_reverse(string):
    string = string.upper()
    string = string[::-1]
    return complement(string)

## verificar si la hilera s es palíndromo

def palindrome(string):
    string[::-1] == string
