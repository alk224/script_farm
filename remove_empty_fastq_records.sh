#!/usr/bin/env bash
set -e

## Check for and remove empty fastq records

input="$1"
fqext="${1##*.}"
fqname="${1%.*}"
fqdir=`dirname $1`
output="$fqname.noempties.fastq"
outext="$fqname.noempties.$fqext"
empties="$fqname.empty_records.txt"

## Test for inputs and outputs

	if [[ ! -f "$input" ]]; then
	echo "
Supplied input not found: $input
Exiting."
	exit 1
	fi
	if [[ -f $output ]]; then
	rm $output
	fi

## Test for empty records and filter if necessary

	emptycount=`grep -B 1 -e "^$" $input | grep -ce "^@"`

	if [[ "$emptycount" -ge "1" ]]; then
	echo "
Filtering $emptycount empty fastq records from input files."
		if [[ "$fqext" != "fastq" ]]; then
		mv $input $fqname.fastq
		fi
		input="$fqname.fastq"
		grep -B 1 -e "^$" $input | grep -e "^@.\+\s.\+" | sed "s/^@//g" > $empties
		filter_fasta.py -f $input -o $output -s $empties -n
	if [[ ! -f "$outext" ]]; then
	mv $output $outext
	fi
	if [[ "$input" != "$1" ]]; then
	mv $input $1
	fi
	
	echo "
Done.  Filter associated files against the empties list:
filter_fasta.pt -f input.fasta -o output -s $empties -n
"
	elif [[ "$emptycount" -eq "0" ]]; then
	echo "
No empty records found.  No lines were removed."
	fi

exit 0
