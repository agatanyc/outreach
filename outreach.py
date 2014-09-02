#!/usr/bin/env python3

"""Generate emails from a template and a list of contacts.

   This program reads a template file and a contact list, and generates a set
   of email files, along with a shell script that may be run to send the
   emails.  The template and contact list file names are passed as command line
   arguments.  The emails and the 'send' script are written to a 'mail'
   subdirectory.
"""

import os
import sys
import shutil

def slurp(path):
    """(str) -> str
    
    Return the content of file 'path'.
    """
    with open(path) as file:
        return file.read()

def spat(path, text):
    """(str, str) -> NoneType
    
    Appends 'text' to file 'path', creating the file if necessary.
    """
    with open(path, 'a') as file:
        file.write(text)

def spit(path, text):
    """(str, str) -> NoneType
    
    Write 'text' to file 'path', creating the file if necessary.
    """
    with open(path, 'w') as file:
        file.write(text)

def process(form, data):
    template = slurp(form)
    contacts = slurp(data)
    folder = 'mail'
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    for line in contacts.splitlines():
        if not line.startswith('#'):
            name, last, mail = line.split()
            output = template.format(name=name, last=last, mail=mail)
            path = folder + '/' + mail + '.eml'
            spit(path, output)
            spat(folder + '/send', "mutt -H - < " + path + "\n")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: outreach.py <form> <data>')
        sys.exit(1)
    process(sys.argv[1], sys.argv[2])
