#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from urllib.parse import unquote
import os
import sys

top = sys.argv[1]
out = sys.argv[2]
flist = sum([[os.path.join(base,file) for file in files] for base,dirs,files in os.walk(top)],[])

os.mkdir(out)

for i in flist:
    dirname = os.path.dirname(i)
    with open(i) as f:
        s = f.readlines()
        filename = ""
        for l in s:
            if l.startswith('Date'):
                index = s.index(l)
                p = l.strip().split()
                filename += unquote(p[1])
            if l.startswith('Slug'):
                index = s.index(l)
                p = l.strip().split()
                filename += unquote(p[-1])
                with open('%s/%s.md'%(out, filename), 'w') as g:
                        g.write(''.join(s))
                break
