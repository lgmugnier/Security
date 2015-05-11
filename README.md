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

# Basic Web Security
This directory explores several basic attacks on websites.  First is a series of SQL injection attacks on a form with varying sanitization techniques.  Second, is an XSS attack on a site wth varying defenses.  Third, is an exploration of CSRF attacks.  Finally, I linked back with the MD5 vulnerabilities for a SQL Injection attack on a site that hashes their passwords using MD5.

# Port Scanning Detector
This is a defensive script.  This is part of a larger IDS using anomoly detection.  Port Scanning, in this case SYN scanning, can be used for locating vulnerable systems and is important to recognize as a plausible recursor to an attack.  This script scans the specified document (not provided for security reasons) for hosts that send three times as many SYN packets as they recieve SYN+ACK packets.
