

# Write a Python program to print a dictionary whose keys should be the valuealphabet from a-z and the value should be corresponding ASCII 

import string
d = {c: ord(c) for c in string.ascii_lowercase}
print(d)



