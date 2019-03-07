import csv
import re

#Regex for links
pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
#Regex for User twitter id on retweets
pattern1 = re.compile(r'@([A-Za-z0-9_]+):')
#Regex for Image codes
pattern2 = re.compile(r'\\x[0123456789abcdef][0123456789abcdef]')
# Open the file with read only permit
f = open('test.txt')
# use readline() to read the first line 
line = f.readline()
# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty
while line:
    s = re.sub("b'", '', line)
    s = re.sub("'", '', s)
    s = re.sub('"', '', s)
    s = re.sub("RT", '', s)
    s = re.sub("#", '', s)
    s=pattern.sub('', s)
    s=pattern1.sub('', s)
    s=pattern2.sub('', s)
    s = re.sub("@", '', s)
    print(s)
    # use realine() to read next line
    line = f.readline()
f.close()

      