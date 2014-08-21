"""Generate emails from a template and a list of contacts.

   This program reads a template file and a contact list, and generates a set
   of email files, along with a shell script that may be run to send the
   emails.  The template and contact list file names are passed as command line
   arguments.  The emails and the 'send' script are written to a 'mail'
   subdirectory.
"""

import os
import sys

def slurp(name):
    """(str) -> str"""
    with open(name) as file:
        return file.read()

def spat(name, text):
    """(str, str) -> NoneType

    Creates new 'name' file or appends to existing file.  The content of the
    file is 'text'.
    """
    with open(name, 'a') as file:
        file.write(text)

def spit(name, text):
    """(str, str) -> NoneType"""
    with open(name, 'w') as file:
        file.write(text)

def process(form, data):
    template = slurp(form)
    contacts = slurp(data)
    folder = 'emails'
    os.mkdir(folder)
    for line in contacts.splitlines():
        if not line.startswith('#'):
            name, last, mail = line.split()
            output = template.format(name=name, last=last, mail=mail)
            file = folder + '/' + mail + '.eml'
            spit(file, output)
            spat('send', "mutt -H - < " + file + "\n")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: outreach.py <form> <data>')
        sys.exit(1)
    process(sys.argv[1], sys.argv[2])
