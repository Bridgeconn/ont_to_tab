import sys
import re

if len(sys.argv) < 2:
    print "File name missing. \n Usage: python filter.py filename"
    raise NameError('File name not given.')
book = open(sys.argv[1], 'r')
wfile = open(sys.argv[1] + '_output.txt', 'w')
flag = False
for line in book.readlines():
    line = line.strip()
    if len(line) > 0:
        temp = line.split(' ')
        if len(temp) > 1:
            if not flag and temp[1] == '\xef\xbb\xbf':
                flag = True
                continue
            pos = line.find(' ')
            verse = str(line[pos+1:])
            verse = re.sub('<.+?>', '', verse)
            wfile.write(line[:pos].replace('.','	') + '	' + verse + '\n')

book.close()
wfile.close()

