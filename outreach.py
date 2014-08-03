"""Generates email from a template and a list of contacts."""

#   inputs:
#       contact info
#       template
#   outputs:
#       email to send
#       script

import sys

def slurp(name):
    """(str) -> str"""
    with open(name) as file:
        return file.read()

def spit(name, text):
    """(str, str) -> NoneType"""
    with open(name, 'w') as file:
        file.write(text)

def process(form, data):
    template = slurp(form)
    contacts = slurp(data)
    for line in contacts.splitlines():
        if not line.startswith('#'):
            name, last, mail = line.split()
            output = template.format(name=name, last=last, mail=mail)
            spit(mail + ".eml", output)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: outreach.py <form> <data>')
        sys.exit(1)
    process(sys.argv[1], sys.argv[2])
