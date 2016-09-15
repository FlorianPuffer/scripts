#Collection of scripts

###hids.py
hids.py is a mini intrusion detection script which creates a Index of a given directory and compares it with a reference index.

If the script is executed the first time a reference index is created. After further execution the generated index is compared with the reference index.
The ouput shows which files has changed.
If a new reference index want be used just delete the generated index file

###poodle.py
poodle.py checks a specific target for SSLv3 service running which is vulnerable to POODLE attack.
The script try to setup a SSL connection with SSLv3 to a specific target.
