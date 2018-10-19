"""
Boolean operators aren't just evaluated from left to right.
Just like with arithmetic operators, there's an order of operations for boolean operators:
not is evaluated first;
and is evaluated next;
or is evaluated last.
"""

onetro = 1>3 and not True or False and 5<3

print (onetro)
