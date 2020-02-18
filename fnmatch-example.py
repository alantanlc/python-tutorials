# This example will print all file names in the current directory with the extension .py:

import fnmatch
import os

for file in os.listdir('.'):
  if fnmatch.fnmatch(file, '*.py'):
    print(file)
