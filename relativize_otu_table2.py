#!/usr/bin/env python

import pandas as pd
import numpy as np
from biom.parse import load_table
from biom.util import biom_open
import biom.table as table
import sys
import argparse
import os.path

parser = argparse.ArgumentParser(description='This is a python script to relative biom tables')

def file_choices(choices, fname):
	ext = os.path.splitext(fname)[1][1:]
#	print ext
	if ext not in choices:
		parser.error('file must be biom format')
	return fname

parser.add_argument('-f', type=lambda s:file_choices(('biom','tab'),s), help='Input BIOM file', action='store')
parser.add_argument('-q', '--quiet', action='store_false', dest='verbose', default=True,
                  help='don\'t print status messages to stdout')

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

results = parser.parse_args()

print 'Input file:', results.f
out = results.f[:-5] + '_relativized.biom'
	
t = load_table(results.f)
normed = t.norm(axis='sample', inplace=False)
out = results.f[:-5] + '_relativized.biom' '\n'

with biom_open(out, 'w') as f:
	normed.to_hdf5(f, 'example')

print '\n' '	Success!' '\n' '	Output file: ' + out
