#!/usr/bin/env python

import pandas as pd
import numpy as np
from biom.parse import load_table
from biom.util import biom_open
import biom.table as table
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
(options, args) = parser.parse_args()


fn = sys.argv[1]

print '\n' '	Input file: ' + sys.argv[1]

t = load_table(fn)
normed = t.norm(axis='sample', inplace=False)
out = fn[:-5] + '_relativized.biom' '\n'

with biom_open(out, 'w') as f:
	normed.to_hdf5(f, 'example')

print '\n' '	Success!' '\n' '	Output file: ' + out
