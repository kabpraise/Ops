'''

Supply filelocation/filename as a single argument
It will replace new line with comma
And output will be in filelocation/filename-out
e.g. $python newlinemedcomma.py /home/ubuntu/test
will create a file test-out with converted output

'''

#!/usr/bin/python

import sys

fin = open(str(sys.argv[1]), "r")
lineout = ""
i = 0

for line in fin.readlines():
   line = line.strip()
   if (i == 1):
      lineout = lineout + "," + line
   else:
      lineout = line
   i = 1

fin.close()
fout = open(str(sys.argv[1])+"-out", "w")
fout.write(lineout)
fout.close()
