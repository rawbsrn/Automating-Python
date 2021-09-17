#!python3
#madLibs
adjective0 = input('Enter an adjective:\n')
noun0 = input('Enter an noun:\n')
verb0 = input('Enter a verb:\n')
noun1 = input('Enter another noun:\n')
output = 'The %s panda walked to  %s and  %s. A nearby %s was unaffected.'% (adjective0, noun0, verb0, noun1)
print(output)
outputFile = open('madLibOutput.txt','w')
outputFile.write(output)
outputFile.close()