#!/usr/bin/env python3
"""from pathlib import Path
files = []
for path in Path('.').iterdir():
    print (path)
    files.append(path)
print (files)

print (files[-1])"""

import os

for file in os.listdir():
    print(file)

