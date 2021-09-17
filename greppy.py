#!python3
#!Greppybutts
import os,re
#TODO: GET USER SUPPLIED REGEX
toStrip = input("What is your search regex?")
userRegex = re.compile(toStrip)
#TODO: OPEN ALL .TXT FILES
for file in os.listdir("."):
    if file.endswith(".txt"):
        os.path.join(".",file)
        openedFile = open(os.path.join(".",file))
        openedFileRead=openedFile.readlines()
        for line in openedFileRead:
            if userRegex.search(line) != None:
                print(line)
        
        #aprint(regexSearch)
