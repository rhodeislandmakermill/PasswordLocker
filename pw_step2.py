#pw.py - An insecure password program

import sys

PASSWORDS = {'email': '78DefRdfer',
             'github': '15HeiamFda',
             'google': '123456'}

print(sys.argv)
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]