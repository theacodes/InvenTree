""" Check that there are no database migration files which have not been committed. """

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import subprocess

print("Checking for uncommitted locale files...")

cmd = ['git', 'status']

proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = proc.communicate()

locales = []

for line in str(out.decode()).split('\n'):
    # Check for any compiled translation files that have not been committed
    if 'modified:' in line and '/locale/' in line and 'django.po' in line:
        locales.append(line)

if len(locales) > 0:
    print("There are {n} unstaged locale files:".format(n=len(locales)))

    for l in locales:
        print(" - {l}".format(l=l))

sys.exit(len(locales))