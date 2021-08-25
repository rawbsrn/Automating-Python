#! python3
#pw.py - insecure pw manager
PASSWORDS = {'email': 'string',
             'blog': 'strong',
             'luggage': '12345',}

import pyperclip, sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy accnt pw')
    sys.exit()

account = sys.argv[1]   #1st command line arg is account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('pw 4 ' + account + ' coppied to clipboard.')
else:
    print('no acct name ' + acct)
