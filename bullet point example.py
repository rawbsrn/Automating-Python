#! python3
# bulletpointadder.py - Addes Wikipedia bullet points to the start
#of each line of test on the clipboard

import pyperclip
text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)


pyperclip.copy(text)
