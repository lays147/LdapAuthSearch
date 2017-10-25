### Ldap Auth and Search with Python-ldap

This Python Module gives you a simple script to
search for all groups in a LDAP domain.
You can change the query filter to search for whatever you want.
That can be challenging because LDAP query stuff sucks. =D
I'm just sharing this to keep you away from the hell that I
entered when working with this. =D

### Running
I tested using Python2. Not sure that works with 3. Probably works...
Install python-ldap package and then run ```python ldap.py``` a virtualenv environment.
Make sure that you have an AD server up and running and the setup for your authentication and search
is made inside the python file.

### License
This project is under MIT License, for more info read LICENSE.txt
