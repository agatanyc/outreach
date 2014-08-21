"""Generate emails from a template and a list of contacts.

   This program reads a template file and a contact list, and generates a set
   of email files, along with a shell script that may be run to send the
   emails.  The template and contact list file names are passed as command line
   arguments.  The emails and the 'send' script are written to a 'mail'
   subdirectory.
"""

from pprint import pprint
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
        name, last, mail = line.split()
        pprint((name, last, mail))
        output = template.format(name=name, last=last, mail=mail)
        pprint(output)
        spit(mail, output)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: outreach.py <form> <data>')
        sys.exit(1)
    process(sys.argv[1], sys.argv[2])
