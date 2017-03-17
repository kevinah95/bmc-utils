supersecuence="TATAT"
subsecuence="TTTTTT"
supersecuence=supersecuence.upper()
subsecuence=subsecuence.upper()
if(len(subsecuence)==0):
     print("Si es subsecuencia")
else:
    limit=len(supersecuence)
    for i in range(limit):
        if subsecuence[0]==supersecuence[i]:
            subsecuence=subsecuence [1:]
    if(len(subsecuence)==0):
        print("s es subsecuencia de t y t es supersecuencia de s")
    else:
        print("s no es subsecuencia de t y t no es supersecuencia de s")


    
