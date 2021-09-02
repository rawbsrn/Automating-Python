#! python3
#! RegexStrip

import pyperclip, re, sys

getText = input("insert your text\n")
print('that you want to strip: \n', getText)
toStrip = input("what do you want to remove?\n")
#^[\s]+||[\s]+$
if toStrip == '':
    toStrip = '^[\s]+||[\s]+$'
    
print('you want to remove\n', toStrip)
stripRegex=re.compile(toStrip)
print(stripRegex.sub('', getText))
