# -*- coding: iso-8859-1 -*-
#open indicated file and assign it as "infile"
infile=open('serprot_pairs.out')
#reads all lines of infile. End result assigned as init
init=infile.readline()
#if index number on read line then continue script
while init[:6] !='     I':
#read the lines
	init=infile.readline()
#defines names of columns displayed in the output file.
colnames=['I', 'J', 'ILEN', 'JLEN', 'MATCH', 'NGAPS', 'NALIG', 'NIDENT', '%IDENT', 'NAS', 'NASAL', 'NRANS', 'RMEAN', 'STEDEV', 'SCORE', 'NUMBER']
#assign indicated file as "filename"
filename='serprot_file.txt'
#open file for writing
file=open(filename, 'w')
#add tab between columns and write to output file
for c in colnames:
        file.write(c + '\t')
for line in infile.readlines():
#Initiate a try for error checking
	try:
#If first 2 lines are " T" then continue
		if line[:2]==' T':
			continue

		I=line[1:6]
		J=line[7:11]
		ILEN=line[12:16]
		JLEN=line[17:21]
 		MATCH=line[22:31]
		NGAPS=line[32:38]
 		NALIG=line[39:45]
		NIDENT=line[46:52]
		IDEN=line[53:62]
		NAS=line[63:72]
		NASAL=line[73:82]
		NRANS=line[83:89]
		RMEAN=line[90:99]
		STDEV=line[100:109]
		SCORE=line[110:119]
		NUMBER=line[120:126]
	
#write output file
		file.write('\n' + I + '\t' + J + '\t' + ILEN + '\t' + JLEN + '\t' + MATCH + '\t' + NGAPS + '\t' + NALIG + '\t' + NIDENT + '\t' + IDEN + '\t' + NAS + '\t' + NASAL + '\t' + NRANS + '\t' + RMEAN + '\t' + STDEV + '\t' + SCORE + '\t' + NUMBER)
 	except:
		pass
#closes file
file.close()

