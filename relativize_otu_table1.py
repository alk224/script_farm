#!/usr/bin/env python

#import pandas as pd
#import numpy as np
from biom import load_table
#from biom.util import biom_open
#import biom.table as table

#from optparse import OptionParser
import argparse
import os.path
import os


#def file_choices(choices):
#	ext = os.path.splitext("input_biom")[1][1:]
#	if ext not in choices:
#		parser.error("Supplied file does not have .biom extension. " "\n"
#		"Is your file a valid biom table?")
#	return fname


parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input_biom', help='The path to the input biom '
	'file to be relativized.', required=True)
#parser.add_argument('-o', '--output_biom', help='The path to the output file.',
#    required=True)

def main():
	args = parser.parse_args()
	input_fp = args.input_biom
		
	if not input_fp.endswith('.biom'):
		raise argparse.ArgumentTypeError(
			'Input file must be a valid .biom file')
	return input_fp

#os._exit(1)

print '\n'


#	ext = os.path.splitext(fname)[1][1:]
#	if ext not in choices:
#		parser.error("Supplied file does not have .biom extension. " "\n"
#		"Is your file a valid biom table?")
#	return fname

#parser.add_argument('fn',type=lambda s:file_choices(("biom"),s))

	#input_table = load_table(input_fp)

#	output_fp = args.output_biom


#print (input_table)


#fn = sys.argv[1]

#print '\n' '	Input file: ' + sys.argv[1]

#t = load_table(fn)

#normed = t.norm(axis='sample', inplace=False)
#out = fn[:-5] + '_relativized.biom' '\n'

#with biom_open(out, 'w') as f:
#	normed.to_hdf5(f, 'example')

#print '\n' '	Success!' '\n' '	Output file: ' + out

if __name__ == '__main__':
    main()
