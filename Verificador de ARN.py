Sec=("ATGFCR")
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
    if flag==True:
        print("Es una secuencia de ARN válida")
    else:
        print("No es una secuencia de ARN válida")
