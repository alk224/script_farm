## Split libraries modification
##
## Steps:
## 1) fastq-multx
## 2) sed to add sampleid and number to fastq headers
## 3) cat result together
## 4) fastq-mcf (quality filtering)
## 5) convert to fasta
##
## Usage:
## Split_libraries_ak.sh rd.fq idx.fq map.txt
##

read=($1)
index=($2)
map=($3)
#readbase=`basename $read .fq`

## Make fastq-multx barcode file
#cat $map | grep -v "#" | cut -f1-2 > multx_barcode_file.txt
#multx_map=multx_barcode_file.txt

## Demultiplexing
#if [[ -d multx_out ]]; then
#	rm -r multx_out
#fi
#mkdir multx_out
#fastq-multx -B $multx_map $index $read -o multx_out/idx.%.fq -o multx_out/rd.%.fq 1> multx_out/multx_summary.txt
#rm multx_out/*unmatched* multx_out/idx* 2>/dev/null

## Add sample IDs and count
echo > seqout.fq
sed -i 's/^$//' seqout.fq
for file in `ls multx_out/*.fq`; do
	echo $file
	sampleid=`ls $file | basename $file .fq | cut -d. -f2-`
	seqcount0=`grep -ce "^@" $file`
	seqcount=`expr $seqcount0 - 1`
	seq 0 $seqcount > multx_out/seqcount.temp
	sed -i "s/^/$sampleid\_/g" multx_out/seqcount.temp
#	sed -i "s/^/@/g" multx_out/seqcount.temp
	grep -e "^@.\+\s" $file | cut -d" " -f1 > multx_out/headers.temp
	sed "s/^@//g" multx_out/headers.temp > multx_out/headers1.temp
	paste multx_out/seqcount.temp multx_out/headers1.temp | sed 's/\t/ /' > multx_out/newheaders.temp
	IFS=$'\n'
	for line in `cat multx_out/newheaders.temp`; do
		search=`echo $line | cut -f2`
		echo $search
		echo $line
		sed -i "s/$search/$line/g" $file
	done
	cat $file >> seqout.fq
done


