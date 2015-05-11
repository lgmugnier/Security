Disclaimer: Attacks were carried out on a site created specifically for this purpose, permission was granted to execute all four types of attacks.

#SQL Injection
In this section there is sql.txt.  The file contains two parts, each shows the SQL Injection method shown and a brief explanation of why it works.  The injections are url encoded.

#Cross Site Request Forgery
The files csrf_0 and csrf_1 contain xss attacks ranging for easy to hard, respectively.  Each attempts to log the victim who opens the html file into the attackers account. For csrf_0, there are no defenses so it was very simple.  For csrf_1 it was slightly more complicated because the site uses a csrf_token as a hidden field in the login form.  Therefore, I used a hybrid xss and csrf attack to allow me access and was successful.

#Cross Site Scripting
xss_0, xss_1, and xss_2 all display attacks of the xss variety.  The xss_0 file, shows the cookie of the site you just visited in an alert box, there were no defenses against this.  The second, xss_1, reports the cookie to a specific port which can then be sniffed using wireshark or netcat.  The last repeats the effects of xss_1 but there is a defense against the word script which is easily resolved.

#SQL with Hashed Passwords
The final file: sql_onePtwo, finds a basic SQL Injection string ('=') somewhere in a binary MD5 hash.  There is further explanation on why this attack works in the file itself.
