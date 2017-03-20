string="ATCFGRGH"
prefix=""
def prefix_check(string, prefix):
    length = len(prefix)
    flag = False
    if(length <= len(string)):
        to_compare = string[:length]
        if(to_compare == prefix):
            flag = True
    return flag
print(prefix_check(string,prefix))
