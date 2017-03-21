import re
import itertools
from utils import const
from utils import adn_to_arn
from utils import adn_to_aminoacid
from utils import three_to_adn
from utils import one_to_adn

# http://stackoverflow.com/questions/2400504/easiest-way-to-replace-a-string-using-a-dictionary-of-replacements
##
# https://www.biostars.org/p/175252/

strADN = "TGCATGCTAC"
adn_to_aminoacid(strADN)
# GATCATATTTTGCATCGGTCCTGGCCGTCATCCACCCTACTGCCCGATCACCCGCACGGTGAAAGTCACCAATGTGGGACGTCCGTC
# DHILHRSWPSSTLLPDHPHGESHQCGTSV


three_to_adn("CysMetLys")    
print("=======================")
one_to_adn("DHI")