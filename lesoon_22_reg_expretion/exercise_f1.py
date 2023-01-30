import re
#1
print(re.search("^[A-Z][a-z]*","Fgjhxjb"))
#2
print(re.search("(TATAA)[ACGT]{3}(TT)", "ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"))
print(re.search("(TATAA)[ACGT]{3}(TT)", "ACGACGTTTACACGGAAATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"))

#3
print(re.search("[0-9]{2}.[^0-9]{2}","45*ga"))
print(re.search("[0-9]{2}.[^0-9]{2}","12-ch"))


jhdjgfjhkdjhfj