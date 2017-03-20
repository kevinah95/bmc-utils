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