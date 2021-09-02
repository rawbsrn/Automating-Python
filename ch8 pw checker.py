#! python3
# StrongPWChecker
import pyperclip, re, sys

passwordRegex = re.compile(r'''(
    (?=.{8,}$)                                   #Length longer than 8
    (?=.*[A-Z])                                  #At least one Upper Case
    (?=.*[a-z])                                  #At least one lower case
    (?=.*[0-9])                                  #At least one digit
    (?=.*[ !"#$%&'()*+,\-./:;<=>?@[\\\]^_`{|}~]) #At least one special character per OWASP list
    )''',re.VERBOSE)

testWord = input("This is a password security checker. Please enter your password to see if it meets security requirements.\n")
if passwordRegex.search(testWord)== None:
    print('fix this shit')
    sys.exit()
else:
    print('meets complexity. Woohoo! Now go change your password to something I dont know.')

