# Security
Exploiting/exploring security vulnerabilities

# MD5 Directory
This directory explores the length extension and collision vulnerabilities of the MD5 
The length extension attack is explored in len_ext_attack.py and uses a server written by BU
Professor, Sharon Goldberg.
By using MD5's hash extension abilities, I was able to insert malicious code without the user's
consent or password.

Efficient algorithms for calculating collisions were presented in 2004.
Evil.py and good.py are two files with the same MD5 hash but act differently using code
conditioned on the SHA256 hash of the padding.

The writeup.txt talks about how using an HMAC would avoid the vulnerability I took advantage
of in the length extension attack.

