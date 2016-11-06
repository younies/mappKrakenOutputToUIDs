
#!/usr/bin/python
"""
This program for converting the Kraken output to two ids
"""

import os
import sys
import subprocess
import re
import commands


mapper = {
	 "hydrophila": 1321367,
   "cereus" :  1441464,
  "fragilis" : 1422847,
   "abscessus" : 1335417,
   "fermentans" : 1149860,
   "sphaeroides" : 272943,
   "aureus" :  1280 ,
   "pneumoniae" : 1449971,
   "cholerae" :  1420885,
   "axonopodis" : 1437877,
}


kraken_output_path 	= ""
names_path 		 	= ""

kraken = open(kraken_output_path)
names = open(names_path)

def getUIDFromHiSeq(dna):
	for ( key,  uid) in mapper.items():
		if( dna.find(key) > -1 ):
			return uid
		
	print "error"
	print dna
	return -1


def getUIDfromTailHiSeq(tail, names):
	for name in  names:
		if(name.find(tail) > -1):
			return name.split()[0]

	print "error tail"
	print tail
	return -1



def getUIDs(kraken_line, names ):
	kraken_line = kraken_line.strip()
	(header , output) = kraken_line.split('\t')
	input_uid = getUIDFromHiSeq(header)
	output_uid = getUIDfromTailHiSeq(output , names)
	return (input_uid , output_uid)



#deal with kraken

kraken_lines = kraken.read()
kraken_lines = kraken_lines.split("\n")

for i in range(len(kraken_lines)):
	kraken_lines[i] = kraken_lines[i].strip()
	kraken_lines






















